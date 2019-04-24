from DBHandler import DBHandler
from corpus_processing import Processor
class BayesClassifier:
    def __init__(self,corpus):
        self.bag = Processor.text_pre_processing(corpus)
        self.db = DBHandler()

    ### Probability that a word belongs to a specific mood
    def calculate_word(self, word, mood):
        values = self.db.get_word_count(word,mood)
        return values[0]/values[1]

    ### Probability that a document/corpus blongs to a specific mood
    def calculate_document(self,mood):
        total = 1
        for word in self.bag:
           total *=self.calculate_word(word, mood)
        return total


b = BayesClassifier("whatup my man")
print(b.db.get_subtitle(6))

