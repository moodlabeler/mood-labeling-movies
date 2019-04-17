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
            #print(x)
            #print(script)
            #tokens = nltk.word_tokenize(script)
            #tagged = nltk.pos_tag(tokens)
            data = {}
            script = str(x)
            splitted = re.findall(r"[\w']+", script)
            #print(splitted)

            i = 0
            while i < len(splitted)-1:
                word = splitted[i]
                if word in data:
                    data[word] += 1
                else:
                    data[word] = 1
                i += 1

            print(sorted(data.items(), key=operator.itemgetter(1), reverse=True))
           # for key in sorted(data.items(), key=operator.itemgetter(1), reverse=True):
           #     print(key)
           #     i += 1

            print("----------------------------------------------------------")

        print("done")

pro = Processor()
pro.process("joy")
