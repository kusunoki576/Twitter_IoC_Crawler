import requests
from typing import List

from virustotal import analyze_virustotal
from re_util import extract_url
from url_util import extract_hash_from_urls

TWITTER_BEARER_TOKEN = 'YOUR TOKEN'
headers = {'Authorization': f'Bearer {TWITTER_BEARER_TOKEN}'}
base_twitter_url = 'https://api.twitter.com/2'



class Tweet:
    def __init__(self, id: int, text: str) -> None:
        self.id = id
        self.text = text
        self.urls:List[str] = [] 
        self.urls.extend(extract_url(self.text))
        self.hashes:List[str] = []
        self.hashes.extend(extract_hash_from_urls(self.urls))

        self.virustotals:List[str] = []
        for hash in self.hashes:
            self.virustotals.append(analyze_virustotal(hash))

    def __eq__(self, other):
        if not isinstance(other, Tweet):
            return NotImplemented
        return self.id == other.id 



def get_userid_from_username(username: str) -> int:
        api_url  = f'{base_twitter_url}/users/by/username/{username}'
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return response.json()['data']['id']
        else:
            return -1

def get_tweets(userid: int, max_results: int) -> List[Tweet]:
        get_tweets:List[Tweet] = []
        api_url  = f'{base_twitter_url}/users/{userid}/tweets'
        params  = {'max_results': max_results}
        response = requests.get(api_url, params=params, headers=headers)
        if response.status_code == 200:
            tweets = response.json()['data']
            for tweet in tweets:
                tw = Tweet(tweet['id'], tweet['text'])
                get_tweets.append(tw)
        return get_tweets