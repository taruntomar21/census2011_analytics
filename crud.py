import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Tarun@sqlserver@55",
        port=3306,
        database="campusx"
    )

    mycursor = conn.cursor()
    print("Connected to MySQL database successfully")

except Exception as e:
    print("Error:", e)

# I already have dataset in csv, this following section is only for understanding basic and experiments.

# create a database on db server -------------------------------

# mycursor.execute("CREATE DATABASE mydb")
# conn.commit()

# create a table ------------------------------------

# mycursor.execute("""
# CREATE TABLE airport(
#     air_id INTEGER PRIMARY KEY,
#     code VARCHAR(10) NOT NULL,
#     city VARCHAR(100) NOT NULL,
#     name VARCHAR(255) NOT NULL
# )
# """)
conn.commit()

# Insert data to the table ---------------------

# mycursor.execute("""
#     INSERT INTO airport VALUES
#     (1,'DEL','New Delhi','IGIA'),
#     (2,'CCU','Kolkata','NSCA'),
#     (3,'BOM','Mumbai','CSMA')
# """)
conn.commit()

# search/retrieve ---------------------------

pop = []
mycursor.execute("""WITH lit AS (SELECT State, SUM(Male) AS "male" FROM census
                                GROUP BY State)
                    SELECT male FROM lit
                    WHERE State = "Kerala"
""")
data = mycursor.fetchall()
print(data)

for i in data:
    pop.append(i[0])

print(pop[0])


