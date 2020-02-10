# -- coding: utf-8 --
"""
Created on Sun Jan 26 14:32:39 2020

@author: alimaleki100
"""


import tweepy as tp
import pandas as pd
import numpy as np
import re
import string
from nltk.stem.porter import *
import matplotlib.pyplot as plt
from textblob import TextBlob


userpattern="@[\w]*"
RTpattern="RT"
def remove_pattern(input_txt, userpattern,RTpattern):
    r = re.findall(userpattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    RT = re.findall(RTpattern, input_txt)
    for i in RT:
        input_txt = re.sub(i, '', input_txt)        
        
    return input_txt



def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text


df=pd.read_excel("C:/Users/session1/Desktop/CoronaVirus21.xlsx")
print(df['text'].head())


#Remove @user and RT pattern

df['tidy_text'] = np.vectorize(remove_pattern)(df['text'], userpattern,RTpattern)


#Remove Punctuation
df['tidy_text'] = df['tidy_text'].apply(lambda x: remove_punct(x))

#Tokenize Texts
df['tokenized_text']  = df['tidy_text'].apply(lambda x: x.split())



# Stemming ( Removing ing, ly, es ,s)
stemmer = PorterStemmer()
df['tokenized_text']  = df['tokenized_text'] .apply(lambda x: [stemmer.stem(i) for i in x]) # stemming
df['tokenized_text'] .head()



writer=pd.ExcelWriter('C:/Users/session1/Desktop/CleanedCoronaVirus.xlsx',engine='xlsxwriter')
df.to_excel(writer, sheet_name='new')
writer.close()
    
