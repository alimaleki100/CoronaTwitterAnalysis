# -- coding: utf-8 --
"""
Created on Sun Jan 26 14:32:39 2020

@author: alimaleki100
"""


import pandas as pd
import numpy as np
import re
import string




userpattern="@[\w]*"
RTpattern="RT"
urlPattern="https://[\w]*"
def remove_pattern(input_txt, userpattern,RTpattern):
    r = re.findall(userpattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    RT = re.findall(RTpattern, input_txt)
    for i in RT:
        input_txt = re.sub(i, '', input_txt)        

    return input_txt

#Remove URL
def remove_urls (vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return(vTEXT)

def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text


df=pd.read_csv("F:/Github/CoronaTwitterAnalysis/CoronaTwitter/secondRun.csv")
print(df['tweet'].head())


#Remove @user and RT

df['tidy_text'] = np.vectorize(remove_pattern)(df['tweet'], userpattern,RTpattern)

#Remove URL
df['tidy_text']=df['tidy_text'].apply(lambda x: remove_urls(x))


#Remove Punctuation
df['tidy_text'] = df['tidy_text'].apply(lambda x: remove_punct(x))

#Tokenize Texts
df['tokenized_text']  = df['tidy_text'].apply(lambda x: x.split())



# Stemming ( Removing ing, ly, es ,s)
stemmer = PorterStemmer()
df['tokenized_text']  = df['tokenized_text'] .apply(lambda x: [stemmer.stem(i) for i in x]) # stemming
df['tokenized_text'] .head()

df['datetime']=df['date'] +' '+ df['time']

df['datetime'] = pd.DatetimeIndex(df['datetime'])



df.dtypes




writer=pd.ExcelWriter('F:/Github/CoronaTwitterAnalysis/CoronaTwitter/CleanedCoronaVirus.xlsx',engine='xlsxwriter')
df.to_excel(writer, sheet_name='new')
writer.close()
    
