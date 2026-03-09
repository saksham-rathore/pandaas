import pandas as pd

data = {
    "name": ["ram", "shyam", "sam", "krish", "yashdeep", "bhavishya"],
    "age": [12,2,41,354,334,34],
    "salary": [23000,34000,70000,340000,670000,56000],
    "performance score": [23,43,53,53,23,67]
}

df = pd.DataFrame(data)

print('sample dataframe')
print(df)
print('name (single column return series)')
name = df["name"]
print(name)

# selecting multiple columns
subset = df[["name", "salary"]]
print('\nsubset with name and salary')
print(subset)