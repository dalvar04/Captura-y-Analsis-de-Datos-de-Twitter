import requests
import os
import json

# To set your environment variables in your terminal run the following line:
BEARER_TOKEN ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
bearer_token = os.environ.get(BEARER_TOKEN)

#endpoint para la busqueda de datos sobre una encuesta
search_url = "https://api.twitter.com/2/tweets?ids=1199786642791452673&expansions=attachments.poll_ids&poll.fields=duration_minutes,end_datetime,id,options,voting_status"

#todos los posibles datos que se pueden aportar sobre una encuesta
# expansions=attachments.poll_ids&poll.fields=duration_minutes,end_datetime,id,options,voting_status'
query_params = ""


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
    with open('json/poll_data.json', 'w') as outfile:
        json.dump(json_response, outfile)


if __name__ == "__main__":
    main()