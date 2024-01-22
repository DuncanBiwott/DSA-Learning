#Extract using pdfplumber


import pdfplumber
import pandas as pd
def extract_data(pdf_path):
    pdfplumber_obj = pdfplumber.open(pdf_path)
    pages = pdfplumber_obj.pages
    page = pages[0]
    table = page.extract_table()
    df = pd.DataFrame(columns=table[0])
    # Traverse through each page
    for i in range(len(pages)):
        page = pages[i]
        table = page.extract_table()
        # storing as dataframe from every table from 1 index (header is already there)
        each_page_data = pd.DataFrame(table[1:], columns=df.columns)
        # Adding each df to main df by using concat (Eg :sum of numbers in array)
        df = pd.concat([df, each_page_data], ignore_index=True)
    return df.to_csv('/home/dbiwott/Downloads/extracted_data.csv', index=False)

extract_data('/home/dbiwott/Downloads/tabithaaccountstatementrafiki-2.pdf')