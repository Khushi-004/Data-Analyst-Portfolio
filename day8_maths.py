import pandas as pd

# Superstore data load kar lete hain
df = pd.read_csv('Sample - Superstore.csv')

print("=== MATHS CLASS START ===")

# 1. MEAN - Average Sales kitna hai?
mean_sales = df['Sales'].mean()
print(f"Average Sales = {mean_sales:.2f}")

# 2. MEDIAN - Beech wala value
median_sales = df['Sales'].median()
print(f"Median Sales = {median_sales:.2f}")

# 3. STD DEV - Sales kitna up-down hota hai?
std_sales = df['Sales'].std()
print(f"Sales ka Up-Down = {std_sales:.2f}")

# 4. CORRELATION - Sales aur Profit ka rishta
corr = df['Sales'].corr(df['Profit'])
print(f"Sales vs Profit ka Rishta = {corr:.2f}")