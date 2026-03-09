import pandas as pd 

#read data from csv file into a dataframe
df = pd.read_csv("datasets/Loan_approval_data_2025.csv")


print("display the info of data set")
print(df.info())
 