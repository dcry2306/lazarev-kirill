import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
name = input('Введите путь к датасету: ')
df = pd.read_csv(name)

# Часть 1

# Задание 1

min_price = df['price'].min()
filtered_df = df[df['price'] == min_price]
min_bedrooms = filtered_df['bedrooms'].apply(lambda x: int(x))
print("Количество спален в самом дешёвом доме:", min_bedrooms.min())

# Задание 2

count_houses = len(df[(df['bedrooms'] <= df['bathrooms'])])
print("Количество домов, в которых количество спален не больше количества ванных:", count_houses)

# Задание 3

guestroom_homes = df[df['guestroom'] != '0']
min_price = guestroom_homes['price'].min()
print("Стоимость самого дешевого дома с гостевой комнатой:", min_price)

# Задание 4

filtered_homes = df[(df['price'] >= 2000000) & (df['price'] <= 5000000)]
aircon_homes = len(filtered_homes[filtered_homes['airconditioning'] == 'yes'])
print("Количество домов, с кондиционированием воздуха", aircon_homes)

# Часть 2

plt.figure(figsize=(8, 6))
plt.xlabel('Цена (Price)')
plt.ylabel('Площадь (Area)')
plt.title('График квартир по цене и площади с разным количеством парковочных мест')
parking_counts = df['parking'].unique()
colors = ['red', 'blue', 'orange', 'green'][:len(parking_counts)]
for count, color in zip(parking_counts, colors):
    filtered_data = df[df['parking'] == count]
    plt.scatter(filtered_data['price'], filtered_data['area'], c=color, alpha=0.5, label=f'{count} парковочных мест')
plt.legend()
plt.show()

# Часть 3

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.tight_layout(pad=5)

ax1 = axes[0, 0]
colors1 = ['red' if guestroom == 'yes' else 'blue' for guestroom in df['guestroom']]
ax1.scatter(df['price'], df['area'], c=colors1, alpha=0.5)
ax1.set_title('График 1: Наличие/отсутствие гостевой комнаты')
ax1.set_xlabel('Цена')
ax1.set_ylabel('Площадь')
ax1.legend(['Отсутствует', 'Присутствует'])
ax1.grid(True)

ax2 = axes[0, 1]
colors2 = ['red' if basement == 'yes' else 'blue' for basement in df['basement']]
ax2.scatter(df['price'], df['area'], c=colors2, alpha=0.5)
ax2.set_title('График 2: Наличие/отсутствие подвала')
ax2.set_xlabel('Цена')
ax2.set_ylabel('Площадь')
ax2.legend(['Отсутствует', 'Присутствует'])
ax2.grid(True)

ax3 = axes[1, 0]
colors3 = ['red' if hotwaterheating == 'yes' else 'blue' for hotwaterheating in df['hotwaterheating']]
ax3.scatter(df['price'], df['area'], c=colors3, alpha=0.5, label='Наличие гостевой комнаты')
ax3.set_title('График 3: Наличие/отсутствие отопления горячей водой')
ax3.set_xlabel('Цена')
ax3.set_ylabel('Площадь')
ax3.legend(['Отсутствует', 'Присутствует'])
ax3.grid(True)

ax4 = axes[1, 1]
colors4 = ['blue' if prefarea == 'yes' else 'red' for prefarea in df['prefarea']]
ax4.scatter(df['price'], df['area'], c=colors4, alpha=0.5)
ax4.set_title('График 4: Наличие/отсутствие предбанника')
ax4.set_xlabel('Цена')
ax4.set_ylabel('Площадь')
ax4.legend(['Отсутствует', 'Присутствует'])
ax4.grid(True)

plt.show()

# Часть 4

with_ac = df[df["airconditioning"] == "yes"]
without_ac = df[df["airconditioning"] == "no"]
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(with_ac["price"], bins=30, color='yellow', alpha=0.5, label="С кондиционированием")
ax.hist(without_ac["price"], bins=30, color='blue', alpha=0.5, label="Без кондиционирования")
ax.set_xlabel("Цена")
ax.set_ylabel("Частота")
ax.set_title("Распределение цены для домов с и без кондиционирования")
ax.legend()
plt.show()



