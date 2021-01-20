from chalice import Chalice
import boto3
import re
import json
import requests 
from requests_aws4auth import AWS4Auth
import nltk
nltk.download('vader_lexicon', download_dir="/tmp")
from nltk.sentiment.vader import SentimentIntensityAnalyzer


endpoint = 'https://search-xxxxxx-xxxxxxx-7pzxxxxxtr72g53m3apcsx6ka7kaje.us-west-1.es.amazonaws.com' # the ES endpoint, including https://
region = 'us-west-1' # e.g. us-west-1
index = 'topnews' # index name

service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
es_url  = endpoint + '/' + index + '/_doc'

headers = { "Content-Type": "application/json" }

app = Chalice(app_name='NewsCrawler')

@app.lambda_function()
def lambda_handler(event, context):
    print("Scheduled event triggered: Fetch Google Top News")

    #NewsAPI
    url = ('http://newsapi.org/v2/top-headlines?sources=google-news&apiKey=b6xxxxxxxxxxe6d26e69a5ce')
    response = requests.get(url)
    
    # all the articles
    article = response.json()["articles"]
    
    sid = SentimentIntensityAnalyzer()
    for ar in article:
        # get the sentiment
        sentiment = sid.polarity_scores(ar["content"])
        print("sentiment",sentiment)
        # add 'sentiment' key and revise 'source' key
        ar["source"] = ar["source"]["name"]
        ar["sentiment"] = sentiment["compound"]
         
        #print(ar)
        
        #send the JSON to ES
        r = requests.post(es_url, auth=awsauth , json=ar, headers=headers)
        print(r)   
    
    return 0  
