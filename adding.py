import pandas as pd

data = {
    "name": ["ram", "shyam", "sam", "krish", "yashdeep", "bhavishya"],
    "age": [12,2,41,354,334,34],
    "salary": [23000,34000,70000,340000,670000,56000],
    "performance score": [23,43,53,53,23,67]
}

df = pd.DataFrame(data)
print(df)
# square brackets df["column name"] = some data 

df["bonus"] = df['salary'] * 0.1
print(df)

# using insert()
# df.insert(loc, "column_name", some_data)
df.insert(0, "employe id", [10,20,30,40,50,60])
print(df)