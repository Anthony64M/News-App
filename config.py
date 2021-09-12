import os

class Config:
    NEWS_API_BASE_URL ='https://newsapi.org/v1/articles?source={}&apiKey={}'
    NEWS_API_KEY = 'caa505d83e9b49a1b15577dd33860f10'
    SECRET_KEY = 'Anthony64M'



class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

