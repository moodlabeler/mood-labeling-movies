from DBHandler import DBHandler


def find_common_words(occurence_per_movie, mood):
    db = DBHandler()
    i = 0
    list = db.get_all_word(mood)
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


find_common_words(1, "sadness")
print("}", end='', flush=True)
