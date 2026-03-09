# pd.merge(df1, df2, on="column_name", how="type of join")

import pandas as pd 

# customer data frame
df_customers = pd.DataFrame({
    'customerid':[1,2,3],
    'name':["raamesh", "suresh", "kalpesh"]
})

# order datafrme
df_orders = pd.DataFrame({
    'customerid':[1,2,4],
    'orderamount':[250,450,350]
})

# merge
df_merged = pd.merge(df_customers, df_orders, on="customerid", how="inner")
print('inner join')
print(df_merged)


''''
4 methods
inner
outer 
left 
right
'''