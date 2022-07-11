#busqueda de tweets que contienen las palabras clave relacionadas con las EERR en el mes de Febrero con Python Puro

from ast import keyword
import requests
import os
import json

# To set your environment variables in your terminal run the following line:
BEARER_TOKEN ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
bearer_token = os.environ.get(BEARER_TOKEN)

search_url = "https://api.twitter.com/2/tweets/search/all?tweet.fields=attachments,author_id,context_annotations,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,source,text,withheld&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld&expansions=author_id"
start_date = ["2022-02-01T00:00:00.000Z"]
end_date = ["2022-03-01T00:00:00.000Z"]

query_params = {'query': 'enfermedadesraras OR enfermedadrara OR eerr OR enfermedadeshuerfanas OR enfermedadhuerfana OR enfermedadesminoritarias OR enfermedadminoritaria OR enfermedadespococomunes OR enfermedadpococomun OR enfermedadespocofrecuentes OR enfermedadpocofrecuente OR enfermedaddebajaprevalencia OR enfermedadesdebajaprevalencia OR "enfermedades raras" OR "enfermedad rara" OR "enfermedades huerfanas" OR "enfermedad huerfana" OR "enfermedades minoritarias" OR "enfermedad minoritaria" OR "enfermedades poco comunes" OR "enfermedad poco comun" OR "enfermedades poco frecuentes" OR "enfermedad poco frecuente" OR "enfermedad de baja prevalencia" OR "enfermedades de baja prevalencia" lang:es',
                'start_time' : start_date,
                'end_time' : end_date,
                'max_results':100
                }


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))
    with open('json/EERR/eerr_api.json', 'w') as outfile:
        json.dump(json_response, outfile)


if __name__ == "__main__":
    main()