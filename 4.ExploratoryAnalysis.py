

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 17:10:34 2020
@author: alimaleki100
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from os import path
from PIL import Image
#import seaborn as sns




df=pd.read_excel("C:/Users/ali/Desktop/CoronaProject/CleanedCoronaVirus.xlsx")


def HandleDateTime(inputdf):
    inputdf['tweet_datetime']=pd.to_datetime(inputdf['date'])
    #inputdf['WeekDay']=inputdf['tweet_datetime'].dt.day()
    inputdf['MonthName']=inputdf['tweet_datetime'].dt.month_name()
    inputdf['Month']=inputdf['tweet_datetime'].dt.month
    inputdf['hour']=inputdf['time'].str[:2]
    #inputdf['day']=inputdf['tweet_datetime'].strftime("%A")
  
    return inputdf


df=HandleDateTime(df)

#Average of Retweets Counts
print(df['retweets_count'].mean())

#Count of tweets by Date
date_gdf=df.groupby(['date']).size()
date_gdf.plot.line(x='0',title='Count of tweets by Date')

#Sum of Retweets by Day
retweet_day_gdf=df.groupby(['date'])['retweets_count'].sum()
retweet_day_gdf.plot.line(x='retweets_count',title='Sum of Retweets by Date')


#Count of tweets by Hour
hour_gdf=df.groupby(['hour']).size()
hour_gdf.plot.line(x='0',title='Count of tweets by Hour')

#Sum of Retweets by Hour
retweet_hour_gdf=df.groupby(['hour'])['retweets_count'].sum()
retweet_hour_gdf.plot.line(x='retweets_count',title='Sum of Retweets by Hour')







#WordCloud
from wordcloud import WordCloud

#twittermask = np.array(Image.open(path.join("tw2.png")))
wordcloud = WordCloud(background_color="black", contour_color='steelblue',width=1800, height=1400, max_font_size=110).generate(str(df['tokenized_text']))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow( cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.savefig('./my_twitter_wordcloud_2.png', dpi=300)

