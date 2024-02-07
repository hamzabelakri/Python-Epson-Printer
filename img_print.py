from PIL import Image, ImageDraw, ImageFont
from escpos.printer import Usb

def generate_image_from_text(text,font_path, image_size=(400, 200), background_color=255):
    # Create a blank image with the specified background color
    image = Image.new("L", image_size, background_color)

    # Load the default font
    font = ImageFont.load_default()

 # Load the Arabic font
    font = ImageFont.truetype(font_path, 30, layout_engine=ImageFont.LAYOUT_RAQM)


    # Get a drawing context
    draw = ImageDraw.Draw(image)

    # Calculate text size and position
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)

    # Draw text on the image
    draw.text(text_position, text, fill=0, font=font)

    return image

if __name__ == "__main__":
    text_to_generate = "Hello, World! مرحبا بالعالم"
    font_path = "Cairo-VariableFont_slnt,wght.ttf"  

    # Generate the image from text
    generated_image = generate_image_from_text(text_to_generate,font_path)

    # Save or display the generated image
    generated_image.show()  # Display the image
    # To save the image, use: generated_image.save("output_image.png")
    """ Seiko Epson Corp. Receipt Printer (EPSON TM-T88V) """
    #p = Usb(0x04b8, 0x0202, 0, profile="TM-T88V")
    #p.image(generated_image)

    #p.ln(10)