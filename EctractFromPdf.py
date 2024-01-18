import csv
from PyPDF2 import PdfReader, PdfWriter
import re
import pandas as pd
def extract_text_from_pdf(pdf_path):
    pdf_file = open(pdf_path, "rb")
    pdf_reader = PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    count = 0
    text = ""
    while count < num_pages:
        pageObj = pdf_reader.pages[count]
        count += 1
        text += pageObj.extract_text()
    if text != "":
        text = text
    else:
        text = "No text found"
    return text

def create_csv_from_text(pdf_path, csv_path, columns):
    text = extract_text_from_pdf(pdf_path)
    transactions = get_transactions(text)
    sub_list = list()
    for my_transactions in transactions:
        split = my_transactions.split()
        "".join(split[1:7])
        sub_list.append(split)

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(columns)
        csv_writer.writerows(sub_list)
    return print("CSV file created successfully")

def get_transactions(text):
    pattern = re.compile(r"\d{2}-[0-9]{2}-\d{4}")
    transactions = list()
    lines = text.split('\n')
    for line in lines:
        if pattern.match(line):
            if line in transactions:
                continue
            else:
                transactions.append(line)
        else:
            continue
    return transactions


def rotate_pdf(pdf_path, rotated_pdf_path):
    pdf_file = open(pdf_path, "rb")
    pdf_reader = PdfReader(pdf_file)
    pdf_writer = PdfWriter()
    for page in pdf_reader.pages:
        pdf_writer.add_page(page.rotate(90))
    with open(rotated_pdf_path, "wb") as fh:
        pdf_writer.write(fh)
    return rotated_pdf_path


columns = ["Date", "Value Date", "Description", "Nurrative", "Cheque Number", "Balance", "Debit", "Credit",
           "Running Balance"]
pdf_path = "/home/dbiwott/Downloads/nipon.pdf"
csv_path = "/home/dbiwott/Downloads/Energy.csv"
create_csv_from_text("/home/dbiwott/Downloads/tabithaaccountstatementrafiki-2.pdf",
                     "/home/dbiwott/Downloads/Tabitha2.csv", ["Date", "Description", "Debit", "Credit", "Balance"])

rotated_path = rotate_pdf(pdf_path, "/home/dbiwott/Downloads/rotated.pdf")
create_csv_from_text(rotated_path, csv_path, columns)
