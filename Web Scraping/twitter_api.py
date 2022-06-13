
import tweepy
import configparser

#read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#get public tweets
public_tweets = api.home_timeline()
#print(public_tweets[0].text)


