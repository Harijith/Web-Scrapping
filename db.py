import sqlite3
name="John"
salary=9000
conn=sqlite3.connect("word_density.db")
print("Connecting to DB...")
#conn.execute('''CREATE TABLE DATA_2(NAME TEXT, SALARY FLOAT);''')
conn.commit()
c=conn.cursor()
#c.execute('''INSERT INTO DATA_2(NAME,SALARY) VALUES(?,?)''',(name,salary))
x=c.execute('''SELECT * FROM DATA_2''')
for i in x:
    print(i)
#conn.commit()
print("\n Data entered successfully")
conn.close()

                    
