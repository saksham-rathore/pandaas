import pandas as pd

data = {
    "name": ['arun', 'varun', 'karan', 'sam', 'yash', 'krish'],
    "age": [24,56,21,24,42,21],
    "salary":[10000,20000,30000,40000,20000,70000]
}

df = pd.DataFrame(data)
grouped = df.groupby("age")["salary"].sum()
print(grouped)