import pandas as pd

data = {
    "name": ["ram", "shyam", "sam", "krish", "yashdeep", "bhavishya"],
    "age": [12,2,41,354,334,34],
    "salary": [23000,34000,70000,340000,670000,56000],
    "performance score": [23,43,53,53,23,67]
}

df = pd.DataFrame(data)

high_salary = df[df["salary"] > 50000]
print("employes with salary > 50000")
print(high_salary)

# filtering rows salary > 50000 and age > 50

filtered = df[(df["age"] > 50) & (df["salary"] > 50000)]
print(f"employe list age > 50 + salary > 50000")
print(filtered)