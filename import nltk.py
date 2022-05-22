import nltk
import PyPDF2
from nltk.tag import pos_tag
import os
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import spacy
from spacy import displacy 

from nltk.corpus import stopwords
#jar = "/Users/lem1s/Desktop/tesis/tagger/stanford-postagger.jar"
#model = "/Users/lem1s/Desktop/tesis/tagger/models/english-bidirectional-distsim.tagger"
#java_path = "/Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home/bin/"
#os.environ["JAVAHOME"] = java_path
#pos_tagger = StanfordPOSTagger(model, jar, encoding = "utf-8")



pdfFileObject = open('asd.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
count = pdfReader.numPages
texto=""
for i in range(count):
    page = pdfReader.getPage(i)
    texto = texto + (page.extractText())
#print(texto)

#Oracionestokenizado=sent_tokenize(texto)
PalabrasTokenizado=word_tokenize(texto)
nlp = spacy.load('es_core_news_sm')
doc = nlp(texto)
#print([(w.text, w.pos_) for w in doc])
#tagged_words = pos_tagger.tag(PalabrasTokenizado[0])
#print(tagged_words)

##palabra mas usada
sr= stopwords.words('spanish')
clean_tokens = PalabrasTokenizado[:]
for token in PalabrasTokenizado:
    if token in stopwords.words('spanish'):
        
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
#for key,val in freq.items():
    #print(str(key) + ':' + str(val))
#freq.plot(20, cumulative=False)

#using spacy
nlp = spacy.load('es_core_news_sm')

doc = nlp("Las personas estan mirando  las galletas de fresa")
for token in doc:
    print(token.dep_)




for token in doc:
    # extract subject
    if (token.dep_=='nsubj'):
        print(token.text)
    # extract object
    elif (token.dep_=='pcomp'):
        print(token.text)