import pandas as pd
import numpy as np
name = input('Укажите путь в файлу: ')
df = pd.read_csv(name)
df.head()
conditions1 = df[(df['Age'] > 30) & (df['Income'] < 30000)]
conditions2 = df[(df['Profession'] == 'Lawyer') & (df['Work Experience'] > 5)]
print(conditions1)
print(conditions2)
