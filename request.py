import newsapi
from newsapi import NewsApiClient
import urllib.request,json
from .models import News

api_key = None
# Getting the  base url
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']



def get_news(headlines):
    
    '''
    Function returns the top headlines from numerous sources
    '''
    
    newsapi =NewsApiClient(api_key)

    headlines = newsapi.get_top_headlines(sources ="")

    return headlines
