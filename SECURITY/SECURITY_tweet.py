#!/usr/bin/env python
from twython import Twython
APP_KEY = 'YOUR_APP_KEY' # FILL THIS IN WHEN APPROVED
APP_SECRET = 'YOUR_APP_SECRET'
OAUTH_TOKEN = 'MY_TOKEN'
OAUTH_TOKEN_SECRET = 'TOKEN_SECRET'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
photo = open('*/home/SECURITY/img.jpg', 'rb')  #PUT THIS SCRIPT WITH CAMERA SCRIPT TO MATCH DATE DOWN TO SECOND
response = twitter.upload_media(media=photo)
twitter.update_status(status='SECURITY CAMERA PIC:', media_ids=[response['media_id']])  #UPDATES STATUS WITH IMAGE
