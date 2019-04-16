import re
import operator
import nltk
from MovieSubtitles import MovieSubtitle

subtitles = MovieSubtitle()
res = subtitles.getSubtitles()
j=0
for x in res:
    print(x)
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

    another_fh = open("words", "w")

    #dict = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    #print(dict)
    for key in sorted(data.items(), key=operator.itemgetter(1), reverse=True):
        another_fh.write(str(key[0]) + " - " + str(key[1]) + "\n")
        print(key)
        i += 1

    another_fh.close()
    print("----------------------------------------------------------")

print("done")
