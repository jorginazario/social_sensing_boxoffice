#Written By: Harry Gebremedhin & Jorge Nazario 
#Program uses get old tweets library
import GetOldTweets3 as got
import re 
import json 

#number of tweets per movie
tweetNum = 1200 

#reads in a movie list and stores in a dictionary
def readMovieList(fileName):
    movieDict = {}
    File = open(fileName, 'r')
    for line in File:
        lis = line.split(',')
        movieDict[lis[0]] = lis[1]
    return movieDict

#function that takes a query string and number of tweets and returns list of tweet objects
def getTweets(queryString, tweetNum):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(queryString)\
                                               .setMaxTweets(tweetNum)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    return tweets

def filterTweet(tweetString):     
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweetString).split())

#returns dictionary with movie title and list of orderpairs which is (tweettext,retweetnumbers)
def organizeTweets(movieDict):
    tweetDict = {}
    for movie in movieDict.values():
        tweetDict[movie] = []
        tweets = getTweets(movie, tweetNum)
        for tweet in tweets:
            t = filterTweet(tweet.text)
            tweetDict[movie].append((t,tweet.retweets))
    return tweetDict

def writeToFile(tweetDict):
    j = json.dumps(tweetDict)
    f = open("tweetsMovies.json", 'w')
    f.write(j)
    f.close()



movieDict = readMovieList('movielist.txt')
tweetDict = organizeTweets(movieDict)
writeToFile(tweetDict)



