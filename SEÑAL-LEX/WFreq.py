import sys
import nltk
import seaborn as sns
import matplotlib.pyplot as plt
import math

with open(sys.argv[1], 'r') as ifile: # abrimos el archivo. Aquí debemos declararlo en el command line así: python3 Wfreq.py data/TestFile.txt
    text = ifile.read()
ifile.close()
#print(text[:300], "...")

text = text.lower() # Enter NLTK
myFD = nltk.FreqDist(text)

tokens = nltk.word_tokenize(text) # tokenization
tokens = [w.lower() for w in tokens]

# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]

from nltk.corpus import stopwords # removing stop words
stop_words = set(stopwords.words('spanish'))
words = [w for w in words if not w in stop_words]
#print(words[:20])

# Distribution
myTokenFD = nltk.FreqDist(words)

# relative frequency try. Hay que intentar incluir la freq. relativa a las tablas de palabras más comunes.

#sum(myTokenFD.values())
total= float(sum(myTokenFD.values())) # relative frequency
total = int(total)
#relfrqtokens = [x / total for x in myTokenFD.values()]


# Unigrams and Bigrams
print("These are the 20 most common words in the dataset:")
print("Token:\t\tFrequency:\t\tRelative Frequency")
for i in myTokenFD.most_common(20): # imprimimos
    print("{}\t\t{}\t\t{}".format(i[0],i[1], (i[1]/total)))

# Type/token ratio
print("Type/Token ratio:", myTokenFD)
print("\n")
# bigrams
myTokenBigrams = nltk.ngrams(words, 2)
bigrams = list(myTokenBigrams)
myBigramFD = nltk.FreqDist(bigrams)
totalbi= float(sum(myBigramFD.values())) # relative frequency
totalbi = int(totalbi)
print("These are the 20 most common bigrams in the dataset:")
print("Bigram:\t\tFrequency:\t\tRelative Frequency")
for ngram in list(myBigramFD.most_common(20)): # imprimimos
    print(" ".join(ngram[0]), "\t", ngram[1], "\t", (ngram[1]/totalbi))
print("Type/Token ratio for bigrams:", myBigramFD)


bag = []
for token in list(myTokenFD.items()): # creamos una tabla con todas las palabras generadas
    bag.append(token[0])

f=open('results/wordlist.txt','w')
bag=map(lambda x:x+'\n', bag) # creamos el archivo txt para ser procesado por el script SubtitleToStimuliFinal3.py
f.writelines(bag)
f.close()

#PLOTS
#Unigrams
common_words = [word[0] for word in myTokenFD.most_common(20)]
common_counts = [word[1] for word in myTokenFD.most_common(20)] # gráfico con las 20 palabras más comunes
fig1 = plt.figure(figsize=(18,6))
sns.barplot(x= common_words, y= common_counts)
plt.title('20 most frequent words used in the dataset')
plt.savefig("results/unigrams")


common_bigrams = [bigram[0] for bigram in myBigramFD.most_common(10)]
common_bigrams = [' '.join(i) for i in common_bigrams] # use list comprehensio instead
bigram_counts = [bigram[1] for bigram in myBigramFD.most_common(10)]

fig2 = plt.figure(figsize=(18,6))
sns.barplot(x= common_bigrams, y= bigram_counts)
plt.title('10 most frequent bigrams used in the dataset')
plt.savefig("results/bigrams")
