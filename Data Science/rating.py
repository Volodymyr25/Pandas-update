import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('base.csv')

plt.figure(figsize=(10, 6))

for name in df['Name'].unique():
    subset = df[df['Name'] == name]
    plt.plot(subset['Year'], subset['Rating'], marker='o', label=name)

plt.title('Рейтинг телефонів за роками')
plt.xlabel('Рік')
plt.ylabel('Рейтинг')
plt.legend(title='Марка телефону')
plt.grid(True)
plt.savefig('rating.png')
plt.show()