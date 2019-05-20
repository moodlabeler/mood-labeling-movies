from integration.DBHandler import DBHandler
from model.stopwords import Stopword



# prints all words that occur more than @occurence_per_movie times for all moods.
def find_common_words(occurence_per_movie, mood):
    db = DBHandler()
    i = 0
    list = db.get_all_word(mood)
    moods = db.list_moods()
    movie_count_for_joy = db.get_count_movies_for_mood("joy")
    movie_count_for_fear = db.get_count_movies_for_mood("fear")
    movie_count_for_surprise = db.get_count_movies_for_mood("surprise")
    movie_count_for_sadness = db.get_count_movies_for_mood("sadness")

    for element in list:
        if db.get_word_count(element[0], 'fear')[0] / movie_count_for_fear > occurence_per_movie \
                and db.get_word_count(element[0], 'sadness')[0] / movie_count_for_sadness > occurence_per_movie \
                and db.get_word_count(element[0], 'surprise')[0] / movie_count_for_surprise > occurence_per_movie \
                and db.get_word_count(element[0], 'joy')[0] / movie_count_for_joy > occurence_per_movie:
            print("\"" + element[0] + "\",", end='')
    print("}", end='', flush=True)


# find_common_words(1, "sadness")


# @param - mood - most common words for which mood
# @param - stopwords - boolean, should stopwords be included or not
def latex_format(mood,stopwords):
    db = DBHandler()
    i = 0
    list = db.get_all_word(mood)
    stopword_list = Stopword().stopwords
    count_movies = db.get_count_movies_for_mood(mood)
    for x in list:
        if i == 10:
            break
        if stopwords or (x[0] not in stopword_list):
            print(x[0] + " & " + str(round(x[1]/count_movies,1)) + "\\" + "\\")
            i += 1
latex_format("joy",True)
