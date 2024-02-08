from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from starlette.background import BackgroundTasks
from PIL import Image
import imgkit 

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Receipt(BaseModel):
    receipt_id: str
    payment_date: str
    entry_date: str
    ticket_id: str
    epan: str
    length_of_stay: str
    parking_fees: str
    vat_percentage: str
    vat_amount: str
    total_amount: str

def generate_image(receipt_data: dict):
    html_file = 'receipt.html'  # Update the path to the template
    image_file = 'receipt.png'
    options = {
        'quiet': '',
        'disable-smart-width': '',
        'width': '512'
    }
    imgkit.from_file(html_file, image_file, options=options)
    image = Image.open(image_file)
    image.show()

@app.post("/generate_receipt/")
async def generate_receipt(request: Request, receipt: Receipt, background_tasks: BackgroundTasks):
    background_tasks.add_task(generate_image, receipt.dict())
    return {"message": "Receipt generated and will be printed shortly.", "receipt_data": receipt}

@app.get("/preview_receipt/")
async def preview_receipt(request: Request, receipt: Receipt):
    return templates.TemplateResponse("receipt.html", {"request": request, "receipt_data": receipt})
