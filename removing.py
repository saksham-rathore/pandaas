import pandas as pd 

data = {
    "name": ["ram", "shyam", "sam", "krish", "yashdeep", "bhavishya"],
    "age": [12,2,41,354,334,34],
    "salary": [23000,34000,70000,340000,670000,56000],
    "performance_score": [23,43,53,53,23,67]
}

df = pd.DataFrame(data)
print(df)

# df.drop(columns = ["column name"], inplace=true)
print('modified data')
df.drop(columns=["performance_score"], inplace=True)
print(df)