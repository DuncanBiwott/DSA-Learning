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
        replaced_string = transaction.replace(',', '')
        splitted_list = replaced_string.split()
        # reg_split= re.split(check_float_pattern, transaction,maxsplit=2)
        date = splitted_list[0]
        mid_list = splitted_list[1:-3]
        last_list = splitted_list[-3:]
        for i in range(len(last_list)):
            if_string=last_list[i]
            if check_float_pattern.match(last_list[i]):
                last_list[i] = float(last_list[i])
            else:
                mid_list.append(last_list[i])
                last_list[i] = 0.0

        # Create a new joined_list for each iteration
        joined_list = [date, " ".join(mid_list)]
        joined_list.extend(last_list)
        # Append the joined_list to sub_list directly
        sub_list.append(joined_list)

    # df = pd.DataFrame(sub_list, columns=columns)

    # print(df)
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
                     "/home/dbiwott/Downloads/Modified9.csv", ["Date", "Description", "Debit", "Credit","Balance"])

rotated_path = rotate_pdf(pdf_path, "/home/dbiwott/Downloads/rotated.pdf")
# create_csv_from_text(rotated_path, csv_path, columns)

# my_string='01-Dec-2022 QL1619VA2S From ::A/C 0082020000687 [TABITHA NYAWI  5,714.03  518.00'
# print(my_string)
# replaced_string=my_string.replace(',','')
# print(replaced_string)
# split_dec=re.split(r'(\d+\.\d+)',replaced_string)
# print(split_dec)


