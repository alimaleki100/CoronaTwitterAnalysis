# -- coding: utf-8 --
"""
Created on Sun Jan 26 14:32:39 2020

@author: alimaleki100
"""



import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob


sentidfColumns=['text','polarity','subjectivity','sentiment']

sentidf=pd.DataFrame(columns=sentidfColumns)

df=pd.read_excel("C:/Users/ali/Desktop/CoronaProject/CleanedCoronaVirus.xlsx")
print(df)



#sentiment_objects = df['tokenized_text']

sentiment_objects = [TextBlob(tweet) for tweet in df['tokenized_text']]

#sentiment_objects.polarity, sentiment_objects.subjectivity

sentiment_values = [[tweet.sentiment.polarity,tweet.sentiment.subjectivity, str(tweet)] for tweet in sentiment_objects]

sentiment_values[0]


sentiment_df = pd.DataFrame(sentiment_values, columns=["polarity",'subjectivity', "tweet"])


#adding date to sentiment df
sentiment_df['date']=df['date']


def pol(p):
    if p > 0:
        return 'Positive'
    elif p < 0:
        return 'Negative'
    else:
        return 'Neutral'
sentiment_df['sentiment'] = sentiment_df.polarity.apply(lambda x: pol(x))


polAvgdf=sentiment_df.groupby('date').mean().reset_index()

polAvgdf.plot.line(subplots=True)
polAvgdf.plot.line(x='date',y='polarity')
#Sentiment Pie Plot
sentiment_df.sentiment.value_counts(sort=False).plot.pie()
plt.show()

polAvgdf.plot.line()
polAvgdf.plot.line(x='date',y='polarity')


fig, ax = plt.subplots(figsize=(8, 6))

# Plot histogram of the polarity values
sentiment_df.hist(
             ax=ax,
             color="purple")


plt.show()



writer=pd.ExcelWriter("C:/Users/ali/Desktop/CoronaProject/sentimentdf.xlsx",engine='xlsxwriter')
sentiment_df.to_excel(writer, sheet_name='new')
writer.close()


