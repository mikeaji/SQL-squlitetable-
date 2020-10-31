import sqlite3

#the structure of details being added to the database so like the list (deets) format 
db = sqlite3.connect("contacts.sqlite")   #connecting to the database
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 645435, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@email.com')")


cursor = db.cursor()  #a cursor is a generator, 
cursor.execute("SELECT * FROM contacts")
for name, phone, email in cursor:
    #print(row)
    print(name)
    print(email)
    print(phone)
    print("_" * 20)

cursor.close()    
db.close()  


