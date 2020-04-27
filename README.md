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
## Sentiment Analysis

Polarity and Subjectivity Chart:
![Image of Polarity and Subjectivity](https://github.com/alimaleki100/CoronaTwitterAnalysis/blob/master/images/polarity.subjectivity.png)




Polarity Pie Chart:

![Image of Polarity Pie Chart](https://github.com/alimaleki100/CoronaTwitterAnalysis/blob/master/images/PolarityPie.png)







