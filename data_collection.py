# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:47:44 2020

@author: Ken
"""

import glassdoor_scraper as gs 
import pandas as pd 

path = "files/chromedriver"

df = gs.get_jobs('data scientist',1000, path, 4)

df.to_csv('glassdoor_jobs.csv', index = False)