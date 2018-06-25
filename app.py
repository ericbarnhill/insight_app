import requests
import pickle
from flask import Flask, render_template, request, redirect, url_for
from get_letters import get_letters
from get_hot_search_terms import hot_search_terms
from top_trends_by_keyword import top_N_trends
from trend_to_plot import trend_to_plot

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("index route")
    errors = []
    searchterm = []
    hot_searchterms = hot_search_terms()
    if request.method == "POST":
        print("post in index route")
        try:
            searchterm = request.form['searchterm']
            # pickle data assets, to render later with graph
            # with open("searchterm.txt", "wb") as fp:
            #    pickle.dump(searchterm, fp)
        except:
            print("no searchterm found, or other error.")
    if searchterm:
        return redirect(url_for('search_results', searchterm = searchterm, hot_searchterms=hot_searchterms))
    else:
        return render_template('index.html', hot_searchterms=hot_searchterms, errors=errors)

@app.route('/searchterm/<searchterm>', methods=['GET', 'POST'])
def search_results(searchterm):
    errors = []
    trends = []
    trends_pct = []
    print("searchterm is", searchterm)
    try:
        hot_searchterms = hot_search_terms()
        trends, trends_pct = top_N_trends(searchterm)
    except:
        errors.append("search term error.")
    print(trends)
    return render_template('index.html', searchterm=searchterm, hot_searchterms=hot_searchterms, trends=trends, trends_pct=trends_pct, errors=errors)

@app.route('/trendingterm/<trendingterm>', methods = ['GET', 'POST'])
def render_plot(trendingterm):
    hot_searchterms = hot_search_terms()
    errors = []
    print("trendingterm is", trendingterm)
    try:
        terms = str.split(trendingterm, '__')
        trendingterm = terms[0]
        if len(terms) > 1:
            searchterm = terms[1]
        else:
            searchterm = []
        trendingterm = ' '.join(str.split(trendingterm, '%20'))
        trends = []
        trends_pct = []
        if searchterm:
            searchterm = ' '.join(str.split(searchterm, '%20'))
            trends, trends_pct = top_N_trends(searchterm)
        try:
            print("plotting:", trendingterm)
            plot_url = trend_to_plot(trendingterm)
        except:
            print("plotting error")
            plot_url = []
        return render_template('index.html', hot_searchterms=hot_searchterms, trends=trends, searchterm=searchterm,  trends_pct=trends_pct, errors=errors, plot_url=plot_url, trendingterm=trendingterm)
    except:
        print("error processing trending term tag, refreshing homepage.")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
