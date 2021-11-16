import requests
import json
import os
import collections


CLIENT_ID = os.environ.get('CLIENT_ID')
SECRET_KEY = os.environ.get('SECRET_KEY')
USERNAME = os.environ.get('REDDIT_USERNAME')
PASSWORD = os.environ.get('REDDIT_PASSWORD')


def call_api(CLIENT_ID, SECRET_KEY, USERNAME, PASSWORD):
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

    data = {'grant_type': 'password',
            'username': USERNAME,
            'password': PASSWORD}

    # setup our header info, which gives reddit a brief description of our app
    headers = {'User-Agent': 'red_assistant/0.0.1'}

    # send our request for an OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    # convert response to JSON and pull access_token value
    TOKEN = res.json()['access_token']

    # add authorization to our headers dictionary
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    return requests.get("https://oauth.reddit.com/r/askcarsales/hot", headers=headers)

def parse_text(data):
    text_votes = {}

    for post in data.json()['data']['children']:
        text_votes[post['data']['ups']] = post['data']['selftext']

    od_text_votes = collections.OrderedDict(sorted(text_votes.items(), reverse=True))
    return list(od_text_votes.items())[0]


if __name__ == '__main__':
    data = call_api(CLIENT_ID, SECRET_KEY, USERNAME, PASSWORD)
    print(parse_text(data))
