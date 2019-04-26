from DBHandler import DBHandler
from bayes_classifier import BayesClassifier

movies = DBHandler().get_test_movies()
for movie in movies:
    id = movie[0]
    mood = movie[1]
    subtitles = movie[2]
    title = movie[3]
    print (title + "-" + mood)
    b = BayesClassifier(id)
    dir = {}
    dir["sadness"] = b.calculate_final("sadness")
    dir["surprise"] = b.calculate_final("surprise")
    dir["fear"] = b.calculate_final("fear")
    dir["joy"] = b.calculate_final("joy")
    for key in dir.items():
        print(key)
