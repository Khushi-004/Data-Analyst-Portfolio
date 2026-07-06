import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data load
df = pd.read_excel('superstore practice.xlsx', sheet_name='Sample - Superstore')

print("=== DAY 9 GRAPH CLASS START ===")

# 1. SCATTER PLOT - Sales vs Profit ka rishta aankh se dekho
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='Sales', y='Profit', alpha=0.5)
plt.title('Sales vs Profit ka Rishta')
plt.xlabel('Sales ₹')
plt.ylabel('Profit ₹')
plt.show()

# 2. HEATMAP - State vs Category me kaha bikta hai sabse zyada
pivot_table = df.pivot_table(values='Sales', index='State', columns='Category', aggfunc='sum')

plt.figure(figsize=(12,8))
sns.heatmap(pivot_table, annot=False, cmap='YlGnBu')
plt.title('State vs Category - Sales Heatmap')
plt.savefig('day9_scatter.png', dpi=300, bbox_inches='tight')
plt.savefig('day9_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()
