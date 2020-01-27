# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:59:09 2020

@author: Yashar
"""
import pandas as pd
import tweepy

access_token='46845259-aFZybrNn3gTgBCcvbxo3uVkuopgRK9Lx3zg43xoEd'
access_token_secret='M4nJxQ6nfB1AXEjsn1zkC62tOH9haQG0rDZAOd0PZaB9a'
apiKey='34oHUFxZ8WvnzthuJ010BGPgW'
apiSecretKey='2XUUm5vz54b9UcjXqBYf0oRYwwW5r860NLVCSIKRS85Fcgc7F7'

# Creating the authentication object
auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth,wait_on_rate_limit=True) 


searched_tweets = []
max_tweets = 100
last_id = -1
c = 0
while len(searched_tweets) < max_tweets:
    count = max_tweets - len(searched_tweets)
    try:
        new_tweets = api.search(q='corona', count=count, max_id=str(last_id - 1))
        if not new_tweets:
            break
        searched_tweets.extend(new_tweets)
        c = c + 1
        print(c)
        last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        # depending on TweepError.code, one may want to retry or wait
        # to keep things simple, we will give up on an error
        print(e)
        break

tweet_data=[[tweet.coordinates,
             tweet.source,
             tweet.text,
             tweet.user.lang,
             tweet.user.screen_name,
             tweet.user.location,
             tweet.place,
             tweet.retweet_count,
             tweet.created_at,
             tweet.user.id,
             tweet.user.name,
             tweet.in_reply_to_status_id,
             tweet.in_reply_to_status_id_str,
             tweet.in_reply_to_user_id,
             tweet.in_reply_to_user_id_str,
             tweet.in_reply_to_screen_name,
             tweet.user.id_str,
             tweet.user.created_at,
             tweet.user.geo_enabled,
             tweet.favorite_count,
             tweet.retweet_count,
             tweet.entities] for tweet in new_tweets]    