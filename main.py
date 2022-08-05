import tweepy
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()
api_key = os.getenv('api_key')
api_secret = os.getenv('api_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

# set the API varaibles
def api():
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)

# Tweets a thingy
def tweet(api: tweepy.API, message: str, image_path: None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print("Tweet successfully")

if __name__ == '__main__':
    api = api()
    tweet(api, "This was Tweeted via Python and Tweepy. Here is my gecko", 'gecko.jpg')
