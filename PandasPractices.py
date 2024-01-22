import pandas as pd

# Create a DataFrame from a list of lists

sub_list = ['01-Jan-2017', 'Cash Withdrawal', '1000.00', '5000.00'],
columns = ['Date', 'Description', 'Debit', 'Credit']

# df = pd.DataFrame(sub_list, columns=columns)

 # my_series = pd.Series(sub_list,index = ['A','B','C','D'])
list_s = ['01-Jan-2017', 'Cash Withdrawal', '1000.00', '5000.00']
list_index=['Date', 'Description', 'Debit', 'Credit']
series_4 = pd.Series(list_s, index =list_index)
print(series_4)
print(len(list_s)==len(list_index))

#Dataframe
list_s = [['01-Jan-2017', 'Cash Withdrawal', '1000.00', '5000.00'],
          ['01-Jan-2017', 'Cash Withdrawal', '1000.00', '5000.00'],
          ['01-Jan-2017', 'Cash Withdrawal', '1000.00', '5000.00']]


df= pd.DataFrame(list_s, columns = ['Date', 'Description', 'Debit', 'Credit'])
print(df)
print("************************************************************************************************")
#Read CSV file
bk_csv= pd.read_csv('/home/dbiwott/Documents/From PC/daily-bike-share.csv')


dirty_csv= pd.read_csv('/home/dbiwott/Downloads/dirtydata.csv')
print(dirty_csv)
