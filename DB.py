import mysql.connector

class DataBase:
    def __init__(self):
        self.conn = None
        self.mycursor = None

        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="Tarun@sqlserver@55",
                port=3306,
                database="campusx"
            )

            self.mycursor = self.conn.cursor()
            print("Connected to MySQL database successfully")

        except Exception as e:
            print("Error:", e)

    def fetch_states(self):
        States = []
        try:
            self.mycursor.execute("""SELECT DISTINCT(State) FROM census""")

            data = self.mycursor.fetchall()
            for i in data:
                States.append(i[0])
            return States
        except Exception as e:
            print("Error:", e)

    def fetch_population(self,state):
        pop = []
        self.mycursor.execute("""WITH pop AS (SELECT State,SUM(Population) AS "population" FROM census
                                                GROUP BY State)
                                SELECT population from pop
                                WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            pop.append(i[0])
        return pop[0]

    def fetch_district(self,state):
        dis = []
        self.mycursor.execute(""" SELECT DISTINCT(District) FROM census
                                    WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            dis.append(i[0])
        return len(dis)

    def fetch_litracy(self,state):
        lit = []
        self.mycursor.execute(""" WITH lit AS (SELECT State, AVG(litracy_rate) AS "litracy_rate" FROM census
                                                GROUP BY State)
                                SELECT ROUND(litracy_rate,2) FROM lit
                                WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            lit.append(i[0])
        return lit[0]

    def fetch_male(self,state):
        lit = []
        self.mycursor.execute(""" WITH lit1 AS (SELECT State, SUM(Male) AS "male" FROM census
                                                GROUP BY State)
                                SELECT male FROM lit1
                                WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            lit.append(i[0])
        return lit[0]

    def fetch_female(self,state):
        lit = []
        self.mycursor.execute(""" WITH lit2 AS (SELECT State, SUM(Female) AS "female" FROM census
                                                GROUP BY State)
                                SELECT female FROM lit2
                                WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            lit.append(i[0])
        return lit[0]

    def fetch_hindu(self,state):
        lit = []
        self.mycursor.execute(""" WITH lit3 AS (SELECT State, SUM(Hindus) AS "hindu" FROM census
                                                GROUP BY State)
                                SELECT hindu FROM lit3
                                WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            lit.append(i[0])
        return lit[0]

    def fetch_muslim(self,state):
        lit = []
        self.mycursor.execute(""" WITH lit4 AS (SELECT State, SUM(Muslims) AS "muslims" FROM census
                                                GROUP BY State)
                                SELECT muslims FROM lit4
                                WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            lit.append(i[0])
        return lit[0]

    def fetch_Christians(self,state):
        lit = []
        self.mycursor.execute(""" WITH lit5 AS (SELECT State, SUM(Christians) AS "Christians" FROM census
                                                GROUP BY State)
                                SELECT Christians FROM lit5
                                WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            lit.append(i[0])
        return lit[0]

    def fetch_sikhs(self, state):
        lit = []
        self.mycursor.execute(""" WITH lit6 AS (SELECT State, SUM(Sikhs) AS "sikhs" FROM census
                                                   GROUP BY State)
                                   SELECT sikhs FROM lit6
                                   WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            lit.append(i[0])
        return lit[0]

    def fetch_Buddhists(self, state):
        lit = []
        self.mycursor.execute(""" WITH lit7 AS (SELECT State, SUM(Buddhists) AS "Buddhists" FROM census
                                                   GROUP BY State)
                                   SELECT Buddhists FROM lit7
                                   WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            lit.append(i[0])
        return lit[0]

    def fetch_jains(self, state):
        lit = []
        self.mycursor.execute(""" WITH lit8 AS (SELECT State, SUM(Jains) AS "jains" FROM census
                                                   GROUP BY State)
                                   SELECT jains FROM lit8
                                   WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            lit.append(i[0])
        return lit[0]

    def fetch_other_religion(self, state):
        lit = []
        self.mycursor.execute(""" WITH lit9 AS (SELECT State, SUM(Others_Religions) AS "Others_Religions" FROM census
                                                   GROUP BY State)
                                   SELECT Others_Religions FROM lit9
                                   WHERE State = '{State}'""".format(State=state))
        data = self.mycursor.fetchall()
        for i in data:
            lit.append(i[0])
        return lit[0]

    # ----------------------------------------------------------------------

    def fetch_districts(self,state):
        dist = []
        try:
            self.mycursor.execute("""SELECT DISTINCT(District) FROM census
                                        WHERE State = '{state}'""".format(state=state))

            data = self.mycursor.fetchall()
            for i in data:
                dist.append(i[0])
            return dist
        except Exception as e:
            print("Error:", e)



    # def fetch_data(self, source, destination):
    #     self.mycursor.execute("""SELECT Airline,Route,Dep_Time, Duration, Price FROM flight
    #                             WHERE Source = '{Source}' AND Destination = '{Destination}'
    #     """.format(Source=source, Destination=destination))
    #
    #     data = self.mycursor.fetchall()
    #     return data
    #
    # def fetch_airlines_frequency(self):
    #     airlines = []
    #     frequency = []
    #     try:
    #         self.mycursor.execute("""SELECT Airline, COUNT(*) FROM flight
    #                                  GROUP BY Airline
    #         """)
    #         data = self.mycursor.fetchall()
    #
    #         for i in data:
    #             airlines.append(i[0])
    #             frequency.append(i[1])
    #
    #         return airlines, frequency
    #     except Exception as e:
    #         print("Error:", e)
    #
    # def busy_airports(self):
    #     cities = []
    #     frequency = []
    #     try:
    #         self.mycursor.execute("""SELECT temp.Source, COUNT(*) FROM (SELECT Source FROM flight
    #                                                                     UNION ALL
    #                                                                     SELECT Destination FROM flight) temp
    #                                 GROUP BY temp.Source
    #                                 ORDER BY COUNT(*) DESC LIMIT 10
    #         """)
    #         data = self.mycursor.fetchall()
    #         for i in data:
    #             cities.append(i[0])
    #             frequency.append(i[1])
    #         return cities, frequency
    #     except Exception as e:
    #         print("Error:", e)
    #
    # def daily_frequency(self):
    #
    #     date = []
    #     frequency = []
    #
    #     self.mycursor.execute("""
    #                         SELECT Date_of_Journey,COUNT(*) FROM flight
    #                         GROUP BY Date_of_Journey
    #     """)
    #
    #     data = self.mycursor.fetchall()
    #
    #     for item in data:
    #         date.append(item[0])
    #         frequency.append(item[1])
    #
    #     return date, frequency