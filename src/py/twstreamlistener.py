import tweepy
import requests

#override tweepy.StreamListener to add logic to on_status
class TwStreamListener(tweepy.StreamListener):
    def __init__(self):
        super(TwStreamListener, self).__init__()
        #initializes the counter
        self.counter = 0

    def on_status(self, status):
        print(status.text)
        if 'transfer' in status.text:
            print "transfer"
            url='http://127.0.0.1:3001/sendValue?f=0xf69fc8a0aa6b2d0f3bafa7d40ee501a788b0d65e&p=ed19d0e3fc1e8d3bb92389bf993943949c6c96f17f4bf506bb0b5c5194ee780b&t=0x2dfce98b4ec6a9e8b719c96b8b21cb75bf0c82d7&a=1000'
            response = requests.get(url)
            print response

        return True


    def on_warning(self, notice):
        print('WARNING:' + str(notice.message))
        return

    def on_exception(self, exception):
        print('EXCEPTION:' + str(exception))
        return

    def on_error(self, status_code):
        print('ERROR: ' + str(status_code))
        return True

    def on_connect(self):
        print('CONNECTED')
        return

    def on_disconnect(self, notice):
        print('DISCONNECTED:' + str(notice.code))
        return
