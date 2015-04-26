# -*- coding: utf-8 -*-
import nltk
from nltk.probability import FreqDist, ELEProbDist
from nltk.classify.util import apply_features

pos = [('Cennet','positive'), 
('GAYET BAŞARILI','positive'),
('Cennet boyle bir yermidir?','positive'),
('Kendinize iyilik yapin, D hotele gidin..','positive'),
('Muhteşem bir tatil ve harika bir eğlence','positive')]

neg = [('okadar uzun ve yorucu yol,haketmeyen fıyatlar, abartılı reklam','negative'),
('beklendiği gibi değil...','negative'),
('Vasatın altı','negative'),
('yemekler berbat !','negative'),
('hayal kırıklıgı','negative')]

reviews = []
for (words, sentiment) in pos + neg:
	words_filtered = [e.lower() for e in words.split() if len(e)>3]
	reviews.append((words_filtered, sentiment))

#print reviews

def get_all_words(reviews):
	all_words = []
	for (words, sentiment) in reviews:
		all_words.extend(words)
	return all_words
def get_features(wordlist):
	wordlist = FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features

review_features = get_features(get_all_words(reviews))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in review_features:
      features['contains(%s)' % word] = (word in document_words)
    return features

training_set = apply_features(extract_features, reviews)
classifier = nltk.classify.NaiveBayesClassifier.train(training_set)


test = ["berbat bir yer", "muhteşem bir yer","harika","vasat bir yer"]
for r in test:
	print classifier.classify(extract_features(r.split()))