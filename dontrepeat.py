from nltk import ngrams
from glob import glob
from sys import argv


n = 10
alltext=''
if len(argv)>1:
    n = int(argv[1])

if len(argv)>2:
    for i in range(2,len(argv)):
        f = file(argv[i],'r')
        for line in f.readlines():
            if line[0]!='%':
                alltext=alltext+' '+ line
else:
    for tex in glob("*.tex"):
        f = file(tex,'r')
        for line in f.readlines():
            if line[0]!='%':
                alltext=alltext+' '+ line

alltext = alltext.replace('\n',' ')
wordsequence = alltext.split()
teddygrams = ngrams(wordsequence,n)
teddygramhashes = {}
i = 0

repeatedgrams = []
for gram in teddygrams:
    blob = ''.join(gram)
    i+=1
    if teddygramhashes.has_key(blob):
        teddygramhashes[blob].append(gram)
    else:
        teddygramhashes[blob] = [gram]

teddygramhashcounts = []


for blob in teddygramhashes.keys():
    if len(teddygramhashes[blob])>1:
        print teddygramhashes[blob]

    teddygramhashcounts.append((len(teddygramhashes[blob]),teddygramhashes[blob]))
sorted(teddygramhashcounts,reverse=True)[0:1000]

#for i in *.tex; do echo $i; grep 'densest regular lattice possible' $i; done
