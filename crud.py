import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Tarun@sqlserver@55",
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

# pop = []
# mycursor.execute(f"SELECT SUM(Male_Workers) FROM census WHERE State = %s", (State,))
# result = mycursor.fetchone()
# print(result)


def fetch_let_long(state):
    query = f"SELECT Latitude, Longitude FROM india WHERE State = %s"
    mycursor.execute(query, (state,))
    result = mycursor.fetchall()
    print(result)


fetch_let_long("Goa")

# for i in data:
#     pop.append(i[0])
#
# print(pop[0])


