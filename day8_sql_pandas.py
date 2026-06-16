import pandas as pd

# Excel khol
df = pd.read_excel('superstore practice.xlsx', sheet_name='Sample - Superstore')

print("=== DAY-8: PANDAS = SQL ===\n")

# SQL: SELECT * FROM table WHERE Sales > 1000
q1 = df[df['Sales'] > 1000]
print("1. Sales > 1000 wale orders:", len(q1))

# SQL: SELECT Category, SUM(Sales) FROM table GROUP BY Category
q2 = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\n2. Category wise total Sales:\n", q2)

# SQL: SELECT State, AVG(Profit) FROM table GROUP BY State ORDER BY AVG(Profit) DESC LIMIT 5
q3 = df.groupby('State')['Profit'].mean().sort_values(ascending=False).head(5)
print("\n3. Top 5 State jaha Profit sabse zyada:\n", q3)

# SQL: SELECT COUNT(DISTINCT Customer ID) FROM table
q4 = df['Customer ID'].nunique()
print("\n4. Total unique Customers:", q4)

# SQL: SELECT Region, AVG(Discount) FROM table GROUP BY Region
q5 = df.groupby('Region')['Discount'].mean()
print("\n5. Region wise average Discount:\n", q5)

# loss me chal rahe order konse h ?
loss_orders = df[df['Profit'] < 0].sort_values('Profit')
print("\n Top 10 Loss wale orders:\n", loss_orders[['Order ID', 'State', 'Sales', 'Profit']].head(10))

# Company k top 5 VIP customer kon se h ?
vip_customer = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 VIP Customers:\n", vip_customer)

# Konsa product category sabse zyada discount maang raha h ?
discount_vs_profit = df.groupby('Category')[['Discount', 'Profit']].mean()
print("\nCategory wise Discount vs Profit:\n", discount_vs_profit)

# konsa ship mode sabse slow h ?
ship_time = df.groupby('Ship Mode')['Profit'].mean().sort_values()
print("\nShip Mode wise avg delivery days:\n", ship_time)

# Konsi sate sabse bura perform krr rahi h ?
west_state = df[df['Region'] == 'West'].groupby('State')['Profit'].sum().sort_values().head(5)
print("\nWest Region ke Bottom 5 State:\n", west_state)