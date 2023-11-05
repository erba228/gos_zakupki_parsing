import pandas as pd

df = pd.read_excel('tenders.xlsx')

df[0] = df[0].astype(str).str.replace('NUMBER', '')
df[1] = df[1].astype(str).str.replace('NAME OF COMPANY', '')
df[2] = df[2].astype(str).str.replace('TYPE OF PROCUREMENT', '')
df[2] = df[2].astype(str).str.replace('Goods', 'Товары')
df[2] = df[2].astype(str).str.replace('work', 'Работа')
df[2] = df[2].astype(str).str.replace('services', 'Услуги')
df[3] = df[3].astype(str).str.replace('PURCHASE NAME', '')
df[5] = df[5].astype(str).str.replace('PROCUREMENT METHOD', '')
df[5] = df[5].astype(str).str.replace('One stage', 'Неограниченный')
df[5] = df[5].astype(str).str.replace('Simplified', 'Простой')
df[6] = df[6].astype(str).str.replace('PLANNED AMOUNT', '')
df[7] = df[7].astype(str).str.replace('DATE PUBLISHED', '')
df[8] = df[8].astype(str).str.replace('BIDS SUBMISSION DEADLINE', '')


df[0] = df[0].astype(str).str.replace('\n', '')
df[1] = df[1].astype(str).str.replace('\n', '')
df[2] = df[2].astype(str).str.replace('\n', '')
df[2] = df[2].astype(str).str.replace('Goods', 'Товары')
df[2] = df[2].astype(str).str.replace('work', 'Работа')
df[2] = df[2].astype(str).str.replace('services', 'Услуги')
df[3] = df[3].astype(str).str.replace('\n', '')
df.drop(df.columns[4], axis=1, inplace=True)
df[5] = df[5].astype(str).str.replace('\n', '')
df[5] = df[5].astype(str).str.replace('One stage', 'Неограниченный')
df[5] = df[5].astype(str).str.replace('Simplified', 'Простой')
df[6] = df[6].astype(str).str.replace('\n', '')
df[7] = df[7].astype(str).str.replace('\n', '')
df[8] = df[8].astype(str).str.replace('\n', '')

df.to_excel('tenders_updated.xlsx', index=False)
print("Обновленные данные сохранены в файл 'tenders_updated.xlsx'")