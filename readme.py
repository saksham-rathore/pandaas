import pandas as pd 

#read data from csv file into a dataframe
df = pd.read_csv("datasets/Loan_approval_data_2025.csv")

print(df)
 

''''
show error while reading a files so you can use encoding="latin1" 
or "utf-8"

read google cloud data so you can use a library in "gcsfs"
'''