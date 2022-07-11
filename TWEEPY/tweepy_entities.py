#extraccion de entidades de tweets que contienen la palabra eerr

from html import entities
import tweepy
import configparser
import pandas as pd
import datetime
import pytz
from tweepy import OAuthHandler

#leer credenciales
config = configparser.ConfigParser()
config.read('config.ini')

api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
api_key_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#autenticacion
auth = OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

keywords = 'eerr lang:es'
limit = 20

tweets = tweepy.Cursor(api.search_tweets, q=keywords, tweet_mode='extended').items(limit)

columns = ["Entities"]
data = []
for tweet in tweets:
    data.append(entities)

df = pd.DataFrame(data, columns=columns) 
print (df)
df.to_csv('tweets_entities.csv')