import requests

ignore_list = ['k9yv','w0gmv','wb0zan','wd0emr','wq0p','k0im','n1ccc']
file1 = open('ALL.TXT', 'r')
Lines = file1.readlines()
 
for line in Lines:
    ignore = any(n in line.lower() for n in ignore_list) 
    if not ignore:
        payload = {'message': line, 'user': '', 'token': '' }
        r = requests.post('https://api.pushover.net/1/messages.json', data=payload, headers={'User-Agent': 'Python'})
        open('ALL.TXT', 'w')
        break