import sqlite3 as sq
conn = sq.connect(r"Lesson 4/stud.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS watermelons(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    weight REAL,
    name TEXT,
    seed_count INTEGER
    );''')

cur.execute('''CREATE TABLE IF NOT EXISTS apples(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    weight REAL,
    name TEXT,
    seed_count INTEGER
    );''')

# cur.execute('''INSERT INTO watermelons(weight, name,
#     seed_count) VALUES(12.1,'Сочный сладкий ВАХ', 43)''')
# conn.commit()

# cur.execute('''UPDATE watermelons SET name="Много семак"
#     WHERE seed_count > 50; ''')
# conn.commit()

# cur.execute('''DELETE FROM watermelons WHERE 
#     name = 'Сочный сладкий ВАХ'; ''')
# conn.commit()
mass = [(10.1,'Синий',23),(2.1, "Red", 100)]
cur.executemany('''INSERT INTO watermelons(weight, name,
    seed_count) VALUES(?,?,?)''',mass)
conn.commit()
sel = (cur.execute('''SELECT * from watermelons '''))

for i in sel:
    print(i)

print()
sel = (cur.execute('''SELECT * from watermelons
    WHERE seed_count > 10 and seed_count <30'''))

for i in sel:
    print(i)