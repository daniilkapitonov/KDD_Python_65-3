import sqlite3 as sq
import time
from random import randint
conn = sq.connect(r"Lesson 4/fast.db")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS data(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    num1 INTEGER,
    num2 INTEGER,
    num3 INTEGER
    ); ''')

# start = time.time()
# r = set()
# for i in range(60000000):
#     n1 = randint(-20000000,20000000)
#     n2 = randint(-20000000,20000000)
#     n3 = randint(-20000000,20000000)
#     r.add(n1)
#     r.add(n2)
#     r.add(n3)
#     cur.execute('''INSERT INTO  data(num1,num2,num3) VALUES(?,?,?)''',
#                 (n1,n2,n3,))
# conn.commit()
# end = time.time()
# print("Time for add - ", end-start)
# print(r)

start = time.time()
sel = (cur.execute('''SELECT * from data WHERE num1 = 43532'''))

# for i in sel:
#     print(i)
end = time.time()
print("Time for search - ", end-start)
print(len(list(sel)))