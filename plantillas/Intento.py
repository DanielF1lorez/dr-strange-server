import tweepy
import Certificacion

class TweetsListener (tweepy.StreamListener):

 def on_connect(self):
     print ("Elon Musk esta conectado!")

 def on_status(self, status):
     
     print ("El ultimo twitt de Musk es:", status.text)

auth = tweepy.OAuthHandler(Certificacion.API_KEY, Certificacion.API_SECRET_KEY)

auth.set_access_token(Certificacion.ACCES_TOKEN, Certificacion.ACCES_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

stream = TweetsListener()
streamapi = tweepy.Stream(auth = api.auth,listener = stream)

streamapi.filter(
    follow = ["44196397"] )

