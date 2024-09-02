import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('base.csv')
sales_summary = df.groupby('Name')['Sales'].sum().reset_index()

plt.figure(figsize=(8, 8))
plt.pie(sales_summary['Sales'], labels=sales_summary['Name'], autopct='%1.1f%%', colors=['blue', 'orange', 'green'])
plt.title('Продажі усіх телефонів')
plt.savefig('summary_sales.png')
plt.show()