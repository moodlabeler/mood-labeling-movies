from bayes_classifier import BayesClassifier

b = BayesClassifier(60) ## Insert id from database
dir = {}
dir["sadness"] = b.calculate_document("sadness")
dir["surprise"] = b.calculate_document("surprise")
dir["fear"] = b.calculate_document("fear")
dir["joy"] = b.calculate_document("joy")
for key in dir.items():
    print(key)
