# import fitz
# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     page1 = doc[0]
#     words = page1.get_text("words")
#     print(words)
#
# extract_text_from_pdf("/home/dbiwott/Downloads/tabithaaccountstatementrafiki-2.pdf")


from PyPDF2 import PdfReader
import re

import pandas as pd

# Open the PDF file
pdf_file = open("/home/dbiwott/Downloads/tabithaaccountstatementrafiki-2.pdf", "rb")

# Create a reader instance
pdf_reader = PdfReader(pdf_file)
num_pages = len(pdf_reader.pages)
count = 0
text = ""

# The while loop will read each page
while count < num_pages:
    pageObj = pdf_reader.pages[count]
    count += 1
    text += pageObj.extract_text()
    # text+="+++++++"

# This if statement exists to check if the above library returned words. It's done because PyPDF2 cannot read scanned files.
if text != "":
    text = text

else:
    print("Cannot process Scanned PDF")
#To write a regular expression to extract the data from the text

# print(text.split("\n"))
lines = text.split("\n")
header = list()
for line in lines:

    if str(line).__contains__("Opening Balance"):
        continue
    print(line)


metadata = {
    "Client_Name": "",
    "Opening_Balance": "",
    "Statement_Period": "",

}

count = 0

# while count < len(lines):
#     print(lines[0])
#     print(lines[1])
#     print(lines[2])
#     print(lines[3])
#     print("**********************************************************************************************")
#     count += 1

