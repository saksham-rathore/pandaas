import pandas as pd

data = {
    "name": ["ram", "shyam", "krish", "sam"],
    "age": [132, 2341, 241, 30],
    "city": ["nagpur", "mumbai", "delhi", "pune"]
}

df = pd.DataFrame(data)
print(df)

# save file in csv format
# and remove index numbers
df.to_csv("output.csv", index=False)  

# save file in excel format
df.to_excel("output.xlsx", index=False)

# save file in excel format
df.to_json("output.json", index=False)
