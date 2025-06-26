import qrcode

def generate_qr(data, filename="output_qr.png"):
    qr = qrcode.QRCode(
        version=1,  # size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"✅ QR code saved as {filename}")

if __name__ == "__main__":
    print("=== QR Code Generator ===")
    user_input = input("Enter the text or URL to generate QR code: ")
    generate_qr(user_input)
