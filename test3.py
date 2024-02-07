from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
from escpos.printer import Usb
import os    
import pdfkit

def read_text_from_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()
    return text.strip()

def generate_image_from_text(text, font_path, image_size=(512, 900), background_color=255):
    image = Image.new("L", image_size, background_color)
    font = ImageFont.truetype(font_path, 30, layout_engine=ImageFont.LAYOUT_RAQM)
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
    draw.text(text_position, text, fill=0, font=font)
    return image

if __name__ == "__main__":
    html_content = """
    <html>
    <body>
    <p>Scheidt &amp; Bachmann</p>
    <p>Breite Str. 132, 41238</p>
    <p>M&ouml;nchengladbach Germany</p>
    <p>Receipt ID: 0001/1588862061</p>
    <p>Payment Date: 04-05-2020 16:41:20</p>
    <p>Entry Date: 04-05-2020 12:30:40</p>
    <p>Ticket ID: MG471</p>
    <p>EPAN:</p>
    <p>02990107003011310015414620??</p>
    <p>Length of Stay: 0 day 2 hours 10 min</p>
    <p>Parking fees : 4.05 &euro;</p>
    <p>VAT (19 %): 0.95 &euro;</p>
    <p>Total amount: 5.00 &euro;</p>
    <p>Thank you and drive safely</p>
    </body>
    </html>
    """
    font_path = "Cairo-VariableFont_slnt,wght.ttf"
    
    text_to_generate = read_text_from_html(html_content)

    generated_image = generate_image_from_text(text_to_generate, font_path)
    generated_image.show()  


    max_width = 512
    width_percent = (max_width / float(generated_image.size[0]))
    new_height = int((float(generated_image.size[1]) * float(width_percent)))
    resized_image = generated_image.resize((max_width, new_height), Image.ANTIALIAS)

    printer = Usb(0x04b8, 0x0202, 0, profile="TM-T88V")  
    printer.image(resized_image)  
    printer.ln(10)  
    printer.cut()
