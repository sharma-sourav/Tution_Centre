import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sourav",
  database="mydb"

)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS person  ( first_name CHAR(20) NOT NULL, last_name CHAR(20) NOT NULL,sex CHAR(10))")
mycursor.execute("INSERT  INTO person ( first_name,last_name, sex) VALUES( 'kakaa', 'baloatr','male')")
mydb.commit()
for tb in mycursor:
    print(tb)