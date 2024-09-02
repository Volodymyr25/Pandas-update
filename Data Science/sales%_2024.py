import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('base.csv')

df_2024 = df[df['Year'] == 2024]

sales_summary_2024 = df_2024.groupby('Name')['Sales'].sum().reset_index()

plt.figure(figsize=(8, 8))
plt.pie(sales_summary_2024['Sales'], labels=sales_summary_2024['Name'], autopct='%1.1f%%', colors=['blue', 'orange', 'green'])
plt.title('Продажі за 2024 рік')
plt.savefig('sales%_2024.png')
plt.show()