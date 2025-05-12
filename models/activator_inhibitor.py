import numpy as np
import matplotlib.pyplot as plt
import os

# Konverze HEX barvy na RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def generate_texture(K: float, t_max: float, delta_t: float, color1: str, color2: str, size=512):
    """
    Vylepšená simulace aktivátor-inhibitor modelu pro vytvoření učebnicového vzoru.
    
    :param K: Konstanta modelu
    :param t_max: Maximální čas simulace (doporučeno min. 1000)
    :param delta_t: Časový krok
    :param color1: První barva v HEX (aktivátor)
    :param color2: Druhá barva v HEX (inhibitor)
    :param size: Rozměr textury (defaultně 512x512)
    :return: Cesta k vygenerovanému obrázku
    """

    # Inicializace mřížky s malými náhodnými fluktuacemi
    A = np.ones((size, size)) * 0.5  # Aktivátor
    B = np.ones((size, size)) * 0.25  # Inhibitor

    # Přidání náhodných bodů jako iniciační podnět
    np.random.seed(42)
    noise = (np.random.rand(size, size) - 0.5) * 0.1  # Náhodný šum
    A += noise
    B += noise

    # Simulační parametry
    D_a = 0.02  # Difuze aktivátoru (nižší)
    D_b = 0.1   # Difuze inhibitoru (5x vyšší než D_a)
    feed_rate = 0.035  # Produkce aktivátoru
    kill_rate = 0.06  # Odstraňování inhibitoru

    # Simulační cyklus
    for step in range(int(t_max / delta_t)):
        # Laplacián pro difuzi
        A_laplace = (
            np.roll(A, 1, axis=0) + np.roll(A, -1, axis=0) +
            np.roll(A, 1, axis=1) + np.roll(A, -1, axis=1) - 4 * A
        )
        B_laplace = (
            np.roll(B, 1, axis=0) + np.roll(B, -1, axis=0) +
            np.roll(B, 1, axis=1) + np.roll(B, -1, axis=1) - 4 * B
        )

        # Reakčně-difuzní rovnice (aktivátor-inhibitor model)
        reaction = A * B**2
        A += delta_t * (D_a * A_laplace - reaction + feed_rate * (1 - A))
        B += delta_t * (D_b * B_laplace + reaction - (kill_rate + feed_rate) * B)

        # Každých 100 iterací vypiš stav
        if step % 100 == 0:
            print(f"Step {step}: A min={np.min(A):.4f}, max={np.max(A):.4f} | B min={np.min(B):.4f}, max={np.max(B):.4f}")

    # Normalizace hodnot 0,1 mi umožnuje generovat se světlýma barvama
    A = np.clip((A - np.min(A)) / (np.max(A) - np.min(A)), 0, 1)
    B = np.clip((B - np.min(B)) / (np.max(B) - np.min(B)), 0, 1)

    # Převod barev
    color1_rgb = np.array(hex_to_rgb(color1))  # Barva aktivátoru
    color2_rgb = np.array(hex_to_rgb(color2))  # Barva inhibitoru

    # Kombinování do textury
    img_data = np.zeros((size, size, 3))
    for i in range(3):
           img_data[:, :, i] = np.clip(color1_rgb[i] * A + color2_rgb[i] * B, 0, 1)

    # Uložení obrázku
    output_dir = "static/images"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "activator_inhibitor_texture.png")

    plt.imsave(output_path, img_data)

    return output_path
