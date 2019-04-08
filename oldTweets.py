#Written By: Harry Gebremedhin & Jorge Nazario 
#Program uses get old tweets library
import GetOldTweets3 as got


# tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama whitehouse")\
#                                            .setMaxTweets(2)
# tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Captain Marvel')\
                                           .setSince("2019-04-08")\
                                           .setUntil("2019-04-20")\
                                           .setMaxTweets(1200)
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
h = []
for tweet in tweets:
  h.append(tweet.text)
print(h)
print('\n')
print(len(h))
