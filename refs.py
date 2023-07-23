def printr(*args, **kwargs):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_datetime,":", *args, **kwargs)

    with open('logs/logs.txt', 'a') as log_file:
        print(formatted_datetime,":", *args, **kwargs,file=log_file)


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
