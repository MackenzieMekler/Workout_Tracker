import json
import mysql.connector

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
        query = "SET @exercise_id = LAST_INSERT_ID()"
        self.cursor.execute(query)
        query = "INSERT INTO gym_sets (exercise_id, set_num, weight, reps) VALUES (@exercise_id, %s, %s, %s)"
        for i in range(num_sets):
            self.cursor.execute(query, (i+1, weights[i], reps[i]))
        self.cnx.commit()
