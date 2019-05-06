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

def calculate_results(TP, FP, FN, tot_movies, correct_guess):
    precsision = TP / (TP + FP)
    recall = TP / (TP + FN)
    accuracy = correct_guess / tot_movies
    print("Recall: ", recall)
    print("Precsision: ", precsision)
    print("Accuracy: ", accuracy)

movies = DBHandler().get_test_movies()
result_file = print_start()
moods = ["sadness", "fear", "joy", "surprise"]
for current_mood in moods:
    correct_guess = 0
    tot_movies = 0
    TP = 0
    FP = 0
    FN = 0
    print("Evaluating ", current_mood)
    for movie in movies:
        tot_movies += 1
        id = movie[0]
        actual__mood = movie[2]
        #title = movie[3]
        b = BayesClassifier()
        predicted_mood = b.label(id)
        if current_mood == predicted_mood and actual__mood == predicted_mood:
            TP += 1
            correct_guess += 1
        elif current_mood == predicted_mood and actual__mood != predicted_mood:
            FP += 1
        else:
            FN += 1
    calculate_results(TP, FP, FN, tot_movies, correct_guess)



print_results(tot_movies, correct_class, result_file)
