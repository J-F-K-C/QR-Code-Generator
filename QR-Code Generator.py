#!/usr/bin/env python3
import qrcode

url = str(input("Your URL: "))

#Creating QR-Code
qr = qrcode.QRCode(
    version = 10,
    box_size = 10,
    border = 4)

#Adding a link for the QR code to open
link = url
qr.add_data(link)
qr.make(fit=True)

#Choose Color and save as picture
img = qr.make_image(fill_color = 'white', back_color = 'red')
img.save('qrcode.png')