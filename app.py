import requests
from flask import Flask, render_template, request
app = Flask(__name__)
from get_letters import get_letters

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    letters = []
    if request.method == "POST":
        # get url that the user has entered
        try:
            word = request.form['word']
            print(word)
            letters = get_letters(word)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
    return render_template('index.html', errors=errors, letters=letters)

if __name__ == '__main__':
    app.run()
