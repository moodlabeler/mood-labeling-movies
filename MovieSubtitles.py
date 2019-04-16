import mysql.connector

class MovieSubtitle:
    def __init__(self):
        self.conn = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        database='moods')

    def getSubtitles(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT datafile FROM movies")
        result = cursor.fetchall()
        #for x in result:
        #    print(str(x))
        self.conn.close()
        return result
