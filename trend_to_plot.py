import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pickle
import numpy as np
import io
import urllib.parse
import base64
import random

def trend_to_plot(trend):
    # load trends object
    with open("trends_converted.pickle", "rb") as fp:
        trends = pickle.load(fp)
    # debug - examine 5 keys
    # print(list(trends)[:5])
    # get time series
    try:
        ts = trends[trend]
    except:
        print("Trending term not found in term dictionary.")
        return False
    print("Trend score: ", ts)
    plt.style.use('seaborn-pastel')
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
    return filename, n_months

