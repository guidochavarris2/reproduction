from flask import Flask, request, send_from_directory, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ruta principal para mostrar la página
@app.route('/')
def index():
    return render_template('index.html')

# Servir archivos estáticos (videos subidos)
@app.route('/static/<filename>')
def serve_static(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Endpoint para subir el video
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return "No se encontró ningún archivo", 400

    file = request.files['video']
    if file.filename == '':
        return "Nombre de archivo vacío", 400

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return "Archivo subido con éxito", 200

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
