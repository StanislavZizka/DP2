"""
Texture generation service containing business logic for mathematical texture algorithms.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for serverless
import matplotlib.pyplot as plt
import os
from config import IMAGES_DIR, SIMULATION_PARAMS, DEFAULT_TEXTURE_SIZE
from utils.helpers import hex_to_rgb

class TextureGeneratorService:
    """Service class for generating mathematical textures."""
    
    def __init__(self):
        """Initialize the texture generator service."""
        # Ensure images directory exists
        os.makedirs(IMAGES_DIR, exist_ok=True)
    
    def generate_activator_inhibitor(self, K: float, t_max: float, delta_t: float, 
                                   color1: str, color2: str, size: int = DEFAULT_TEXTURE_SIZE) -> str:
        """
        Generate texture using activator-inhibitor reaction-diffusion model.
        
        Args:
            K: Model constant (reaction rate)
            t_max: Maximum simulation time
            delta_t: Time step for simulation
            color1: First color in HEX format (activator)
            color2: Second color in HEX format (inhibitor)
            size: Texture dimensions (default from config)
            
        Returns:
            str: Path to generated image file
        """
        # Initialize grid with small random fluctuations
        A = np.ones((size, size)) * 0.5  # Activator
        B = np.ones((size, size)) * 0.25  # Inhibitor
        
        # Add noise as initial stimulus
        np.random.seed(SIMULATION_PARAMS['random_seed'])
        noise = (np.random.rand(size, size) - 0.5) * 0.1
        A += noise
        B += noise
        
        # Get simulation parameters from config
        D_a = SIMULATION_PARAMS['D_a']
        D_b = SIMULATION_PARAMS['D_b']
        feed_rate = SIMULATION_PARAMS['feed_rate']
        kill_rate = SIMULATION_PARAMS['kill_rate']
        
        # Run simulation
        steps = int(t_max / delta_t)
        for step in range(steps):
            # Calculate Laplacian for diffusion
            A_laplace = self._calculate_laplacian(A)
            B_laplace = self._calculate_laplacian(B)
            
            # Apply reaction-diffusion equations
            reaction = A * B**2
            A += delta_t * (D_a * A_laplace - reaction + feed_rate * (1 - A))
            B += delta_t * (D_b * B_laplace + reaction - (kill_rate + feed_rate) * B)
            
            # Log progress every 100 steps
            if step % 100 == 0:
                print(f"Simulation step {step}/{steps}: A range=[{np.min(A):.4f}, {np.max(A):.4f}], "
                      f"B range=[{np.min(B):.4f}, {np.max(B):.4f}]")
        
        # Create and save image
        image_path = self._create_texture_image(A, B, color1, color2, size)
        return image_path
    
    def _calculate_laplacian(self, grid: np.ndarray) -> np.ndarray:
        """
        Calculate Laplacian operator for diffusion simulation.
        
        Args:
            grid: 2D numpy array representing the concentration field
            
        Returns:
            np.ndarray: Laplacian of the input grid
        """
        return (
            np.roll(grid, 1, axis=0) + np.roll(grid, -1, axis=0) +
            np.roll(grid, 1, axis=1) + np.roll(grid, -1, axis=1) - 4 * grid
        )
    
    def _create_texture_image(self, A: np.ndarray, B: np.ndarray, 
                            color1: str, color2: str, size: int) -> str:
        """
        Create and save texture image from simulation results.
        
        Args:
            A: Activator concentration grid
            B: Inhibitor concentration grid
            color1: First color in HEX format
            color2: Second color in HEX format
            size: Image dimensions
            
        Returns:
            str: Path to saved image file
        """
        # Normalize values to [0, 1] range
        A_norm = np.clip((A - np.min(A)) / (np.max(A) - np.min(A)), 0, 1)
        B_norm = np.clip((B - np.min(B)) / (np.max(B) - np.min(B)), 0, 1)
        
        # Convert colors from HEX to RGB
        color1_rgb = np.array(hex_to_rgb(color1))
        color2_rgb = np.array(hex_to_rgb(color2))
        
        # Create RGB image
        img_data = np.zeros((size, size, 3))
        for i in range(3):
            img_data[:, :, i] = np.clip(color1_rgb[i] * A_norm + color2_rgb[i] * B_norm, 0, 1)
        
        # Save image
        output_path = os.path.join(IMAGES_DIR, "activator_inhibitor_texture.png")
        plt.imsave(output_path, img_data)
        
        return output_path