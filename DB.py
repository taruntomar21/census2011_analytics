import mysql.connector
import pandas as pd

class DataBase:
    def __init__(self):

        try:
            self.conn = mysql.connector.connect(
                host="campusx.c5ck4o0m492k.ap-southeast-3.rds.amazonaws.com",
                user="admin",
                password="Tarunmysql55",
                database="campusx"
            )

            self.mycursor = self.conn.cursor()
            print("Connected to MySQL database successfully")

        except Exception as e:
            print("Error:", e)

    def fetch_row_data(self):
        self.mycursor.execute("""SELECT * FROM india""")
        data = self.mycursor.fetchall()
        df = pd.DataFrame(data)
        return df

    def fetch_states(self):
        States = []
        try:
            self.mycursor.execute("""SELECT DISTINCT(State) FROM india""")

            data = self.mycursor.fetchall()
            for i in data:
                States.append(i[0])
            return States
        except Exception as e:
            print("Error:", e)

    def fetch_all_states_summary(self):
        self.mycursor.execute("""
            SELECT State, 
                   SUM(Population) as Population,
                   ROUND(AVG(litracy_rate), 2) as Literacy_Rate,
                   AVG(Latitude) as Latitude,
                   AVG(Longitude) as Longitude
            FROM india
            GROUP BY State
        """)
        result_df = self.mycursor.fetchall()
        df = pd.DataFrame(result_df, columns=['State', 'Population', 'Literacy_Rate', 'Latitude', 'Longitude'])
        return df

    def fetch_population(self,state):
        pop = []
        self.mycursor.execute("""WITH pop AS (SELECT State,SUM(Population) AS "population" FROM india
                                                GROUP BY State)
                                SELECT population from pop
                                WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            pop.append(i[0])
        return pop[0]

    def fetch_district(self,state):
        dis = []
        self.mycursor.execute(""" SELECT DISTINCT(District) FROM india
                                    WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            dis.append(i[0])
        return len(dis)

    def fetch_litracy(self,state):
        lit = []
        self.mycursor.execute(""" WITH lit AS (SELECT State, AVG(litracy_rate) AS "litracy_rate" FROM india
                                                GROUP BY State)
                                SELECT ROUND(litracy_rate,2) FROM lit
                                WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            lit.append(i[0])
        return lit[0]

    def fetch_data(self,column,state):
        query = f"SELECT SUM({column}) FROM india WHERE State = %s"
        self.mycursor.execute(query, (state,))
        result = self.mycursor.fetchone()
        return result[0] if result else 0


    # ----------------------------------------------------------------------

    def fetch_districts(self,state):
        dist = []
        try:
            self.mycursor.execute("""SELECT DISTINCT(District) FROM india
                                        WHERE State = '{state}'""".format(state=state))

            data = self.mycursor.fetchall()
            for i in data:
                dist.append(i[0])
            return dist
        except Exception as e:
            print("Error:", e)


    def fetch_dist_data(self,column,district):
        query = f"SELECT {column} FROM india WHERE District = '{district}'"
        self.mycursor.execute(query)
        result = self.mycursor.fetchone()
        return result[0] if result else 0

    def fetch_lat_long(self, state):
        rows = self.mycursor.execute("SELECT District, Latitude, Longitude FROM india WHERE State = %s",(state,))
        rows = self.mycursor.fetchall()
        df = pd.DataFrame(rows, columns=['District', 'Latitude', 'Longitude'])
        return df