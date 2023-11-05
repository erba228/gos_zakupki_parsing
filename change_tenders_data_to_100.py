import pandas as pd

df = pd.read_excel('tenders_updated.xlsx')

df.drop(df.columns[-1], axis=1, inplace=True) 
df.drop(df.columns[-1], axis=1, inplace=True) 

df.columns = ['№', 'НАИМЕНОВАНИЕ ОРГАНИЗАЦИИ', 'ВИД ЗАКУПОК', 'НАИМЕНОВАНИЕ ЗАКУПКИ', 'МЕТОД ЗАКУПОК', 'ПЛАНИРУЕМАЯ СУММА', 'ДАТА ОПУБЛИКОВАНИЯ', 'СРОК ПОДАЧИ ПРЕДЛОЖЕНИЙ']

df['НАИМЕНОВАНИЕ ОРГАНИЗАЦИИ'] = df['НАИМЕНОВАНИЕ ОРГАНИЗАЦИИ'].astype(str)
df['ВИД ЗАКУПОК'] = df['ВИД ЗАКУПОК'].map(lambda x: x.replace(',', '')).astype(str)
df['НАИМЕНОВАНИЕ ЗАКУПКИ'] = df['НАИМЕНОВАНИЕ ЗАКУПКИ'].map(lambda x: x.replace(',', '')).astype(str)
df['МЕТОД ЗАКУПОК'] = df['МЕТОД ЗАКУПОК'].map(lambda x: x.replace(',', '')).astype(str)
df['ПЛАНИРУЕМАЯ СУММА'] = df['ПЛАНИРУЕМАЯ СУММА'].str.replace(',', '').astype(float)
df['ДАТА ОПУБЛИКОВАНИЯ'] = df['ДАТА ОПУБЛИКОВАНИЯ'].map(lambda x: x).astype(str).str.split().str[0]
df['СРОК ПОДАЧИ ПРЕДЛОЖЕНИЙ'] = df['СРОК ПОДАЧИ ПРЕДЛОЖЕНИЙ'].map(lambda x: x).astype(str).str.split().str[0]

df['ДАТА ОПУБЛИКОВАНИЯ'] = pd.to_datetime(df['ДАТА ОПУБЛИКОВАНИЯ'], format='%d.%m.%Y')
df['СРОК ПОДАЧИ ПРЕДЛОЖЕНИЙ'] = pd.to_datetime(df['СРОК ПОДАЧИ ПРЕДЛОЖЕНИЙ'], format='%d.%m.%Y')

filtered_df = df[df['ПЛАНИРУЕМАЯ СУММА'] > 5000000].head(100)

filtered_df.to_excel('tenders_updated_to_100.xlsx', index=False)
