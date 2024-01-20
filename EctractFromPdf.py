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
    check_float_pattern = re.compile(r"(\d+\.\d+)")
    text = extract_text_from_pdf(pdf_path)
    transactions = get_transactions(text)

    # Initialize sub_list directly as a list of lists
    sub_list = []

    for transaction in transactions:
        splited_list = transaction.split()
        date = splited_list[0]
        mid_list = splited_list[1:-2]
        last_list = splited_list[-2:]

        # Create a new joined_list for each iteration
        joined_list = [date, " ".join(mid_list)]
        joined_list.extend(last_list)

        # Append the joined_list to sub_list directly
        sub_list.append(joined_list)

        print(sub_list)

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(columns)
        csv_writer.writerows(sub_list)

    print("CSV file created successfully")

def get_transactions(text):
    pattern = re.compile(r"\d{2}-[A-Za-z]{3}-\d{4}")
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
                     "/home/dbiwott/Downloads/Modified9.csv", ["Date", "Description", "Debit", "Credit", "Balance"])

# rotated_path = rotate_pdf(pdf_path, "/home/dbiwott/Downloads/rotated.pdf")
# create_csv_from_text(rotated_path, csv_path, columns)
