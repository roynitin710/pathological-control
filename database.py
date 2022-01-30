import mysql.connector


class DB:

    def __init__(self):
        # connect to database
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='pathcon')
            self.mycursor = self.conn.cursor()
            print("Connected to Database")
        except:
            print("Couldn't connect to database")

    def register_user(self, name, username, password):
        try:
            temp_query = "SELECT * FROM users WHERE username LIKE '{}'".format(username)
            self.mycursor.execute(temp_query)
            temp_data = self.mycursor.fetchall()
            if len(temp_data) != 0:
                return -1
            else:
                query = "INSERT INTO users VALUES (NULL,'{}','{}','{}', 0, 0, 0, 0)".format(name, username, password)
                self.mycursor.execute(query)
                self.conn.commit()
                return 1
        except:
            return 0

    def login_user(self, username, password):
        try:
            query = "SELECT * FROM users WHERE username LIKE '{}' AND password LIKE '{}'".format(username, password)
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            return data
        except:
            return 0

    def fetch_user_data(self, user_id):
        try:
            query = "SELECT * FROM users WHERE user_id = {}".format(user_id)
            self.mycursor.execute(query)
            data = self.mycursor.fetchall()
            return data
        except:
            return 0

    # def fetch_score(self, category):
    #     try:
    #         query = "SELECT user_id, name, username, {} FROM users ORDER BY {} DESC".format(category, category)
    #         self.mycursor.execute(query)
    #         data = self.mycursor.fetchall()
    #         return data
    #     except:
    #         return 0

    # def update_score_in_db(self, update_score, category, user_id):
    #     try:
    #         query = "UPDATE users SET {}={} WHERE user_id={}".format(category, update_score, user_id)
    #         self.mycursor.execute(query)
    #         self.conn.commit()
    #     except:
    #         return 0