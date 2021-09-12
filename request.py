import newsapi
from newsapi import NewsApiClient
import urllib.request,json
from .models import News

api_key = None
# Getting the  base url
base_url = None
