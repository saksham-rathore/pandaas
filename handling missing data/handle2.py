'''''
fillna()
fillna(value, inplace=True)
'''
import pandas as pd

data = {
    "name": ["ram", None, "sam", "krish", "yashdeep", "bhavishya"],
    "age": [12,None,41,354,334,34],
    "salary": [23000,34000,70000,340000,670000,56000],
    "performance score": [23,43,53,53,23,67]
}

df = pd.DataFrame(data)
print(df)

df.fillna(0, inplace=True)
print(df)