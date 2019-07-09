# Python 3

# Be sure you have followed the instructions to download the 98-0.txt,
# the text of A Tale of Two Cities, by Charles Dickens

import collections

file=open('98-0.txt')
fileStopWords = open('stopwords.txt')

# if you want to use stopwords, here's an example of how to do this

print('doing the stop words thing..')
#stopwords = set(line.strip() for line in open('stopwords.txt'))


  
# create your data structure here.  F
wordcount={}

stopwords={}
stopwords = fileStopWords.read().lower().split()


# for w in stopwords:
#     print(w)
    
print(len(stopwords))

# Instantiate a dictionary, and for every word in the file, add to 
# the dictionary if it doesn't exist. If it does, increase the count.

# Hint: To eliminate duplicates, remember to split by punctuation, 
# and use case demiliters. The functions lower() and split() will be useful!

# remvomves punctuation from the text
for word in file.read().lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace("\"","")
    word = word.replace("“","")
    #print(word)
# adds word and word frequency to the dictionary 
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

# after building your wordcount, you can then sort it and return the first
# n words.  If you want, collections.Counter may be useful.

d = collections.Counter(wordcount)
for word, count in d.most_common(10):
	print(word, ": ", count)
