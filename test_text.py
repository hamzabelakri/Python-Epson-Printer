from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
from escpos.printer import Usb
import os

def read_text_from_html(html_content):
    if os.path.isfile(html_content):
        with open(html_content, 'r') as file:
            html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()
    return text.strip()

def generate_image_from_text(text, font_path, image_size=(512, 700), background_color=255):
    image = Image.new("L", image_size, background_color)
    font = ImageFont.truetype(font_path, 30, layout_engine=ImageFont.LAYOUT_RAQM)
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
    draw.text(text_position, text, fill=0, font=font)
    return image

font_path = "Cairo-VariableFont_slnt,wght.ttf"
html_file = "receipt.html"
text_to_generate = read_text_from_html(html_file)

text="##----------مرحبا بالعالم-------------------"
# Generate image
generated_image = generate_image_from_text(text_to_generate, font_path)
generated_image.show()
printer = Usb(0x04b8, 0x0202, 0, profile="TM-T88V")
printer.image(generated_image)
printer.ln(5)
#printer.cut()