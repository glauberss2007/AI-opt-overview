import pandas as pd

personal_data = pd.read_excel('../files/dados.xlsx', sheet_name='pessoas')
score_data = pd.read_excel('../files/dados.xlsx', sheet_name='notas')

print(personal_data)
print(score_data)

data_all = score_data.set_index('nome').join(personal_data.set_index('nome'))
print(data_all)

avg = data_all.groupby('nome').nota.mean()
print(avg)

avg.to_excel('../files/saida.xlsx')