import yt_dlp
import os
from utils import manejar_excepcion

def descargar_video():
    try:
        url = input('Introduce la URL del video de YouTube: ')

        # Crear la carpeta 'downloads' si no existe
        output_folder = os.path.join(os.getcwd(), "downloads")
        os.makedirs(output_folder, exist_ok=True)

        # Configuración para descargar en la mejor calidad de video y audio
        ydl_opts = {
            'format': 'best',  # Selecciona el mejor video y audio y los combina
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Guarda en la carpeta 'downloads'
            'merge_output_format': 'mp4',  # Formato final combinado
            'noplaylist': True,  # Evitar listas de reproducción completas
            'verbose': True  # Activar modo detallado para depuración
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)  # Extrae la información del video sin descargar
            print(f"Título: {info.get('title')}")
            print(f"URL de la miniatura: {info.get('thumbnail')}")
            
            # Iniciar la descarga
            print("Descargando en máxima calidad con audio...")
            ydl.download([url])
            print(f"¡Descarga completada! El archivo se guardó en la carpeta '{output_folder}' y contiene video y audio.")
    except Exception as e:
        manejar_excepcion(e)
