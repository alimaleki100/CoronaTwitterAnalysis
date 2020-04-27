# -- coding: utf-8 --
"""
Created on Sun Jan 26 14:32:39 2020

@author: alimaleki100
"""


import pandas as pd
import numpy as np
import re
import string
from nltk.stem.porter import *
import nltk 

import matplotlib.pyplot as plt
#from textblob import TextBlob


userpattern="@[\w]*"
RTpattern="RT"
urlpattern="https://[\w]*"
stopword = nltk.corpus.stopwords.words('english')
def remove_pattern(input_txt, userpattern,RTpattern,urlpattern):
    r = re.findall(userpattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    RT = re.findall(RTpattern, input_txt)
    for i in RT:
        input_txt = re.sub(i, '', input_txt)
    url = re.findall(urlpattern, input_txt)
    for i in url:
        input_txt = re.sub(i, '', input_txt)          
        
    return input_txt

def remove_stopwords(text):
    text = [word for word in text if word not in stopword]
    return text

def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text

def remvove_nonASCII(text):
    return ''.join([w if ord(w) < 128 else ' ' for w in text])

df=pd.read_csv("C:/Users/Ali/Desktop/CoronaProject/tweetCoronaJan2020.csv")
print(df['tweet'].head())


#Remove @user and RT pattern
df['tidy_text'] = np.vectorize(remove_pattern)(df['tweet'], userpattern,RTpattern,urlpattern)

#Remove Punctuation
df['tidy_text'] = df['tidy_text'].apply(lambda x: remove_punct(x))

#Remove non ASCII chars
df['tidy_text']  = df['tidy_text'].apply(lambda x: remvove_nonASCII(x))


#Tokenize Texts
df['tokenized_text']  = df['tidy_text'].apply(lambda x: x.split())

#Remove Stop Words
df['tokenized_text']  = df['tokenized_text'].apply(lambda x: remove_stopwords(x))


# Stemming ( Removing ing, ly, es ,s)
stemmer = PorterStemmer()
df['tokenized_text']  = df['tokenized_text'] .apply(lambda x: [stemmer.stem(i) for i in x]) # stemming
df['tokenized_text'] .head()




writer=pd.ExcelWriter("C:/Users/ali/Desktop/CoronaProject/CleanedCoronaVirus.xlsx",engine='xlsxwriter')
df.to_excel(writer, sheet_name='new')
writer.close()




#stitch these tokens back together.

