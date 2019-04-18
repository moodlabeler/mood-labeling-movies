import re
import operator
import nltk

from MovieSubtitles import MovieSubtitle
class Processor:
    def process(self,mood):
        subtitles = MovieSubtitle()
        res = subtitles.getSubtitles(mood)
        j=0
        for x in res:
            #tokens = nltk.word_tokenize(script)
            #tagged = nltk.pos_tag(tokens)
            data = {}
            script = str(x[0])
            #splitted = re.findall(r"[\w']+", script)
            #splitted = re.split(r'[\s-]+', script)
            splitted = re.split(r'[^A-Za-z0-9\\]+', script)
            #print(splitted)

            i = 0
            while i < len(splitted)-1:
                word = splitted[i]
                if word in data:
                    data[word] += 1
                else:
                    data[word] = 1
                i += 1

            #print(sorted(data.items(), key=operator.itemgetter(1), reverse=True))
            for key in sorted(data.items(), key=operator.itemgetter(1), reverse=True):
                #print(key[1])
                subtitles.storeWord(key[0],mood,key[1])
                i += 1

            print("----------------------------------------------------------")

        print("done")

pro = Processor()
pro.process("joy")
