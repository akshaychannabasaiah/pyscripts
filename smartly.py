import requests
base_url = 'http://fasttrack.herokuapp.com'
next = ''
try:
    while(True):

        print('next2' + next)
        headers = {'Accept':'application/json'}
        url = base_url + next
        r = requests.get(url, headers=headers)
        print(r.text)
        next = r.json()['next'] 
        print('next2' + next)
finally:
    print("Get on with the next step")
