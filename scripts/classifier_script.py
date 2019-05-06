import datetime
import operator
from math import exp, log

from soupsieve.util import upper

from DBHandler import DBHandler
from bayes_classifier import BayesClassifier


def print_results(tot_movies, correct_class, result_file):
    print("Total movies: ", tot_movies)
    print("Correct guesses: ", correct_class)
    print("Correct percentage: ", correct_class / tot_movies)
    result_file.write("Total movies: " + str(tot_movies) + "\n")
    result_file.write("Correct guesses: " + str(correct_class) + "\n")
    result_file.write("Correct percentage: " + str(correct_class / tot_movies) + "\n")
    result_file.close()
    print("------------------------")
    print("Done")
    print("------------------------")


def print_start():
    file_name = str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S")) + ".txt"
    print("------------------------")
    print("Printing results to file ", file_name)
    print("------------------------")
    return open(file_name, 'w')


movies = DBHandler().get_test_movies()
correct_class = 0
tot_movies = 0
result_file = print_start()
for movie in movies:
    tot_movies += 1
    id = movie[0]
    mood = movie[1]
    subtitles = movie[2]
    title = movie[3]
    b = BayesClassifier(id)
    dir = {}
    dir["sadness"] = b.calculate_final("sadness")
    dir["surprise"] = b.calculate_final("surprise")
    dir["fear"] = b.calculate_final("fear")
    dir["joy"] = b.calculate_final("joy")
    result_mood = max(dir.items(), key=operator.itemgetter(1))[0]
    print(title + "-" + upper(mood) + " - " + upper(result_mood))
    result_file.write(title + " - " + upper(mood) + " - " + upper(result_mood) + "\n")
    if mood == result_mood:
        correct_class += 1
    for key in dir.items():
        print(key)
        result_file.write(str(key) + "\n")
    result_file.write("\n")
print_results(tot_movies, correct_class, result_file)
