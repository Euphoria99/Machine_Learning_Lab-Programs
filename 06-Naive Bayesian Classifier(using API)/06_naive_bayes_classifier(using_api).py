# -*- coding: utf-8 -*-
"""06.Naive-Bayes-Classifier(using API).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZLDQ39Ml7Hc1bcguvYWA_cEUadbs4ooC

6. **Assuming a set of documents that need to be classified, use the naïve Bayesian Classifier model to perform this task. Built-in Java classes/API can be used to write the program. Calculate the accuracy, precision, and recall for your data set.**
"""

import pandas as pd

msg = pd.read_csv('text_doc.csv', names = ('message', 'label'))

#contains 18 different rows in dataset
print("Total Instance of Database: " , msg.shape[0])

#identifying target value with positive 1 and neg 0
msg ['labelnum'] = msg.label.map( {'pos' : 1, 'neg': 0})

X = msg.message
print(X)

y = msg.labelnum
print(y)

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)

from sklearn.feature_extraction.text  import CountVectorizer

#convert a collection of text documents to a matrix of token counts
count_v = CountVectorizer()

#calculating the mean and variance of each of the features present in our data.
Xtrain_dm = count_v.fit_transform(Xtrain)

Xtest_dm = count_v.transform(Xtest)

df = pd.DataFrame(Xtrain_dm.toarray(), columns=count_v.get_feature_names())
print(count_v.get_feature_names())

print(df[0:5])
print(df)

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()

clf.fit(Xtrain_dm, ytrain)

pred = clf.predict(Xtest_dm)

for doc, p in zip(Xtrain, pred):
    p = 'pos' if p == 1 else 'neg'
    print("%s -> %s" % (doc,p))

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

print('Accuracy Metrics: \n')

print('Accuracy: ', accuracy_score(ytest, pred))

print('Accuracy: ', accuracy_score(ytest, pred))

print('Recall: ', recall_score(ytest, pred))

print('Precision: ', precision_score(ytest, pred))

print('Confusion Matrix: \n', confusion_matrix(ytest, pred))