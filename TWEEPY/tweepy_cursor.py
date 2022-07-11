#prueba de funcionamiento del metodo cursor

import tweepy
import configparser
import pandas as pd
import json
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

# Iniciamos un array que va a contener los datos
simple_list = []
# Iniciamos el for con Cursor
# Usamos algunos parámetros extra para excluir respuestas, retweets y traer el texto completo de cada tweet
for status in tweepy.Cursor(api.user_timeline, screen_name = "unileon", exclude_replies = True, include_rts = False, tweet_mode="extended").items(5):
# Agregamos el texto, fecha, likes, retweets y hashtags al array
    simple_list.append([status.full_text, status.created_at, status.favorite_count, status.retweet_count, [h["text"] for h in status.entities["hashtags"]]])
# Convertimos el array en un DataFrame y nombramos las columnas
simple_list = pd.DataFrame(simple_list, columns=["Text", "Created at", "Likes", "Retweets", "Hashtags"])
# Guardamos en el directorio en que estamos trabajando
simple_list.to_csv("test_cursor_tweepy.csv")


