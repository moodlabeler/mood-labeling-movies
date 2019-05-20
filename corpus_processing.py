import operator
import re

import nltk
from nltk.corpus import stopwords

from Stopword import Stopword
from DBHandler import DBHandler


class Processor:
    def construct_lexicon(self, mood):
        ### NLTK
        print(mood)
        dbhandler = DBHandler()
        res = dbhandler.getSubtitles(mood)
        j=0
        self.occ = 0
        self.occlist = []
        for x in res:
            bag = self.text_pre_processing(x[0])
            i=0
            for key in bag.items():
                dbhandler.storeWord(key[0],mood,key[1])
                i += 1
        print(self.occ)
        print(self.occlist)
        print("--------------------")
        dbhandler.disconnect()

    def text_pre_processing(self, text):
        stemmer = nltk.SnowballStemmer("swedish")
        bag = {}
        script = text

        ### Decode for special characters, lowercase and split the string into independant words.
        script = script.decode('utf-8')
        script = script.lower()
        splitted = re.split(r'[^A-Za-z0-9\wåäöÅÄÖ]+', script)
        # print(splitted)

        ### Fill in the bag-of-words with stemmed non-stopwords
        i = 0
        occ = 0
        while i < len(splitted) - 1:
            if splitted[i] not in stopwords.words('swedish') and splitted[i] not in Stopword().stopwords:
                if stemmer.stem(splitted[i]) =="tunn":
                    self.occ += 1
                    if splitted[i] not in self.occlist:
                        self.occlist.append(splitted[i])
                word = stemmer.stem(splitted[i])
                #word = splitted[i]
                #print(word)
                if word in bag:
                    bag[word] += 1
                else:
                    #   print(word)
                    bag[word] = 1
            i += 1
        return bag


    def clear_lexicons(self):
        s = DBHandler()
        s.delete()


