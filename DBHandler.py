import mysql.connector

class DBHandler:
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
        resultCursor.execute("SET NAMES utf8mb4;")  # or utf8 or any other charset you want to handle

        resultCursor.execute("SET CHARACTER SET utf8mb4;")  # same as above

        resultCursor.execute("SET character_set_connection=utf8mb4;")  # same as above
        resultCursor.execute("SELECT datafile,movie_title FROM resources WHERE mood=%s and datafile IS NOT NULL"
                             ,(mood_id[0][0],))
        result = resultCursor.fetchall()
        return result

    def storeWord(self,word,mood,count):
        cursor = self.conn.cursor()
        count_cursor = self.conn.cursor()
        total = 0
        count_cursor.execute("SELECT EXISTS(SELECT 1 FROM words WHERE word=%s)", (word,))
        word_exists = count_cursor.fetchall()
        if word_exists[0][0] == 0:
            total = count
            cursor.execute("INSERT INTO words (word, {moodp}) VALUES (%s,%s)".format(moodp=mood), (word, total))
        else:
            count_cursor.execute("SELECT {moodp} FROM words WHERE word=%s".format(moodp=mood), (word,))
            word_count = count_cursor.fetchall()
            total = word_count[0][0]+count
            cursor.execute("UPDATE words SET {moodp} = %s WHERE word = %s".format(moodp=mood), (total,word,))
        self.conn.commit()
        #print(total)

    def get_subtitle(self,id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MOVIE_TITLE,datafile FROM test WHERE id=%s"
                         , (id,))
        result = cursor.fetchall()
        return result[0]

    def disconnect(self):
        self.conn.disconnect()

    def delete(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM words")
        self.conn.commit()
        self.conn.disconnect()

    def list_moods(self):
        array = []
        mood_cursor = self.conn.cursor()
        mood_cursor.execute("SELECT mood FROM moods")
        mood_list = mood_cursor.fetchall()
        i=0
        for mood in mood_list:
            array.append(mood[0])
        return array


    # mood_value - the occurence of a word in the context of a specific mood
    # total - the total occurence of the word in the lexicon
    # @return {mood_value, total}
    def get_word_count(self,word,mood):
        total = 0
        mood_value = 0
        cursor = self.conn.cursor()
        count_cursor = self.conn.cursor()
        list = self.list_moods()
        for element in list:
            count_cursor.execute("SELECT {moodp} FROM words WHERE word=%s ".format(moodp=element), (word,))
            count_array = count_cursor.fetchall()
            if len(count_array) <= 0:
                return [1,1]
            count = count_array[0][0]
            total +=count   #total is for all the words in all the moods
            if element == mood:
                mood_value=count    #count is specific word in specific mood
        return [mood_value,total]

    # Returns the total occurence of words for a specific mood and the total occurence of words for all moods.
    def get_mood_count(self,mood):
        total = 0
        mood_value = 0
        cursor = self.conn.cursor()
        list = self.list_moods()
        for element in list:
            cursor.execute("SELECT SUM({moodp}) FROM words".format(moodp=element))
            count = cursor.fetchall()[0][0]
            total += count
            if element == mood:
                mood_value = count
        return [mood_value, total]
    #cursor.execute("SELECT {moodp} FROM words WHERE word=%s ".format(moodp=mood), (word,))

    def get_all_word(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT word,joy FROM words")
        result = cursor.fetchall()
        print("word - joy - fear - sadness - surprise")
        print(result)
        for x in result:
            print(x[0] + "-"+ str(x[1]))

    def get_test_movies(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT test.ID,moods.mood,datafile,  movie_title FROM test, moods WHERE test.mood = moods.mood_id")
        #cursor.execute("SELECT movie_title FROM test",())
        result = cursor.fetchall()
        return result

    def count_all_moods(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(word) FROM words")
        result = cursor.fetchall()
        return result[0][0]
