import requests, pyshorteners,json
from datetime import datetime

def printr(*args, **kwargs):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_datetime,":", *args, **kwargs)
    
    with open('logs/logs.txt', 'a') as log_file:
        print(formatted_datetime,":", *args, **kwargs,file=log_file)

unrequire_parameters = ["ref","ref_", "red", "tag", "tat", "th", "linkCode", "psc"]


def get_affiliate_url(long_url,affiliate_id, unrequire_parameters=unrequire_parameters):
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
        if key in unrequire_parameters:
            continue
        new_url += query + "&"

    # add affiliate id
    new_url += "tag=" + affiliate_id

    return new_url
