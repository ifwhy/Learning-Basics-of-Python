import qrcode as QR
import image as img
qr = QR.QRCode(
    version = 1.5,
    box_size = 10,
    border = 5
)

# Link di bawah hanya sebagai contoh
# Ganti link di bawah dengan link yang diperlukan
data = "https://github.com/ifwhy"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("text.png")