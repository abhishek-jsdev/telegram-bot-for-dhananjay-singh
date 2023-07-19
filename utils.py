import requests, pyshorteners,json
from datetime import datetime

def printr(*args, **kwargs):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_datetime,":", *args, **kwargs)
    
    with open('logs/logs.txt', 'a') as log_file:
        print(formatted_datetime,":", *args, **kwargs,file=log_file)


def expand_short_url(short_url):
    response = requests.head(short_url, allow_redirects=True)
    return response.url


def short_url(long_url):
    # TinyURL shortener service
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    return short_url


def update_url(long_url, unrequire_parameters,affiliate_id):
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

    return short_url(new_url)


unrequire_parameters = ["ref","ref_", "red", "tag", "tat", "th", "linkCode", "psc"]


# generate new affiliate url using tiny url api
def parse_url(url,amazon_affiliate_id):
    url_info = {"long": url, "is_amazon_link": False, "updated": url}
    
    url_info["long"] = expand_short_url(url)

    url_info["is_amazon_link"] = "https://www.amazon.in" in url_info["long"]
    
    if url_info["is_amazon_link"]:
        url_info["updated"] = update_url(url_info["long"], unrequire_parameters,amazon_affiliate_id)
    printr(url_info)
    return url_info


def get_compliment():
    response_API = requests.get("https://complimentr.com/api")
    return json.loads(response_API.text)['compliment']