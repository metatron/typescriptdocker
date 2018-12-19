import tweepy
#override tweepy.StreamListener to add logic to on_status
class TwStreamListener(tweepy.StreamListener):
    def __init__(self):
        return

    def on_status(self, status):
        print(status.text)
