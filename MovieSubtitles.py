import mysql.connector

class MovieSubtitle:
    def __init__(self):
        self.conn = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        database='moods')

    def getSubtitles(self,mood):
        cursor = self.conn.cursor()
        resultCursor = self.conn.cursor()
        cursor.execute("SELECT mood_id FROM moods WHERE mood=%s",(mood,))
        mood_id = cursor.fetchall()
        if len(mood_id)<1:
            return []
        resultCursor.execute("SELECT datafile FROM movies WHERE mood=%s"
                             ,(mood_id[0][0],))
        result = resultCursor.fetchall()
        self.conn.close()
        return result
