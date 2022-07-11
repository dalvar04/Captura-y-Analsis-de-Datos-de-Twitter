#busqueda de los 100 tweets mas recientes que contienen las palabras indicadas con sus respectivos datos

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

keywords = 'enfermedadesraras OR enfermedadrara OR eerr OR "enfermedades raras" OR "enfermedad rara" OR "enfermedades poco comunes"'
limit = 100

tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=limit, tweet_mode='extended').items(limit)

columns = ["ID", "Texto", "Fecha", "Dispositivo", "Retweets", "Favoritos","Geo","Idioma", "Tweet original", "Nombre pantalla", "Nombre User","Bio", "Verificado", "Alta en Twitter", "Seguidores", "Seguidos", "Numero de Tweets"]
data = []
for tweet in tweets:
    data.append([tweet.id , tweet.full_text, tweet.created_at, tweet.source, tweet.retweet_count, tweet.favorite_count, tweet.geo, tweet.lang, tweet.in_reply_to_status_id, tweet.user.screen_name, tweet.user.name, tweet.user.description, tweet.user.verified, tweet.user.created_at, tweet.user.followers_count, tweet.user.friends_count, tweet.user.statuses_count])

df = pd.DataFrame(data, columns=columns) 
print (df)
df.to_csv('tweets_eerr.csv')


