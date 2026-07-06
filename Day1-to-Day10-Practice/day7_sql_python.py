import sqlite3

# STEP 1: Database connect karo
conn = sqlite3.connect('day7.db')
print("Database ban gayi!")

# STEP 2: Cursor leke table banao
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS sales(id INTEGER PRIMARY KEY, product TEXT, amount INTEGER)")
print("Table ban gayi!")

# STEP 3: Purana data saaf karo + 10 row dalo
c.execute("DELETE FROM sales")

data = [
    (1, 'Laptop', 50000),
    (2, 'Mouse', 500),
    (3, 'Keyboard', 2000),
    (4, 'Monitor', 15000),
    (5, 'Printer', 8000),
    (6, 'Pendrive', 800),
    (7, 'Speaker', 3000),
    (8, 'Webcam', 2500),
    (9, 'Headphone', 1500),
    (10, 'Mousepad', 300)
]

c.executemany("INSERT INTO sales VALUES (?,?,?)", data)
conn.commit()
print("10 row add ho gaye!")

# STEP 4: Data nikal ke dikhao - SELECT
c.execute("SELECT * FROM sales")
rows = c.fetchall()

print("\n=== SAARA DATA ===")
for row in rows:
    print(row)

print("\n=== SIRF PRODUCT NAAM ===")
c.execute("SELECT product FROM sales")
rows = c.fetchall()
for row in rows:
    print(row[0])

print("\n=== 5000 SE MEHNGA ===")
c.execute("SELECT product, amount FROM sales WHERE amount > 5000")
rows = c.fetchall()
for row in rows:
    print(row)

# STEP 5: Connection band karo
conn.close()
print("\nKaam khatam!")
