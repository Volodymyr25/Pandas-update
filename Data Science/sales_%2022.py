import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("base.csv")

df_2022 = df[df['Year'] == 2022]

sales_summary_2022 = df_2022.groupby('Name')['Sales'].sum().reset_index()

plt.figure(figsize=(8, 8))
plt.pie(sales_summary_2022['Sales'], labels=sales_summary_2022['Name'], autopct='%1.1f%%', colors=['blue', 'orange', 'green'])
plt.title('Продажі за 2022 рік')
plt.savefig('sales%_2022.png')
plt.show()