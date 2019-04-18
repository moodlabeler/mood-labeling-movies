import operator
import re

import nltk
from nltk.corpus import stopwords
from DBHandler import DBHandler


class Processor:
    def text_pre_processing(self,mood):
        ### NLTK
        stemmer = nltk.SnowballStemmer("swedish")
        dbhandler = DBHandler()
        res = dbhandler.getSubtitles(mood)
        j=0
        for x in res:
            bag = {}
            script = x[0]

            ### Decode for special characters, lowercase and split the string into independant words.
            script = script.decode('utf-8')
            script = script.lower()

            splitted = re.split(r'[^A-Za-z0-9\wåäöÅÄÖ]+', script)
            #print(splitted)

            ### Fill in the bag-of-words with stemmed non-stopwords
            i = 0
            while i < len(splitted)-1:
                if splitted[i] not in stopwords.words('swedish'):
                    word = stemmer.stem(splitted[i])
                    if word in bag:
                        bag[word] += 1
                    else:
                     #   print(word)
                        bag[word] = 1
                i += 1
            for key in sorted(bag.items(), key=operator.itemgetter(1), reverse=True):
                dbhandler.storeWord(key[0],mood,key[1])
                i += 1
        dbhandler.disconnect()



    def clear_lexicons(self):
        s = DBHandler()
        s.delete()


pro = Processor()
pro.clear_lexicons()
pro.text_pre_processing("surprise")
pro.text_pre_processing("joy")
pro.text_pre_processing("fear")
pro.text_pre_processing("sadness")
print("Lexicon created")
