from DBHandler import DBHandler

DBHandler().get_all_word()

"""def get_all_word(self):
    cursor = self.conn.cursor()
    cursor.execute("SELECT word,fear FROM words")
    result = cursor.fetchall()
    # print("[word - occurence]")
    # print(result)
    for x in sorted(result, key=lambda x: int(x[1]), reverse=True):
        if x[1] > 1000:
            print(x[0] + " & " + str(x[1]) + "\\" + "\\")
"""
