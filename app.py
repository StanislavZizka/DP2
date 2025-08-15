from flask import Flask, render_template, request, jsonify, url_for, send_from_directory
import os
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for serverless
from models.activator_inhibitor import generate_texture

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/activator_inhibitor')
def activator_inhibitor():
    return render_template('activator_inhibitor.html')


@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('assets', filename)


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        
        # DEBUG: Výpis hodnot přijatých z frontendové části
        print("Přijatá data:", data)

        # Validace vstupů
        K = float(data.get('K', 1.0))
        t_max = float(data.get('t_max', 10.0))
        delta_t = float(data.get('delta_t', 0.1))
        color1 = data.get('color1', "#0000ff")
        color2 = data.get('color2', "#ff0000")

        print(f"DEBUG: Zpracované hodnoty -> K={K}, t_max={t_max}, delta_t={delta_t}")

        # Generování textury
        image_path = generate_texture(K, t_max, delta_t, color1, color2)
        print(f"DEBUG: Obrázek úspěšně vygenerován -> {image_path}")

        image_url = url_for('static', filename='images/activator_inhibitor_texture.png', _external=True)


        return jsonify({'image_url': image_url})
    
    except Exception as e:
        print(f"CHYBA: {str(e)}")
        return jsonify({'error': str(e)}), 500


# Vercel needs this for serverless deployment
# Export the app object for Vercel
application = app

if __name__ == '__main__':
    app.run(debug=True)
