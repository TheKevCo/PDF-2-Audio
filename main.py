import requests
from pathlib import Path
import PyPDF2
import os

input_text = ""
pdfFileObj = open('example.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

for i in range(pdfReader.numPages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    input_text += text + " "

pdfFileObj.close()
filename = Path('speech.mp3')
url = "http://api.voicerss.org/"

querystring = {"key": os.environ['API_KEY'],
               "hl": "en-us",
               "src": f"{input_text}",
               "f": "8khz_8bit_mono",
               "c": "mp3",
               "r": "0"}

response = requests.request("GET", url, params=querystring)
filename.write_bytes(response.content)
