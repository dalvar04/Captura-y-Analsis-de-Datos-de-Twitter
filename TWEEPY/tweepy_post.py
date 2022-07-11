#ejemplo para la publicacion de tweets con Tweepy (faltan permisos)

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

"""
#escribir un tweet
api.update_status("Tweet de prueba")


#escribir un comentario a un tweet
texto = "Respuesta a un tweet"
api.update_status(texto, in_reply_to_status_id="1141453669541584897")


#escribir un tweet con imagen
data_img = api.media_upload("./imagen.png")
print data_img

api.update_status("tweet con imagen", media_ids=["id de la imagen"])
"""
