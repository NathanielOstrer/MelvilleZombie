import markovify
import tweepy
import time

# Twitter authentication
consumer_key = '96AhfssCSVvXuzLeZw2HO9tdz'
consumer_secret = 'ZB7nfoCj71wpy4xnZWJVFp6XReJN8mkFiK9XxXFoXxs1IiCkXH'
access_token = '3718965617-DauRyzQ8tog69Vn27dVbO987hNeMPF7vuxq40Fu'
access_token_secret = 'TdEBvUV6KsQGTHepCKM4002DAxT2T4cRaaJWco4aF6e4Y'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get corpus
corpus = 'mobydick.txt'

with open(corpus) as f:
    text = f.read()

# Train model
text_model = markovify.Text(text)

# Tweet
while True:
    while True:
         tweet = text_model.make_short_sentence(140)
         if tweet != None:
             break

    api.update_status(tweet)

    # Wait a day to tweet again
    time.sleep(60*60*24)
