
import Certificacion
import tweepy
import time

#authenticacion

auth = tweepy.OAuthHandler(Certificacion.API_KEY, Certificacion.API_SECRET_KEY)

auth.set_access_token(Certificacion.ACCES_TOKEN, Certificacion.ACCES_TOKEN_SECRET)

api = tweepy.API(auth)



id = None
count = 0
while True:
    tweets = api.user_timeline("@elonmusk", max_id=id)
    for tweet in tweets:
      if tweet.text.startswith("RT"):
          
       continue
    print (tweet.text)
    print ()
         
         
    id = tweet.id
  