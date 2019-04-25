from math import log

import numpy as np

from DBHandler import DBHandler
from corpus_processing import Processor

### Fetches text and movie title of movie with @param - id
class BayesClassifier:
    def __init__(self,id):
        self.db = DBHandler()
        movie= self.db.get_subtitle(id)
        print(movie[0])
        self.bag = Processor().text_pre_processing(movie[1])

    ### Logratithmic Probability that a word belongs to a specific mood - P(word|mood)
    def calculate_word(self, word, mood):
        values = self.db.get_word_count(word,mood)
        return values[0]/values[1]

    ### Logarithmic Probability that a document/corpus blongs to a specific mood - P(corpus|mood)
    ### Achieved by adding the logarithmic probability of all individual words - sum(Pi(word|mood))
    def calculate_document(self,mood):
        total = 1
        for word in self.bag:
             #   print(self.calculate_word(word,mood))
                total+=log(self.calculate_word(word, mood))
        #print("----------------------------------------------------------------------------------------")
        return total

    # Calculates the logarithmic probability of a mood in the collection - P(mood)
    def calculate_mood(self,mood):
        values = self.db.get_mood_count(mood)
        return log(values[0]/values[1])

    # Calculates the logarithmic probability that an input corpus belongs to a mood - P(corpus|mood)
    def calculate_final(self,mood):
        return self.calculate_mood(mood) + self.calculate_document(mood)
