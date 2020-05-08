# CoronaTwitterAnalysis
Sentiment Analysis and EDA project on Corona virus outbreak.
## Contributors
Ali Maleki(alimaleki100)[https://alimaleki100.github.io] and Yashar Eskandari(@yasharesk)

## Project Overview
This repo contains works fora personal project on analysis of of tweets about CoronaVirus2019 outbreak.
In this project, we have extracted tweets with Corona search key.
Tweets were clustered and classified to delete Irrelevant tweets.
An EDA and sentiment analysis using textblob were performed on dataset.

## Data Gathering
You can use dataGathering-twint.py script to gather tweets or use twint CLI command:
twint -s corona -o output.csv --csv -l en --unt 2020-04-15 since 2020-01-01
the current tweet sample was gathered by twint CLI command.
The used data set consists 246K tweets with 'corona' keyword since 2020/01/01 until 2020/01/31.

## Data Cleaning
The data cleaning process is accessiblein dataCleaning.py file.

# Results

Word Cloud
![Image of word Cloud](https://github.com/alimaleki100/CoronaTwitterAnalysis/blob/master/images/wordCloud.png)

## Exploratory Analysis

Number of Tweets: 246068

Average of Retweets Count: 5.03

Tweets by Date:
![Image of Tweets by Date](https://github.com/alimaleki100/CoronaTwitterAnalysis/blob/master/images/tweetsByDate.png)

ReTweets by Date:
![Image of ReTweets by Date](https://github.com/alimaleki100/CoronaTwitterAnalysis/blob/master/images/retweetsByDate.png)

Tweets by Hour:
![Image of Tweets by Hour](https://github.com/alimaleki100/CoronaTwitterAnalysis/blob/master/images/tweetsByHour.png)

ReTweets by Hour:
![Image of ReTweets by Hour](https://github.com/alimaleki100/CoronaTwitterAnalysis/blob/master/images/RetweetsByHour.png)


## Sentiment Analysis

Polarity and Subjectivity Chart:
![Image of Polarity and Subjectivity](https://github.com/alimaleki100/CoronaTwitterAnalysis/blob/master/images/polarity.subjectivity.png)




Polarity Pie Chart:

![Image of Polarity Pie Chart](https://github.com/alimaleki100/CoronaTwitterAnalysis/blob/master/images/polarityPie.png)




Polarity Line Chart:

![Image of Polarity Line Chart](https://github.com/alimaleki100/CoronaTwitterAnalysis/blob/master/images/PolarityLineChart.png)



