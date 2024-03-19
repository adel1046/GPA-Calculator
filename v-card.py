import qrcode
from vobject import vCard

vcard = vCard()
vcard.add('Fn').value = input("Name:")
vcard.add('Email').value = input("Email: ")
vcard.add('tel').value = input("phone number: ")

vcard_info = vcard.serialize()

qr = qrcode.QRCode(version = 5)
qr.add_data(vcard_info)
qr.make()

img = qr.make_image()
img.save("V-card1.png")