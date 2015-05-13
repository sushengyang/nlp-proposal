# -*- coding: utf-8 -*-
import nltk, random
from nltk.probability import FreqDist, ELEProbDist
from nltk.classify.util import apply_features
from nltk.metrics.scores import accuracy

# Getting data from train-data.txt in appropriate form.
posList, negList = [], []
pos, neg = [], []
posTuple, negTuple = (), ()
txt = open("train-data.txt", "r")
for line in txt:
	if(line[:3]=='pos'):
		posList.append(line[5:-1])
	if(line[:3]=='neg'):
		negList.append(line[5:-1])
for p in posList[:25]:
	tupples = posTuple + (p,) + ("positive",)
	pos.append(tupples)
#print pos
for n in negList[:25]:
	tupples = negTuple + (n,) + ("negative",)
	neg.append(tupples)
#print neg

#picking random objects from data
test = []
test_reviews = []
posTestTuple = ()
negTestTuple = ()
for p in range(5):
	p = posList[random.randrange(26)]
	test.append(p)
	tupples = posTestTuple + (p,) + ("positive",)
	test_reviews.append(tupples)

for n in range(5):
	n = negList[random.randrange(26)]
	test.append(n)
	tupples = negTestTuple + (n,) + ("negative",)
	test_reviews.append(tupples)
print test_reviews
	
reviews = []
for (words, sentiment) in pos + neg:
	words_filtered = [e.lower() for e in words.split() if len(e)>3]
	reviews.append((words_filtered, sentiment))

def get_all_words(reviews):
	all_words = []
	for (words, sentiment) in reviews:
		all_words.extend(words)
	return all_words
def get_features(wordlist):
	wordlist = FreqDist(wordlist)
	word_features = wordlist.keys()
	print wordlist
	return word_features

review_features = get_features(get_all_words(reviews))
#print review_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in review_features:
      features['contains(%s)' % word] = (word in document_words)
    #print features
    return features

training_set = apply_features(extract_features, reviews)
classifier = nltk.classify.NaiveBayesClassifier.train(training_set)


#test = ["berbat bir yer", "Muhteşem bir yer.","harika","mükemmel bir yer","vasat","rezalet","Başarılı","Kötü yemekler"]

for r in test:
	print classifier.classify(extract_features(r.split()))


				
test_set = apply_features(extract_features, test_reviews)

print nltk.metrics.scores.accuracy(classifier, test_set)
#print classifier.show_most_informative_features(1)
