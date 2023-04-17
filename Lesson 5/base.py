import sqlite3 as sq
conn = sq.connect(r"Lesson 5/bazar.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS watermelons(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    weight REAL,
    name TEXT UNIQUE,
    seed_count INTEGER,
    sel_id INTEGER NOT_NULL,
    FOREIGN KEY (sel_id) REFERENCES seller (id)
    );''')

cur.execute('''CREATE TABLE IF NOT EXISTS seller(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT UNIQUE,
    IP_id INTEGER,
    score REAL
    );''')

cur.execute('''INSERT OR IGNORE INTO watermelons(weight, name,
    seed_count, sel_id) VALUES(12.1,'Сочный сладкий ВАХ', 2,1)''')
cur.execute('''INSERT OR IGNORE INTO watermelons(weight, name,
    seed_count, sel_id) VALUES(8.4,'Без семок, отвечаю', 4,2)''')
cur.execute('''INSERT OR IGNORE INTO watermelons(weight, name,
    seed_count, sel_id) VALUES(4.5,'На один разок', 1,1)''')
cur.execute('''INSERT OR IGNORE INTO watermelons(weight, name,
    seed_count, sel_id) VALUES(?,?,?,?)''',(16.8,'Попробуй утащи', 7,3,))
cur.execute('''INSERT OR IGNORE INTO watermelons(weight, name,
    seed_count, sel_id) VALUES(?,?,?,?)''',(4.7,'Нормас', 6,3,))
cur.execute('''INSERT OR IGNORE INTO watermelons(weight, name,
    seed_count, sel_id) VALUES(?,?,?,?)''',(5.6,'Пятачок', 8,2,))
cur.execute('''INSERT OR IGNORE INTO watermelons(weight, name,
    seed_count, sel_id) VALUES(?,?,?,?)''',(2.4,'На вынос', 5,1,))
conn.commit()

cur.execute('''INSERT OR IGNORE INTO seller(name,
    IP_id, score) VALUES(?,?,?)''',('Ashot',0, 3,))
cur.execute('''INSERT OR IGNORE INTO seller(name,
    IP_id, score) VALUES(?,?,?)''',('Mashot',0, 4,))
cur.execute('''INSERT OR IGNORE INTO seller(name,
    IP_id, score) VALUES(?,?,?)''',('Tashot',0, 1,))
conn.commit()

# cur.execute('''UPDATE watermelons SET weight = 0 WHERE seed_count = 43; ''')
# conn.commit()

# cur.execute('''DELETE FROM watermelons WHERE name = 'На один разок' ''')
# conn.commit()

sel = cur.execute('''SELECT * from watermelons ''')

for i in sel:
    print(i)
print()
sel = cur.execute('''SELECT * from seller ''')

for i in sel:
    print(i)
print('res')

sel = cur.execute('''SELECT watermelons.name,seller.name, max(watermelons.weight)  FROM watermelons INNER JOIN seller 
                WHERE watermelons.sel_id = seller.id and seller.name = (SELECT seller.name FROM seller) ''')

# sel = cur.execute('''SELECT watermelons.name,seller.name FROM watermelons INNER JOIN seller 
#                     WHERE watermelons.sel_id = seller.id and seller.name = 'Ashot' ''')

for i in sel:
    print(i)