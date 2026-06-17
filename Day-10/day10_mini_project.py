import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('superstore practice.xlsx',sheet_name='Sample - Superstore')
print(df.head())
print(df.info())

# Bar chart Category comparison :
plt.figure(figsize=(8,5))
ax=sns.barplot(x='Category',y='Sales', data=df, estimator=sum)
ax.set_title('Category wise Total Sales')

for p in ax.patches:
    height=p.get_height()
    ax.text(p.get_x()+p.get_width()/2, height,f'{int(height)}',ha='center',va='bottom')
plt.xticks(rotation=45)
plt.savefig('bar_chart.png',dpi=100,bbox_inches='tight')

# line chart

# Step 1: Date ko month me convert karo
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M').astype(str) # 2023-01 jaisa ban jayega

# Step 2: Har month ka total sales nikalo
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

# Step 3: Line graph banao
plt.figure(figsize=(10,5))
sns.lineplot(x='Month', y='Sales', data=monthly_sales, marker='o') # marker='o' se dot aa jayenge
plt.title('Month-wise Sales Trend')
plt.xticks(rotation=45)
plt.savefig('line_chart.png',dpi=100,bbox_inches='tight')

# scatter plot

plt.figure(figsize=(8,6))
df_sample=df.sample(1000)
plt.scatter(x=df_sample['Discount'], y=df_sample['Profit'], alpha=0.2, s=5)
plt.title('Discount vs Profit')
plt.savefig('scatter.png') # Graph image ban jayega
print("Graph save ho gaya: scatter.png")

