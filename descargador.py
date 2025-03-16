import yt_dlp

def descargar_video(url):
    opciones = {
        'outtmpl': '%(title)s.%(ext)s',  # Guarda con el nombre del video
        'format': 'bestvideo+bestaudio/best'  # Mejor calidad disponible
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Ingresa la URL del video de YouTube: ")
    descargar_video(url)
