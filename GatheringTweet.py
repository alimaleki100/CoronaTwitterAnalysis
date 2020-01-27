# -- coding: utf-8 --
"""
Created on Sun Jan 26 14:32:39 2020

@author: alimaleki100
"""


import tweepy as tp
import pandas as pd



access_token='46845259-aFZybrNn3gTgBCcvbxo3uVkuopgRK9Lx3zg43xoEd'
access_token_secret='M4nJxQ6nfB1AXEjsn1zkC62tOH9haQG0rDZAOd0PZaB9a'
apiKey='34oHUFxZ8WvnzthuJ010BGPgW'
apiSecretKey='2XUUm5vz54b9UcjXqBYf0oRYwwW5r860NLVCSIKRS85Fcgc7F7'

# Creating the authentication object
auth = tp.OAuthHandler(apiKey, apiSecretKey)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tp.API(auth,wait_on_rate_limit=True) 

dfcolumns=['coordinates','source','text','lan','screen_name','userlocation','place','retweetCount','created_at','id','userName',
           'in_reply_to_status_id','in_reply_to_status_id_str','in_reply_to_user_id','in_reply_to_user_id_str',
           'in_reply_to_screen_name','user.id_str','user.created_at','user.geo_enabled','favorite_count','retweet_count','entities']

""""
coordinates.coordinates
place.bounding_box.coordinates
place.country
place.country_code
place.full_name
place.id
place.name
place.type
"""

tweets = tp.Cursor(api.search,
              q='corona',
                           since = "2020-01-25",
                           until = "2020-01-26").items()


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
             tweet.entities] for tweet in tweets]


tweetdf=pd.DataFrame(data=tweet_data,columns=dfcolumns)
writer=pd.ExcelWriter("C:/Users/session1/Desktop/CoronaVirus24.xlsx",engine='xlsxwriter')
tweetdf.to_excel(writer, sheet_name='new')
writer.close()

