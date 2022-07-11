#busqueda de los ultimos 20 tweets escritos por la cuenta @unileon

import tweepy
import configparser
import pandas as pd
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

api = tweepy.API(auth)

user = 'unileon'
limit = 20

tweets = tweepy.Cursor(api.user_timeline,screen_name=user, count=limit, tweet_mode='extended').items(limit)

columns = ['Hora y Dia', "Usuario", "Tweet"]
data = []
for tweet in tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns) 
print (df)
df.to_csv('tweets_user.csv')