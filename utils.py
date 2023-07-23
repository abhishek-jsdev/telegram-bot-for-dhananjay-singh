import requests, pyshorteners, json, random
from datetime import datetime


API_NAMES = ['compliment','pickup'] #'joke', 'quote'
UNREQUIRED_PARAMETERS = ["ref","ref_", "red", "tag", "tat", "th", "linkCode", "psc"]


def get_affiliate_url(long_url,affiliate_id, UNREQUIRED_PARAMETERS=UNREQUIRED_PARAMETERS):
    long_url_parts = long_url.rsplit("/", 1)
    new_url = long_url_parts[0] + "/"

    query = long_url_parts[1]

    if "?" in query:
        query = query.split("?")
        new_url += query[0] + "?"
        query = query[1]

    array_of_queries = query.split("&")

    for query in array_of_queries:
        key = query.split("=")[0]
        if key in UNREQUIRED_PARAMETERS:
            continue
        new_url += query + "&"

    # add affiliate id
    new_url += "tag=" + affiliate_id

    return new_url


def get_test_response():
    response_text = ''
    random_api_name = random.choice(API_NAMES)


    match random_api_name:

        case 'compliment':
            response_API = requests.get("https://complimentr.com/api")
            response_text= json.loads(response_API.text)['compliment']

        case 'pickup':
            response_API = requests.get('https://vinuxd.vercel.app/api/pickup')
            response_text= json.loads(response_API.text)['pickup']

    return response_text
