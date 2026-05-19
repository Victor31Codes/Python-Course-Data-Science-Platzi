import pandas as pd
import numpy as np

df1 = pd.DataFrame({
  'key': ['A', 'B', 'C'],
  'value1': [1,2,3]
})

df2 = pd.DataFrame({
  'key': ['B', 'C', 'D'],
  'value2': [4,5,6]
})

print(df1)
print(df2)

inner_merged = pd.merge(df1,df2, on = 'key', how = 'inner') #What it does? Check on the key list which values are in common and base on that it merge the values, basically it works like an intersection
print(inner_merged)

outer_merged = pd.merge(df1,df2, on = 'key', how = 'outer') #What it does? Check on the key list which values are in common and base on that it merge the values but the outer  basically it works like an union
print(outer_merged)

left_merged = pd.merge(df1, df2, on = 'key', how = 'left') #The same as the previous ones, the only thing is that it merged based on the left value
print(left_merged)

right_merged = pd.merge(df1, df2, on = 'key', how = 'right')#The same as the previous ones, the only thing is that it merged based on the right value
print(right_merged)


df3 = pd.DataFrame({
  'A': ['A0', 'A1', 'A2'],
  'B': ['B0', 'B1', 'B2'],
})

df4 = pd.DataFrame({
  'A': ['A3', 'A4', 'A5'],
  'B': ['B3', 'B4', 'B5'],
}) 

vertical_concat = pd.concat(df1,df2)
horizontal_concat = pd.concat(df1,df2, axis=1)

joined = df3.join(df4, how='inner')