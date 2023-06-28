import urllib.parse as urlparse
url = "http://www.example.com?type=a&type1=b&type2=c"
# trigger = ["'or '1'='1'"," 'OR '1'='2'","'OR a=a"]

parsed = urlparse.urlparse(url)
querys = parsed.query.split("&")
result = []
# for pairs in trigger:
#     new_query = "&".join([ "{}{}".format(query, pairs) for query in querys])
#     parsed = parsed._replace(query=new_query)
#     print(urlparse.urlunparse(parsed))
#     result.append(urlparse.urlunparse(parsed))

# print(result)

# url="https://www.amazon.in/dp/B0C4T91SNK?linkCode=sl1&th=1&psc=1&tag=ozians06-21"

# from urllib.parse import urlparse, urlunparse
# # url = 'https://www.google.com/search?q=python'
# parsed_url = urlparse(url)
# # Change the value of the `q` parameter
# params = parsed_url.query.split('&')
# for param in params:
#     param=param.split('=')
#     value=param[1]
#     param=param[0]
#     # if(param=='tag')
# # parsed_url.query['tag'] = ['nnew value']
# # Delete the `q` parameter
# # del parsed_url.query['ref_']
# # Convert the `ParseResult` object back into a URL
# new_url = urlunparse(parsed_url)
# print(new_url)

# # a=url.split('?')
# # b= [a[0]]
# # b.extend(a[1].split('&'))
# # print(b)

# # delete_params=['ref','red','ref_','tag']

# # c=''
# # for item in b:
# #     items = item.split('=')
# #     if items.length > 1:
# #         print(items[0])