''''
vertically (row-wise)
horizontally (column wise)

pd.concate([df1, df2], axis=0, ignore_index=true)
[df1, df2] = 
axis = 1
ignore_index = True
'''

# vertically
import pandas as pd 

# region1
df_region1 = pd.DataFrame({
    "customerid":[1,2],
    "name":["sam","simran"]
})
# region2
df_region2 = pd.DataFrame({
    "customerid":[3,4],
    "name":["dipali", "mohini"]
})

# concatenate vertically
df_concat = pd.concat([df_region1, df_region2], axis=1, ignore_index=True)
print(df_concat)