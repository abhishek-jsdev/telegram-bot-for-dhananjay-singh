import requests, pyshorteners, json, random
from datetime import datetime


from strings import API_NAMES


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


def get_test_response():
    response_text = ''
    random_api_name = random.choice(API_NAMES)
        

    match random_api_name:
            
        case 'compliment':
            response_API = requests.get("https://complimentr.com/api")
            response_text= json.loads(response_API.text)['compliment']
            
        # case 'quote':
        #     response_API = requests.get("https://api.quotable.io/quotes/random")
        #     response_text = json.loads(response_API.text)[0]
        #     response_text = response_text['content'] +'\n~'+response_text['author']
        
        # case 'joke':
        #     response_API = requests.get("https://official-joke-api.appspot.com/jokes/random")
        #     response_text = json.loads(response_API.text)
        #     response_text = response_text['setup'] +'\n\n'+response_text['punchline']
        
        case 'pickup':
            response_API = requests.get('https://vinuxd.vercel.app/api/pickup')
            response_text= json.loads(response_API.text)['pickup']
         
    return response_text