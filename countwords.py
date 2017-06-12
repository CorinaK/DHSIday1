import codecs

stopwords = set()
for line in codecs.open('stopwords_fr.txt', encoding='utf8'):
    stopwords.add(line.strip())

def tokenize_words(line):
    without_spaces = line.strip().lower()
    tokenized = without_spaces.split(' ')
    outputwords = []
    for word in tokenized:
        if word != '' and word not in stopwords:
            outputwords.append(word)

    return outputwords

countedwords = {}
in_file = codecs.open('le-musee.txt', encoding='utf8')
for line in in_file:
    tokenizedwords = tokenize_words(line)

    for word in tokenizedwords:
        countedwords.setdefault(word, 0)
        countedwords[word] += 1
# Two lines above replace the stuff in this comment:
#        if word in countedwords:
#            countedwords[word] += 1
#        else:
#            countedwords[word] = 1

out_file = codecs.open('output.txt', 'w', encoding='utf8')
for key, value in sorted(countedwords.items(), key=lambda x:x[1]):
    out_file.write(key + ': ' + str(value) + '\n')