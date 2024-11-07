from pytube.exceptions import PytubeError

def manejar_excepcion(e):
    if isinstance(e, PytubeError):
        print(f"Error al procesar el video: {e}")
    else:
        print(f"Ha ocurrido un error inesperado: {e}")
