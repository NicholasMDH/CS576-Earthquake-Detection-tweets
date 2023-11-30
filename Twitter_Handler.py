import tweepy
from auth import (
    api_key,
    api_secret,
    access_token,
    bearer_token,
    access_token_secret
)


class Twitter_Handler(object):

    client: tweepy.Client
    api: tweepy.API

    def __init__(self):
        self.client = tweepy.Client(
            bearer_token,
            api_key,
            api_secret,
            access_token,
            access_token_secret
        )
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def send_tweet(self, message):
        self.client.create_tweet(text = message)

# FOR TESTING ONLY
if __name__ == '__main__':
    twitter = Twitter_Handler()
    twitter.send_tweet("Hello")
# ================