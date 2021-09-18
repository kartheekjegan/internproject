import sqlite3
# creating and connecting to a database in sqlite3
conn= sqlite3.connect('C:\sqlite\Movieslist.db')
print("opened database successfully")

# creating a table movies
conn.execute('''CREATE TABLE Movies(
       movie_name varchar(255),
       actor varchar(255), 
       actress varchar(255),  
       director varchar(255),
       yearrofrelease int(10)
       );''')
print("Table Created Sucessfully")

# inserting data into the table movies
conn.execute("INSERT INTO Movies(movie_name,actor,actress,director,yearrofrelease)\
 VALUES('Titanic','Jack','rose','james',2002)")
conn.execute("INSERT INTO Movies(movie_name,actor,actress,director,yearrofrelease)\
 VALUES('Fight','Tony','Natasha','Jenifer',2004)")
conn.execute("INSERT INTO Movies(movie_name,actor,actress,director,yearrofrelease)\
 VALUES('TheStark','Harley','Scarlett','Nolan',2006)")
conn.execute("INSERT INTO Movies(movie_name,actor,actress,director,yearrofrelease)\
 VALUES('Friends','Cristiano','Katherine','Robert',2008)")
conn.execute("INSERT INTO Movies(movie_name,actor,actress,director,yearrofrelease)\
 VALUES('StreetClub','David','Dida','Cameron',2010)")
conn.commit()
print ("Records inserted successfully")

# querying data from table movies using select statement
cursor = conn.execute("SELECT movie_name,actor,actress,director,yearrofrelease from Movies")
for row in cursor:
   print ("movie_name = ", row[0])
   print ("actor = ", row[1])
   print ("actress = ", row[2])
   print ("director = ", row[3])
   print ("yearrofrelease =",row[4], "\n")

print ("Operation done successfully")
conn.close()