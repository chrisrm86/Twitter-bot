import tweepy
from time import sleep
from credentials import *

# variables
keyword = "#covid-19 AND #vaccine -filter:retweets"
items_search = 5

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK.")
except:
    print("Error during authentication.")

# bot data
bot_information = api.me()
print("{} loaded".format(bot_information.name))
bot_twitter_acount = api.get_user(bot_information.screen_name)
print("username: {}".format(bot_information.screen_name))
print("description: {}".format(bot_information.description))
print("followers: {}".format(bot_information.followers_count))
print("-"*20)

# Last followers
print("Last 20 followers")
for follower in bot_twitter_acount.followers():
    print("- {}".format(follower.screen_name))

# follow followers
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    #print(follower.screen_name)
    #api.update_status("Thanks for follow me " + "@{}".format(follower.screen_name))

# retweets
for tweet in tweepy.Cursor(api.search, q=keyword, lang='en').items(items_search):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)
        tweet.retweet()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# likes
for tweet in tweepy.Cursor(api.search, q=keyword, lang='en').items(items_search):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)
        tweet.favorite()
        print('Tweet liked')
        sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
