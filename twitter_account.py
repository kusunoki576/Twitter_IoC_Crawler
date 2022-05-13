from typing import List

from twitter import Tweet, get_userid_from_username, get_tweets
from slack import SlackBot



class TwitterAccount:
    def __init__(self, username: str) -> None:
        username = username.replace('\r', '').replace('\n', '')
        self.username = username
        self.userid:List[int] = get_userid_from_username(username)
        self.tweets:List[Tweet]  = []
        self.slack_bot = SlackBot()
        self.slack_bot.send_start_message(username)
    
    def update_tweets(self, max_results: int = 5) -> None:
        tweets:List[Tweet] = get_tweets(self.userid, max_results, self.tweets)
        for tw in tweets:
            if tw not in self.tweets:
                self.tweets.append(tw)
                if tw.hashes:
                    self.slack_bot.send_detail_message(self.username, tw)