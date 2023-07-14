import requests, pyshorteners,logging

# Configure the logging module
# logging.basicConfig(filename='logs.txt', format='%(asctime)s - %(levelname)s - %(message)s')

from datetime import datetime

def printr(*args, **kwargs):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_datetime,":", *args, **kwargs)
    # logging.info(formatted_datetime,":", *args, **kwargs)
    # current_datetime = datetime.now()
    # formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    # log_message = f'{formatted_datetime} ' + ' '.join(map(str, args)) + '\n'
    
    # # with open('logs.txt', 'a') as log_file:
    # #     log_file.write(log_message)
    # logging.info(log_message)

def is_amazon_link(long_url):
    if "https://www.amazon.in" in long_url:
        return True
    return False


def expand_short_url(short_url):
    response = requests.head(short_url, allow_redirects=True)
    return response.url


def url_exists(long_url):
    try:
        response = requests.get(long_url)
        if response.status_code < 400:
            return True
    except:
        return False


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

    # if '&' in new_url[::1]:
    #     new_url = new_url.rstrip(new_url[-1])

    tiny_url = short_url(new_url)

    printr('new:',new_url,'tiny:',tiny_url,'long:',long_url)
    return tiny_url
    # if url_exists(new_url):
    #     return new_url
    # else:
    #     return long_url


unrequire_parameters = ["ref","ref_", "red", "tag", "tat", "th", "linkCode", "psc"]


# generate new affiliate url using tiny url api
def parse_url(url,amazon_affiliate_id):
    url_info = {"long": url, "is_amazon_link": False, "updated": url}
    url_info["long"] = expand_short_url(url)
    url_info["is_amazon_link"] = is_amazon_link(url_info["long"])
    if url_info["is_amazon_link"]:
        url_info["updated"] = update_url(url_info["long"], unrequire_parameters,amazon_affiliate_id)
    printr(url_info)
    return url_info


