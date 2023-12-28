
import pandas as pd
import numpy as np
name = input('Укажите путь в файлу: ')
df = pd.read_csv(name)
print('Проверка на пропуски\n', df.isnull().any())
df.fillna(0, inplace=True)
result = df.groupby('Profession').agg({'Income':'mean'})           
print('Группировка по профессии, средний годовой доход\n',result)
