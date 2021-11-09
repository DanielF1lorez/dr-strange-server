from logging import setLogRecordFactory
from typing import ContextManager
from django import http
from django.http import HttpResponse
import datetime
from django.http.response import HttpResponseBadRequest, JsonResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
import tweepy
import json

API_KEY=  "Cxgat7jdZKUXOZN0APDxTAFrw"
API_SECRET_KEY =  "2ZGyXI9HPyzYIj1ns85x1EmNvFRBflnyZ5O68K1McdHB7UroGM"
ACCES_TOKEN = "3754540756-F8u1PoqZ7guykbGpQsR19RBm6UkVWV4oBKqkfvk"
ACCES_TOKEN_SECRET = "Nq5ArhqIXVD6pUGCR5z8A0Wxk3btuw1TLPtEU09GvJzQD"

auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCES_TOKEN, ACCES_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)


def Inicio(request): # Primera respuesta
 for tweet in tweepy.Cursor(api.user_timeline, follow = "44196397",tweet_mode = "extended" ).items(1): 
      nombre = "Elon Musk"
      tiempo = datetime.datetime.now()
    
  
 
      doc_externo = loader.get_template('plantillasaludo.html')

 
 documento= tweet._json["full_text"]  , doc_externo.render({"nombre_persona":nombre, "momento_actual":tiempo})


 
 return HttpResponse(documento)
  

def damefecha(request): #Segunda respuesta 
    fecha_actual = datetime.datetime.now()

    documento = "<html><body><h1>fecha y hora actual %s</h1></body></html>"% fecha_actual

    return HttpResponse(documento)

def tweet(request):
 
 
 for tweet in tweepy.Cursor(api.user_timeline, follow = "44196397",tweet_mode = "extended" ).items(1): 
     
     

     documento = tweet._json["full_text"]

     return HttpResponse(documento)


