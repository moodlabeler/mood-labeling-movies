import re
import operator
import nltk
import zlib

from MovieSubtitles import MovieSubtitle
class Processor:
    def text_pre_processing(self,mood):
        subtitles = MovieSubtitle()
        res = subtitles.getSubtitles(mood)
        j=0
        for x in res:
            bag = {}
            script = x[0]

            ### Decode for special characters, lowercase and split the string into independant words.
            script = script.decode('utf-8')
            script = script.lower()
            splitted = re.split(r'[^A-Za-z0-9\wåäöÅÄÖ]+', script)


            ### Fill in the bag-of-words
            i = 0
            while i < len(splitted)-1:
                word = splitted[i]
                if word in bag:
                    bag[word] += 1
                else:
                    bag[word] = 1
                i += 1
            for key in sorted(bag.items(), key=operator.itemgetter(1), reverse=True):
                subtitles.storeWord(key[0],mood,key[1])
                i += 1
        subtitles.disconnect()



    def clear_lexicons(self):
        s = MovieSubtitle()
        s.delete()


pro = Processor()
pro.clear_lexicons()
pro.text_pre_processing("surprise")
pro.text_pre_processing("joy")
pro.text_pre_processing("fear")
pro.text_pre_processing("sadness")
print("Lexicon created")
