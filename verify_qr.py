from pyzbar.pyzbar import decode
from PIL import Image
import os

def verify_qr(image_path):
    """
    Decodes a QR code and prints its content to verify it's static.
    """
    if not os.path.exists(image_path):
        print(f"Error: El archivo {image_path} no existe.")
        return

    # Decode the QR code
    decoded_objects = decode(Image.open(image_path))
    
    if not decoded_objects:
        print("No se encontró ningún código QR en la imagen.")
        return

    for obj in decoded_objects:
        print(f"Tipo: {obj.type}")
        print(f"Contenido: {obj.data.decode('utf-8')}")
        print("-" * 20)
    
    print("\nSi el contenido coincide exactamente con tu enlace, el QR es 'inerte' (estático),")
    print("ya que la información está grabada directamente en los puntos del código.")

if __name__ == "__main__":
    verify_qr("static_qr.png")
