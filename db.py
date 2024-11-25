import csv
import sqlite3

con = sqlite3.connect("laila.db")
cursor = con.cursor()

#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
#cursor.execute(query)
#con.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
#cursor.execute(query)
#con.commit()

#Create a table with the desired columns
#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

#desired_columns_indices = [0, 30]
#
# #Read data from CSV and insert into SQLite table for the desired columns
#with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#    csvreader = csv.reader(csvfile)
#    for row in csvreader:
#        selected_data = [row[i] for i in desired_columns_indices]
#        cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))
## Commit changes and close connection
#con.commit()
#con.close()

query = "INSERT INTO contacts VALUES (null,'Appu', '7892270063', 'null')"
cursor.execute(query)
con.commit()

query = "INSERT INTO contacts VALUES (null,'Mahi', '8792000959', 'null')"
cursor.execute(query)
con.commit()

query = "INSERT INTO contacts VALUES (null,'Anna', '8095800098', 'null')"
cursor.execute(query)
con.commit()

query = "INSERT INTO contacts VALUES (null,'Amma', '8453330685', 'null')"
cursor.execute(query)
con.commit()

query = "INSERT INTO contacts VALUES (null,'Boss', '8453323174', 'null')"
cursor.execute(query)
con.commit()

query = "INSERT INTO contacts VALUES (null,'Harish', '7337805677', 'null')"
cursor.execute(query)
con.commit()

query = "INSERT INTO contacts VALUES (null,'Rani Akka', '7349305040', 'null')"
cursor.execute(query)
con.commit()

query = "INSERT INTO contacts VALUES (null,'Aishu Sweden', '+46 760999076', 'null')"
cursor.execute(query)
con.commit()



#Searhing a contact
#query = 'Mahi'
#query = query.strip().lower()
#cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
#results = cursor.fetchall()
#print(results[0][0])