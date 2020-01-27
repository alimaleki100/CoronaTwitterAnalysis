# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 00:26:57 2020

@author: Yashar
"""

import pandas as pd
import git.DataCleaning.Libs as libs
import ast
df = pd.read_excel(libs.getFileName()["CompleteFile"])
#%%
dfl = df[df.coordinates.notnull()]
dfl['coor'] = dfl.coordinates.apply(lambda x: ast.literal_eval(x)["coordinates"])
