import requests
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        try:
            search_term = request.form['word']
            print("word was:")
            print(word)
        except: 
            print("error")
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
