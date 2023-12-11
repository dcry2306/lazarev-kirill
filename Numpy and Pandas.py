import pandas as pd
import numpy as np
data = {
'Имя': ['Иван', 'Мария', 'Олег', 'Антон', 'Максим', 'Кирилл' ],
'Класс': ['10A', '10A', '10Б', '10В', '10Б', '10A' ],
'Оценка': ['4', '4', '5', '3', '5', '5']
}
df = pd.DataFrame(data)
print('Первые 3 строки:\n', df.head(3))
print('Последние 3 строки:\n', df.tail(3))
df.to_csv('data.csv', index=False)