import pandas as pd 

#read data from csv file into a dataframe
df = pd.read_csv("D:\learn pandas\datasets\Loan_approval_data_2025.csv")

print("display 10 rowd of first")
print(df.head(20))

print("display 10 rows of last")
print(df.tail(20))

''''
head is use to show starting rows 
and tail basically use ending rows 
'''
