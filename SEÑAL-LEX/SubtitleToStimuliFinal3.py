# read in the subtitle  frequency file and add the data to dictionary where the key is the word form
import sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


IN = open("data/FreqCorpus.txt") # abrimos el corpus del español
dictlist = {}

for w in IN:
    data = w.split()
    key, value = data[0], data[1:] # generamos un diccionario con las palabras más la frecuencia
    dictlist[key] = value
#print(list(dictlist.items())[:5])
IN.close()

# read through the stimuli file and print out. Aquí debemos declararlo en el command line así: cat results/wordlist.txt | python3 SubtitleToStimuliFinal3.py
inline = sys.stdin.readline() #
freqlist = []
cnt = 0
while inline:
    inline = inline.strip()
    if inline not in dictlist:
        inline = sys.stdin.readline()
        continue
    freq = dictlist[inline]
    freqlist.append((inline, freq))
    inline = sys.stdin.readline()

#pprint(freqlist)
#print(freqlist2)
x = list(zip(*freqlist))[0] # sacamos la información que necesitamos
y = list(zip(*freqlist))[1]
z = list(zip(*y))[1]

tokens = []
tokens2 = []
for i in x: # creamos las dos tablas
    data2 = i.split()
    data2 = i.strip()
    tokens.append(data2)


for y in z:
    data3 = y.split()
    data3 = y.strip()
    tokens2.append(data3)

cnt = 0

while cnt < len(tokens):
    print(tokens[cnt], tokens2[cnt], sep = '\t') # imprimimos las palabras junto con su frecuencia en el español
    cnt += 1


# Plot. Para hacer los gráficos necesitamos convertir los strings a floats.
#print(z[1])
#f = float(z[1])
#print(type(f))
#g = float(z[2])
#print(f + g)
num = [float(i) for i in z] # convertimos los strings a floats
#print(type(num))
#print(type(z))
#print(num[1] + num[2])
mean = (sum(num)/len(num)) # generamos el promedio
print("\nEl promedio de frecuencia global es:", round(mean))

frecuencia = ('Lexicon')
promedio = [mean]

fig = plt.figure(figsize =(10, 7))
plt.boxplot(num) # boxplot = mejor
plt.xticks([1], ['Frequency'])
#plt.yticks(np.arange(0, 3000, 250))
plt.title('Global Frequency in Spanish')
plt.savefig("results/frequency")


#print(z[1] + z[2])

"""
# otros intentos
#freqlist2 = ",".join(freqlist)
#for token in freqlist2:
 #   data2 = token.split()
  #  print(data2)
    #freqlist2.append(data2[0][2])

#while cnt <= len(freqlist):
 #   print(freqlist[cnt][0][2])
#print(freqlist[:5])

# Use this to change the file format to UTF-8
# $ cat FreqCorpus.txt | iconv -f latin1 -t utf-8 > l
# $ file l
# $ head l

# bar plot = no es el más bonito porque sólo hay una barra
plt.bar(frecuencia, promedio, align='center', alpha=0.5) # bar plot
plt.ylabel('Average')
plt.title('Global Frequency in Spanish')
plt.savefig("results/frequencyBar")

"""