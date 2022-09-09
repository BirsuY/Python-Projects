#birsuyilmaz
import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("QRimage.png")
    
generate_qrcode("https://www.youtube.com/channel/UCKyig8Lr1nmu2CFY-SL1HpA")

url = input("Please enter to url: ")
generate_qrcode(url)
#birsuyilmaz