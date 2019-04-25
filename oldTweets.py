#Written By: Harry Gebremedhin & Jorge Nazario 
#Program uses get old tweets library
from textblob import TextBlob
from progressbar import ProgressBar
import GetOldTweets3 as got
import re 
import json 


tweetNum = 1200 #number of tweets per movie
pbar = ProgressBar() # shows progress bar as the program takes too long

#reads in a movie list and stores in a dictionary
def readMovieList(fileName):
    movieDict = {}
    File = open(fileName, 'r')
    for line in File:
        lis = line.split(',')
        movieDict[lis[0]] = lis[1]
    return movieDict

def get_tweet_sentiment(tweet): 
    # create TextBlob object of passed tweet text 
    analysis = TextBlob(tweet) 
    # set sentiment 
    if analysis.sentiment.polarity > 0: 
        return "positive"
    elif analysis.sentiment.polarity == 0: 
        return "neutral"
    else: 
        return "negative"

#function that takes a query string and number of tweets and returns list of tweet objects
def getTweets(queryString, tweetNum):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(queryString)\
                                               .setMaxTweets(tweetNum)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    return tweets

def filterTweet(tweetString):     
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweetString).split())

#returns dictionary with movie title and list of orderpairs which is (average sentiment, average num of retweets)
def organizeTweets(movieDict):
    tweetDict = {}
    for movie in pbar(movieDict.values()):
        positiveCount = 0
        neagativeCount = 0
        totalCount = 0 
        numRetweet = 0

        tweetDict[movie] = []
        tweets = getTweets(movie, tweetNum)
        for tweet in tweets:
            t = filterTweet(tweet.text)
            numRetweet += tweet.retweets
            sentiment = get_tweet_sentiment(t)
            if (sentiment == "positive"):
                positiveCount += 1
            elif (sentiment == "negative"):
                neagativeCount -= 1
        totalCount = positiveCount + neagativeCount
        sentimentFinal = float (totalCount/tweetNum)
        averageRetweet = float (numRetweet/tweetNum)

        tweetDict[movie]= (sentimentFinal, averageRetweet)
    return tweetDict

def writeToFile(tweetDict):
    j = json.dumps(tweetDict)
    f = open("tweetsMovies.json", 'w')
    f.write(j)
    f.close()


movieDict = readMovieList('movielist.txt')
tweetDict = organizeTweets(movieDict)
writeToFile(tweetDict)