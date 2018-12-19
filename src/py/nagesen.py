import tweepy
from twstreamlistener import TwStreamListener


Consumer_key = 'UyAIOxvesKKY2UG15UTh6q4qA'
Consumer_secret = '0YCYlkj7QHdmhgxlk71SBS6aAuq3GG33ipLbdFI5JBVnuDbzKV'
Access_token = '3107466672-NIXkhTHiSsFce5e8QbePWnAx67nWpjgczyGRFka'
Access_secret = '20sjAydS12nSv3L68cTYwKgmjnAlttJokMhuo1LFQ7UBA'

auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_token, Access_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

twStreamListener = TwStreamListener()
twStream = tweepy.Stream(auth = api.auth, listener=twStreamListener)
twStream.filter(track=['python'])
