import tweepy
#override tweepy.StreamListener to add logic to on_status
class TwStreamListener(tweepy.StreamListener):
    def __init__(self):
        super(TwStreamListener, self).__init__()
        #initializes the counter
        self.counter = 0

    def on_status(self, status):
        print(status.text)
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
