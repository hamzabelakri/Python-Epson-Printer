from PIL import Image
from escpos.printer import Usb
import subprocess
import imgkit  # Import imgkit module

html_file = 'receipt.html'

image_file = 'receipt.png'

options = {
    'quiet': '',
    'disable-smart-width': '',
    'width': '400'
}

imgkit.from_file(html_file, image_file, options=options)

image = Image.open(image_file)

image.show()

""" printer = Usb(0x04b8, 0x0202, 0, profile="TM-T88V")

with open(image_file, 'rb') as f:
    printer.image(Image.open(f))

printer.cut() """
