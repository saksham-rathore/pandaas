import pandas as pd

data = {
    "name": ['arun', 'varun', 'karan'],
    "age": [23,56,21],
    "salary":[10000,20000,30000]
}

df = pd.DataFrame(data)
df.sort_values(by=["age", "salary"], ascending=[True, False], inplace=True)
print('sorted age by descending')
print(df)