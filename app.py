import requests
from flask import Flask, render_template, request
app = Flask(__name__)
from get_letters import get_letters
from get_hot_keywords import get_hot_keywords
from top_trends_by_keyword import top_N_trends

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    letters = []
    keywords = get_hot_keywords()
    if request.method == "POST":
        # get url that the user has entered
        try:
            word = request.form['word']
            print("query was ",word)
            trends = top_N_trends(word)
        except:
            errors.append(
                "Unable to process search term. Please make sure it's valid and try again."
            )
    return render_template('index.html', word=word, keywords=keywords, trends=trends, errors=errors)

if __name__ == '__main__':
    app.run()
