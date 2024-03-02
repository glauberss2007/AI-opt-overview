import pandas as pd
import copy

## dataframe
table = pd.DataFrame({'name': ['rafael','jose','pedro'], 'age': [21,22,23]})
print(table)
print(table.name[2])
print(table.loc[2,'age'])
print(table.age[table.name=='pedro'])

## Copy using pointers
table2 = table

## Copy without use pointers
table3 = copy.deepcopy(table)
