import numpy as np
import pandas as pd

# Create a DataFrame
l = [1,2,3,4,5,6]
h = pd.DataFrame(l)
print(type(h))

d  = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
      'Age': [28, 24, 35, 32],
      'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(d)
print(df)

list = [[1, 'John', 28, 'New York'],
        [2, 'Anna', 24, 'Paris'],
        [3, 'Peter', 35, 'Berlin'],
        [4, 'Linda', 32, 'London']]
df2 = pd.DataFrame(list, columns=['ID', 'Name', 'Age', 'City'])
print(df2)

s = { "ID":pd.Series([1, 2, 3, 4]),
      "Name":pd.Series(['John', 'Anna', 'Peter', 'Linda']),}
df3 = pd.DataFrame(s)
print(df3)