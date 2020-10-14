import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="vidyasagar",
    passwd="mav12345",
    database="mydatabase"
)

cursor= db.cursor()
import datetime as datetime

 
# cursor.execute("CREATE TABLE Details (name VARCHAR(30),age smallint UNSIGNED , id int PRIMARY KEY AUTO_INCREMENT)")
print(db.is_connected())


cursor.execute("INSERT INTO Details (name,age) VALUES (%s,%s)",("vidya SAGAR",23))
db.commit()
cursor.execute("DESCRIBE Details")
for x in cursor:
    print(x)

cursor.execute("SELECT * FROM Details")
for x in cursor:
    print(x)



cursor.execute("CREATE TABLE deapthDetails (name VARCHAR(50) NOT NULL,age int UNSIGNED NOT NULL,gender ENUM('M','F','O') NOT NULL,id int PRIMARY KEY AUTO_INCREMENT)")
cursor.execute("DESCRIBE deapthDetails")
for x in cursor:
    print(x)


cursor.execute("INSERT INTO deapthDetails (name,age,gender) VALUES (%s,%s,%s)",("HUtch_kukka",18,"M"))
db.commit()


cursor.execute("SELECT name,id FROM deapthDetails WHERE id=4 ORDER by id ASC ")
for x in cursor:
    print(x)

# Edit the table
cursor.execute("ALTER TABLE deapthDetails ADD COLUMN date datetime NOT NULL")
cursor.execute("ALTER TABLE deapthDetails ADD COLUMN food VARCHAR(50) NOT NULL")
cursor.execute("DESCRIBE deapthDetails")
for x in cursor:
    print(x)

# drop the column
cursor.execute("ALTER TABLE deapthDetails DROP date")

# change the name of the column
cursor.execute("ALTER TABLE deapthDetails CHANGE name first_name VARCHAR(100)")

# show the tables
cursor.execute("show tables")
for x in cursor:
    print(x)

# combine the tables by foreign key
query1="CREATE TABLE userinfo (userid int PRIMARY KEY AUTO_INCREMENT NOT NULL,name VARCHAR(50) NOT NULL,age int DEFAULT 10)"
query2="CREATE TABLE userScoreinfo (id int PRIMARY KEY AUTO_INCREMENT,FOREIGN KEY(id) REFERENCES userinfo(userid),Scores int DEFAULT 0)"

cursor.execute(query1)
cursor.execute(query2)
cursor.execute("show tables")
for x in cursor:
    print(x)
cursor.execute("DESCRIBE userinfo")
for x in cursor:
    print(x)

userinfo_entries=[
    ("vidya",20),
    ("sagar",30),
    ("murali",20)
]
userScoreinfo_entries=[
    (2000,),
    (3000,),
    (5000,),
]



query3="INSERT INTO userinfo (name,age) VALUES (%s,%s)"
query4="INSERT INTO userScoreinfo (id,scores) VALUES (%s,%s)"

for x,userinfo in enumerate(userinfo_entries):
    cursor.execute(query3,userinfo)
    db.commit()
    lastid= cursor.lastrowid
    print(lastid)
    cursor.execute(query4,(lastid,)+userScoreinfo_entries[x])
    db.commit()
cursor.execute("SELECT * FROM userinfo")
for x in cursor:
    print(x)
cursor.execute("SELECT * FROM userScoreinfo")
for x in cursor:
    print(x)