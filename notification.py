import requests

ignore_list = ['k9yv','w0gmv','wb0zan','wd0emr','wq0p','k0im']
file1 = open('ALL.TXT', 'r')
Lines = file1.readlines()
 
for line in Lines:
    ignore = any(n in line.lower() for n in ignore_list) 
    if not ignore:
        print("Line{}: {}".format(count, line.strip()))
        url = "https://api.simplepush.io/send/Ere7WA/{}".format(line)
        response = requests.request("GET", url)
        print(response.text)
        open('ALL.TXT', 'w')
        break