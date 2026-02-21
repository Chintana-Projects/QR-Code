import qrcode
from PIL import Image, ImageDraw

def generate_qr(data, save_location, fill_color, back_color, size, shape):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=size,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_matrix = qr.get_matrix()
    modules_count = len(qr_matrix)

    img_size = modules_count * size
    img = Image.new("RGBA", (img_size, img_size), back_color)
    draw = ImageDraw.Draw(img)

    for row in range(modules_count):
        for col in range(modules_count):
            if qr_matrix[row][col]:
                x1 = col * size
                y1 = row * size
                x2 = x1 + size
                y2 = y1 + size

                if shape.lower() == "circle":
                    draw.ellipse((x1, y1, x2, y2), fill=fill_color)
                else:
                    draw.rectangle((x1, y1, x2, y2), fill=fill_color)

    if not save_location.lower().endswith(".png"):
        save_location += ".png"

    img.save(save_location, format="PNG")
    print(f"QR Code saved successfully at {save_location}!")

def main():
    print("Choose the QR code type:")
    print("1. Text")
    print("2. URL")
    print("3. Phone Number")
    print("4. Email")
    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        data = input("Enter the text: ")
    elif choice == "2":
        data = input("Enter URL (including http:// or https://): ")
    elif choice == "3":
        phone = input("Enter phone number: ")
        data = f"tel:{phone}"
    elif choice == "4":
        email = input("Enter email address: ")
        data = f"mailto:{email}"
    else:
        data = input("Enter the text: ")

    save_location = input("Enter save location (example: qr_code or path/qr_code.png): ")

    print("Choose a fill color:")
    print("1. Black")
    print("2. Red")
    print("3. Blue")
    fill_choice = input("Enter choice (1/2/3): ")

    if fill_choice == "1":
        fill_color = (0, 0, 0)
    elif fill_choice == "2":
        fill_color = (255, 0, 0)
    elif fill_choice == "3":
        fill_color = (0, 0, 255)
    else:
        fill_color = (0, 0, 0)

    print("Choose a background color:")
    print("1. Yellow")
    print("2. Pink")
    print("3. White")
    back_choice = input("Enter choice (1/2/3): ")

    if back_choice == "1":
        back_color = (255, 255, 0)
    elif back_choice == "2":
        back_color = (255, 192, 203)
    elif back_choice == "3":
        back_color = (255, 255, 255)
    else:
        back_color = (255, 255, 255)

    size = int(input("Enter the QR box size (5–30 recommended): "))

    print("Choose shape style:")
    print("1. Square")
    print("2. Circle")
    shape_choice = input("Enter choice (1/2): ")

    shape = "circle" if shape_choice == "2" else "square"

    generate_qr(data, save_location, fill_color, back_color, size, shape)

if __name__ == "__main__":
    main()
