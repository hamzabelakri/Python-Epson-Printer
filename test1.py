import os
from io import BytesIO, open
from escpos.printer import Usb
from escpos_xml import parse
xml = BytesIO( bytes('''
<receipt width="48">
    <h1>Receipt!</h1>
    <ul>
        <li>
            <span align="left" width="22">Product</span>
            <span align="right" width="24">0.15€</span>
        </li>
    </ul>
    <hr/>
    <p size="2h">
        <span align="left" width="24">TOTAL</span>
        <span align="right" width="24">0.15€</span>
    </p>
    <barcode encoding='ean13'>
        5449000000996
    </barcode>
    <cashdraw pin="2"/>
    <cut/>
</receipt>''', 'utf-8'))
printer = Usb(0x04b8, 0x0202)
parse(printer, xml)
parse(printer,
     open(os.path.join('escpos_xml', 'tests', 'image.xml'), 'rb'))