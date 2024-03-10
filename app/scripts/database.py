import json
import mysql.connector
import pandas as pd

class database:
    def __init__(self):
        with open("/app/config/database.json", "r") as file:
            config_data = json.load(file)

        self.cnx = mysql.connector.connect(
            user = config_data["user"],
            password = config_data["password"],
            host = config_data["host"],
            port = config_data["port"],
            database = config_data["database"],
            auth_plugin = 'mysql_native_passowrd'
        )

        self.cursor = self.cnx.cursor()

    def add_exercise(self, date, name, num_sets, reps, weights):
        query = """
        INSERT INTO gym_exercises (exercise_date, exercise_name, num_sets)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(query, (date, name, num_sets))
        # query = "LAST_INSERT_ID()"
        query = "SET @exercise_id = LAST_INSERT_ID()"
        self.cursor.execute(query)
        query = "INSERT INTO gym_sets (exercise_id, set_num, weight, reps) VALUES (@exercise_id, %s, %s, %s)"
        for i in range(num_sets):
            self.cursor.execute(query, (i+1, weights[i], reps[i]))
        self.cnx.commit()

    def add_gym_sets(self, id, set_num, weight, reps):
        query = """
        INSERT INTO gym_sets (exercise_id, set_num, weight, reps)
        VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(query, (id, set_num, weight, reps))

    def search_exercise(self, name):
        query = f"""
        SELECT * FROM gym_exercises WHERE exercise_name = '{name}'
        """

        self.cursor.execute(query)
        result_set = self.cursor.fetchall()
        df = pd.DataFrame(result_set, columns=[desc[0] for desc in self.cursor.description])

        sets = df['id'].unique()
        df2s = []
        # for row in df, save unique exercise_id values
        for item in sets:
            df2s.append(self.get_exercise_sets(item))

        return df, df2s

    def get_exercise_sets(self, id):
        query = f"""
        SELECT * FROM gym_sets WHERE exercise_id = {id}
        """

        self.cursor.execute(query)
        result_set = self.cursor.fetchall()
        df = pd.DataFrame(result_set, columns=[desc[0] for desc in self.cursor.description])

        return df

    def add_swim(self, date, time, total_yards, distance, mid, sprint, stroke, technique, other):
        query = """
        INSERT INTO swim (swim_date, swim_time, total_yards, distance, mid, sprint, stroke, technique, other)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        self.cursor.execute(query, (date, time, total_yards, distance, mid, sprint, stroke, technique, other))
        self.cnx.commit()

    def add_bjj(self, date, time, practice, rolling):
        query = """
        INSERT INTO bjj (bjj_date, bjj_time, practice, rolling)
        VALUES (%s, %s, %s, %s)
        """

        self.cursor.execute(query, (date, time, practice, rolling))
        self.cnx.commit()

    def add_volley(self, date, time, games, practice, matches):
        query = """
        INSERT INTO volley(volley_date, volley_time, games, practice, matches)
        VALUES (%s, %s, %s, %s, %s)
        """

        self.cursor.execute(query, (date, time, games, practice, matches))
        self.cnx.commit()
