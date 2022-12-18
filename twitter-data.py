import tweepy
import configparser
import pandas as pd
import numpy as np

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# search tweets
keywords = "eating disorder OR eatingdisorder OR anorexia OR anorexic OR anorexia OR nervosa OR bulimia OR bulimic OR bulemia OR bulimia OR nervosa OR ednos OR edprob OR proana OR promia OR anamia OR askanamia OR purge OR binge OR thinspo OR bonespo OR legspo"
limit = 900

tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=limit, tweet_mode='extended').items(limit)

# create DataFrame
columns = ['User', 'Tweet', 'Followers', 'Followees', '#Tweets', '#Re-Tweets', 'Hashtags', 'Date of Joining',
            'Date of Last Post']
data = []

for tweet in tweets:
    tweets_list= api.user_timeline(user_id = tweet.user.id, count=1) # Get the last tweet
    data.append([tweet.user.screen_name, tweet.full_text, tweet.user.followers_count, tweet.user.friends_count,
                tweet.user.statuses_count, tweet.retweet_count, len(tweet.entities.get('hashtags')),
                tweet.user.created_at, tweets_list[0].created_at])

df = pd.DataFrame(data, columns=columns)

df.to_csv('ED.csv') # Random Data

data1 = pd.read_csv('ED.csv')

data1 = data1[data1['Tweet'].str.contains('BMI | CW | LW | HW | GW | UGW | kg | lbs', case=False)]

data1.to_csv('final.csv') # ED data

data2 = pd.read_csv('final.csv')

data2 = data2.reset_index()

users = []
for index, row in data2.iterrows():
    users.append(row['User'])

unique_users = set(users) # Nodes

print('Number of Nodes :', len(unique_users))
