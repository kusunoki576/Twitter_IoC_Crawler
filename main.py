# The following codes includes codes from the book Cyber Security Programming.

from typing import List
import time

from twitter_account import TwitterAccount


twitter_list:List[TwitterAccount] = []
usernames = open('accountlist.txt', 'r').readlines()
for user in usernames:
    twitter_list.append(TwitterAccount(user))

while True:
    for twitter in twitter_list:
        twitter.update_tweets(5)
    print("===== sleeping =====")
    time.sleep(3600)