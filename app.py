import os
from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__)

UPLOAD_FOLDER = 'static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Asegura que la carpeta exista
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return "No se seleccionó archivo", 400
    file = request.files['video']
    if file.filename == '':
        return "Nombre de archivo vacío", 400
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    return "Archivo subido con éxito", 200

@app.route('/static/<filename>')
def serve_static(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Lee el puerto de Railway
    app.run(host='0.0.0.0', port=port)
