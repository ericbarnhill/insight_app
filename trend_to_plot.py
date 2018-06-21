import seaborn as sns
import pickle
import numpy as np

def trend_to_plot(trend):
    # load bow_trends object
    with open("bow_trends.txt", "rb") as fp:
        bow_trends = pickle.load(fp)
    # get time series
    try:
        ts = bow_trends['trend']
    except:
        print("Trending term not found in term dictionary.")
        return False
    sns_plot = sns.tsplot(ts)
    sns_plot.savefig("plot.png")
    print("plot saved")
    return True

