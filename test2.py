from time import sleep
from escpos.printer import Usb
import text_to_image

""" Seiko Epson Corp. Receipt Printer (EPSON TM-T88V) """
p = Usb(0x04b8, 0x0202, 0, profile="TM-T88V")
#print(p.hw('RESET'))
#encoded_image_path = text_to_image.encode("HELLO WORLD" ,"image.png")
#print(p.image(encoded_image_path))

# Set the printer encoding to Arabic
#p.codepage = 'cp1256'
# Print the Arabic text from right to left
# Arabic text to print
#arabic_text = "مرحبا بالعالم"

# Reverse the Arabic text to print from right to left
#reversed_arabic_text = arabic_text[::-1]

# Print the Arabic text
#p.text(reversed_arabic_text + '\n')

# Send a command to check printer status
#status = p.query_status(b'RT_STATUS_ONLINE')
#print(f'status:{status}')
# Check the status response

#tatus = p.query_status(b'RT_STATUS_PAPER')
#print(f'status:{status}')
sleep(3)
print(p.is_online())
sleep(5)
print(p.is_usable())
sleep(5)
print(p.paper_status())
sleep(5)
# Close the connection to the printer
p.close()

#p.image("logo.gif")
#p.barcode('4006381333931', 'EAN13', 64, 2, '', '')
 #p.cut()