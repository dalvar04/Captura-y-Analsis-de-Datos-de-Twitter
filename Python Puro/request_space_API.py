import requests
import os
import json

# To set your environment variables in your terminal run the following line:
BEARER_TOKEN ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
bearer_token = os.environ.get(BEARER_TOKEN)

#endpoint para la busqueda de datos sobre un espacio de twitter
search_url = "https://api.twitter.com/2/spaces/1DXxyRYNejbKM?space.fields=created_at,creator_id"

# todos los posibles datos que se pueden aportar sobre un espacio de twitter
# space.fields=created_at,creator_id,created_athost_ids,lang,is_ticketed,invited_user_ids,participant_count,scheduled_start,speaker_ids,started_at,state,title,updated_at&expansions=creator_id,host_ids,invited_user_ids,speaker_ids"
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
    with open('json/space_data.json', 'w') as outfile:
        json.dump(json_response, outfile)


if __name__ == "__main__":
    main()