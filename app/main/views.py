from flask import render_template,request,redirect,url_for
from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_abc_news, get_aljazeera_news, get_bbc_news, get_news, search_news

@main.route('/')
def index():
    '''
    main generate docstring
    '''

    news = get_news('headlines')

    headline = news['articles']

    search_news = request.args.get('news_query')

    if search_news:

        return redirect(url_for('main.search',keyword =search_news))
    else:

        return render_template('index.html', headline = headline)


@main.route('/search/<keyword>')
def search(keyword):
    '''
    View function to display the search results
    '''
    news_name_list =keyword.split(" ")
  
    searched_news = search_news(keyword)

    title = f'SEARCH RESULT FOR   {news_name_list}'
    
    return render_template('search.html',title = title, news = searched_news)
