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


def get_bbc_news(headlines):
    
    '''
    Function returns the top headlines from BBC_news
    '''
    newsapi =NewsApiClient(api_key)

    headlines = newsapi.get_top_headlines(sources ="bbc-news")

    return headlines

def get_aljazeera_news(headlines):
    
    '''
    Function returns the top headlines from Aljazeera_news
    '''

    newsapi =NewsApiClient(api_key)

    headlines = newsapi.get_top_headlines(sources ="al-jazeera-english")

    return headlines


def search_news(keyword):
    
    '''
    Function returns the top headlines from a search query
    '''
    search_news_url = 'https://newsapi.org/v2/everything?q={}&apiKey=caa505d83e9b49a1b15577dd33860f10'.format(keyword)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_results = search_news_response

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_movie_results = process_results(search_news_list)




    return search_results

