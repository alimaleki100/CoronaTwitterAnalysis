# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 17:10:34 2020

@author: alimaleki100
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from textblob import TextBlob
from os import path
from PIL import Image
import seaborn as sns




df=pd.read_excel("C:/Users/session1/Desktop/CleanedCoronaVirus.xlsx")


def HandleDateTime(inputdf):
    inputdf['tweet_datetime']=pd.to_datetime(inputdf['created_at'])
    inputdf['WeekDay']=inputdf['tweet_datetime'].dt.weekday_name
    inputdf['MonthName']=inputdf['tweet_datetime'].dt.month_name
    inputdf['Month']=inputdf['tweet_datetime'].dt.month
    inputdf['hour']=inputdf['tweet_datetime'].dt.hour
  
    return inputdf


df=HandleDateTime(df)



sns.countplot(x='airline_sentiment', data=tweets)








#WordCloud
from wordcloud import WordCloud

twittermask = np.array(Image.open(path.join("tw2.png")))
wordcloud = WordCloud(background_color="black", contour_color='steelblue',width=1800, height=1400,mask=twittermask, max_font_size=110).generate(str(df['tokenized_text']))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(twittermask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.savefig('./my_twitter_wordcloud_2.png', dpi=300)

print(df['tokenized_text'].head())



#stitch these tokens back together.
