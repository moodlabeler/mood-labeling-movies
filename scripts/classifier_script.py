from integration.DBHandler import DBHandler
from model.bayes_classifier import BayesClassifier


def print_results(tot_movies, correct_class, result_file):
    print("Total movies: ", tot_movies)
    print("Correct guesses: ", correct_class)
    print("Correct percentage: ", correct_class / tot_movies)
    print("------------------------")
    print("Done")
    print("------------------------")


def calculate_results(TP, FP, FN, tot_movies, correct_guess):
    if FP == 0 and TP == 0:
        precsision = -1
    else:
        precsision = TP / (TP + FP)
    if TP == 0 and FN == 0:
        recall = -1
    else:
        recall = TP / (TP + FN)
    accuracy = correct_guess / tot_movies
    print("Recall: ", recall)
    print("Precsision: ", precsision)
    # print("Accuracy: ", accuracy)
    print("TP : " + str(TP) + ", FP : " + str(FP) + " , FN : " + str(FN))
    print("***********************")


movies = DBHandler().get_test_movies()
results = []
moods = ["sadness", "fear", "joy", "surprise"]
tot_movies = 0
for movie in movies:
    tot_movies += 1
    id = movie[0]
    actual__mood = movie[1]
    # title = movie[3]
    b = BayesClassifier()
    predicted_mood = b.label(id)
    print(actual__mood + " - " + predicted_mood)
    results.append([actual__mood, predicted_mood])


for current_mood in moods:
    print("Calculating for: " + current_mood)
    correct_guess = 0
    TP = 0
    FP = 0
    FN = 0
    for result in results:
        predicted_mood = result[1]
        actual__mood = result[0]
        if current_mood == predicted_mood and actual__mood == predicted_mood:
                TP += 1
        elif current_mood == predicted_mood and actual__mood != predicted_mood:
                FP += 1
        elif current_mood == actual__mood and actual__mood != predicted_mood:
                FN += 1
        if predicted_mood == actual__mood:
                correct_guess += 1
    calculate_results(TP, FP, FN, tot_movies, correct_guess)

# print_results(tot_movies, correct_class, result_file)
