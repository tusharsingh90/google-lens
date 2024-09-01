from PIL import Image
from pytesseract import pytesseract as pt
import pyautogui as pag
import os 

from tkinter.filedialog import askopenfile

def text_extractor(image_path):
    tesseract_path = r'C:\Program Files\Tesseract-OCR '
    pt.tesseract_cmd = tesseract_path

    img = Image.open(image_path)

    text = pt.image_to_string(img)
    
    return text

image = askopenfile()
image_address= image.name
para = text_extractor(image_address)
 
# Gives time so that you can switch to the required tab.
pag.countdown(5)

permission = pag.prompt("Are you Ready?")
# Will only execute if the answer is "yes" or "YES"
if permission.lower() == "yes":
    pag.typewrite(para,0.1) # this 0.10 represents the ms in which each character would be printed
    # pag.typewrite(para,0.0600) # this 0.10 represents the ms in which each character would be printed

image.close()
# os.remove(image_address)
    