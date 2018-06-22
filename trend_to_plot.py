import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pickle
import numpy as np
import io
import urllib.parse
import base64
import random

def trend_to_plot(trend):
    # load bow_trends object
    with open("bow_trends.txt", "rb") as fp:
        bow_trends = pickle.load(fp)
    # debug - examine 5 keys
    # print(list(bow_trends)[:5])
    # get time series
    try:
        ts = bow_trends[trend]
    except:
        print("Trending term not found in term dictionary.")
        return False
    plt.style.use('ggplot')
    n_months = len(ts)
    x = np.linspace(1, n_months, n_months)
    plt.plot(x, ts)
    plt.xlabel('Month')
    plt.ylabel('Number of Mentions')
    plt.xticks(x)
    random_number = random.randrange(100)
    filename = "plot_" + str(random_number) + ".png"
    print("plot filename:", filename)
    plt.savefig("static/"+filename, bbox_inches="tight")
    plt.clf()
    return filename

