from DBHandler import DBHandler
from bayes_classifier import BayesClassifier

movies = DBHandler().get_test_movies()
moods = ["sadness", "fear", "joy", "surprise"]
total = 0
correct = 0
for movie in movies:
    total+=1
    id = movie[0]
    actual__mood = movie[1]
    # title = movie[3]
    b = BayesClassifier()
    predicted_mood = b.label(id)
    if predicted_mood == actual__mood:
        correct+=1
    print(str(total)  + " - " + str(correct))

print(str(correct/total))
