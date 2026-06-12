import requests

def get_data():
    url = "https://app.ticketmaster.com/discovery/v2/events.json?keyword=  &apikey=k8uIxpExADo58NKAHY6GocJmR9iI5Amz"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(response.status_code)

get_data()