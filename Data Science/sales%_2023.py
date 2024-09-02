import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('base.csv')

df_2023 = df[df['Year'] == 2023]

sales_summary_2023 = df_2023.groupby('Name')['Sales'].sum().reset_index()

plt.figure(figsize=(8, 8))
plt.pie(sales_summary_2023['Sales'], labels=sales_summary_2023['Name'], autopct='%1.1f%%', colors=['blue', 'orange', 'green'])
plt.title('Продажі за 2023 рік')
plt.savefig('sales%_2023.png')
plt.show()