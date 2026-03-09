import pandas as pd

data = {
    "name": ["ram", "shyam", "sam", "krish", "yashdeep", "bhavishya"],
    "age": [12,2,None,354,334,34],
    "salary": [23000,34000,70000,340000,670000,56000],
    "performance score": [23,43,53,53,23,67]
}

df = pd.DataFrame(data)
print(df)
''''
methods to learn is important 
linear,polynomial,time 
'''
df.interpolate(method="linear", axix=0, inplace=True)
