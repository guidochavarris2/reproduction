from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os

app = Flask(__name__)

# Crear carpeta "static" si no existe  eeee
os.makedirs('static', exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return "No se subió ningún archivo", 400

    file = request.files['video']
    if file.filename == '':
        return "Nombre de archivo inválido", 400

    file.save(os.path.join('static', 'KARDEX.mp4'))
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
