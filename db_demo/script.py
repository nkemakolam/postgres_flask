DB_HOST = "localhost"
BD_NAME = "prestashop"
BD_USER = "postgres"
BD_PASS = "ghosts"

import psycopg2
import psycopg2.extras


conn = psycopg2.connect(dbname=BD_NAME,user=BD_USER, password=BD_PASS,host=DB_HOST)
#opening connection 
#cur = conn.cursor()
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) # this help to get data with indexing from database

#cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY,name VARCHAR)")
# inserting into the table
# cur.execute("INSERT INTO student (name) VALUES(%s)",("jasper",))

# Fetch all from the database
# cur.execute("SELECT * FROM student;")
# print(cur.fetchall())

# fetching one record from the database 
cur.execute("SELECT * FROM student WHERE id = %s;", (1,))
print(cur.fetchone()["name"])
conn.commit()
cur.close()
conn.close()