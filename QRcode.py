import qrcode
import matplotlib.pyplot as plt

# create a QR code from a string
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
string = input("Enter string: ")
qr.add_data(string)
try:
    qr.make(fit=True)
except qrcode.exceptions.DataOverflowError:
    print("\n" + "String too long.")
    exit()

# plot the QR code
img = qr.make_image(fill_color="black", back_color="white")
plt.imshow(img, interpolation="nearest")
# Fix the weird colors
# https://github.com/opencv/opencv/issues/10587#issuecomment-357503558
plt.imshow(img, cmap='Greys_r')
plt.show()