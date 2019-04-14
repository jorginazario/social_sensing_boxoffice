#Written By: Harry Gebremedhin & Jorge Nazario 
#Program Crawls Twitter and gets tweets made about movies 
#This will be used for movies that are about to come out
import tweepy
import re

#Returns api object after authentication 
def authenticate(consumer_key,consumer_secret,access_token,access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
        return api

def search(queryString, count, api):
        tweets = api.search(queryString, count)
        for tweet in tweets:
                print (tweet.text.encode("utf-8"))

#some more filtering with the querystring as well 
def filterTweet(tweetString):     
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweetString).split())
