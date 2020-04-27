# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 01:26:10 2020

@author: Yashar
"""

import twint


c = twint.Config()

#c.Username = "noneprivacy"
#c.Custom["tweet"] = ["id"]
#c.Custom["user"] = ["bio"]
#c.Limit = 10
c.Custom_query = "corona OR coronavirus"
c.Store_csv = True
c.Output = 'firstRun.csv'
c.Resume = 'firstRune.csv'
c.Pandas_clean = True
c.Since = '2020-01-01'
c.Until= '2020-04-15'
c.Pandas = True
#c.Pandas_type = 'DataFrame'
c.Pandas_au = True
c.Lang = 'en'
#c.Limit = 10
twint.run.Search(c)

result = twint.storage.panda.Tweets_df
