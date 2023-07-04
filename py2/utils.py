import requests, pyshorteners

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

    new_url = short_url(new_url)

    if url_exists(new_url):
        return new_url
    else:
        return long_url


unrequire_parameters = ["ref","ref_", "red", "tag", "tat", "th", "linkCode", "psc"]


# generate new affiliate url using tiny url api
def parse_url(url,amazon_affiliate_id):
    url_info = {"long": url, "is_amazon_link": False, "updated": url}
    url_info["long"] = expand_short_url(url)
    url_info["is_amazon_link"] = is_amazon_link(url_info["long"])
    if url_info["is_amazon_link"]:
        url_info["updated"] = update_url(url_info["long"], unrequire_parameters,amazon_affiliate_id)
    return url_info

# def get_url_info2(url):
#     url_info = {"long": url, "is_amazon_link": False, "updated": url}

#     # expand url if shortened
#     response = requests.head(short_url, allow_redirects=True)
#     url_info["long"] =response.url
    
#     # is amazon link
#     if "https://www.amazon.in" in url_info["long"]:
#         url_info["is_amazon_link"]=True
    
#     # generate new url
#     if url_info["is_amazon_link"]:
#         url_info["updated"] = update_url(url_info["long"], unrequire_parameters)
    
#     return url_info
# # Test
# urls = [
#     "https://www.amazon.in/b?ie=UTF8&node=77323998031&ref=ebd",
#     "https://www.amazon.in/s?k=menhood+grooming+trimmer&red=ebd&sprefix=menhood+%2Caps%2C1448&ref=ebd",
#     "https://www.amazon.in/deal/9641fee6?showVariations=true&ref_=cm_sw_r_api_dlpg_oH7y7fmMLOV3q&ref=ebd",
#     "https://www.amazon.in/dp/B076Q1NVQV/ref=ebd",
#     "https://www.amazon.in/s?me=A1SU155JFG0BDG&marketplaceID=A21TJRUUN4KGV&ref=ebd",
#     "https://www.amazon.in/dp/B0C4T91SNK?linkCode=sl1&th=1&psc=1&tag=ozians06-21",
#     "https://www.amazon.in/dp/B0C4T91SNK?linkCode=sl1&th=1&psc=1&tag=ozians06-21&tat=1",
# ]

# for url in urls:
#     info = get_url_info(url)
#     # print(url)
#     print(info)
#     print()
