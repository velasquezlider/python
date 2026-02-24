import qrcode
import os

def generate_static_qr(data, filename="static_qr.png"):
    """
    Generates a static (inerte) QR code from the provided data.
    """
    print(f"Generando QR para: {data}")
    
    # Create QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(filename)
    print(f"Código QR guardado como: {os.path.abspath(filename)}")

if __name__ == "__main__":
    # Example data (updated with user link)
    data_to_encode = "https://docs.google.com/forms/d/e/1FAIpQLScy2QR89Mc1PhgV39kGGTduvSt5SikF-thF2Ty6IZXxCwu4rg/viewform"
    generate_static_qr(data_to_encode)
