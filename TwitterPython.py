#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy


consumer_key = "**************************************"
consumer_secret = "**************************************"
access_token = "**************************************"
access_token_secret = "**************************************"

giris = tweepy.OAuthHandler(consumer_key, consumer_secret)
giris.set_access_token(access_token, access_token_secret)

api = tweepy.API(giris)


def  twitleriGor():
	twitler = api.home_timeline()
	for twit in twitler:
		print twit.text
		print "**************"
		print twit.retweet_count
		

def twitAt():
	twit = raw_input("Twit At>> ")
	api.update_status(twit)
	
	
twitleriGor()	
twitAt() 

# KAYNAK
# http://tweepy.readthedocs.org/en/v3.1.0/
# https://github.com/tweepy/tweepy
