import sqlite3
def sql():
    cur.execute("SELECT * FROM users;")
    one_result = cur.fetchone()
    print(one_result)
    cur.execute("SELECT * FROM users;")
    four_results = cur.fetchmany(4)
    print(four_results)
