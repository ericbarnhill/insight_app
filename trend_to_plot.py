import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pickle
import numpy as np
import io
import urllib.parse
import base64
import random
import numpy as np

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
    plt.figure(figsize=(3,4))
    plt.style.use('seaborn-pastel')
    n_months = len(ts)
    x = np.linspace(1, n_months, n_months)
    plt.plot(x, ts, linewidth=3)
    line_fit = np.polyfit(x, ts, 1)
    fit_start = line_fit[1]
    fit_end = line_fit[1] + n_months*line_fit[0]
    print("start: ", np.round(fit_start))
    print("end: ", np.round(fit_end))
    pct_inc =  fit_end / fit_start
    print("pct inc", pct_inc)
    pct_inc ='{0:.{1}f}%'.format((pct_inc-1)*100, 1)
    print("Percent increase: ", pct_inc)
    plt.xlabel('Month')
    plt.ylabel('Number of Mentions')
    plt.xticks(x)
    random_number = random.randrange(100)
    filename = "plot_" + str(random_number) + ".png"
    print("plot filename:", filename)
    plt.savefig("static/"+filename, bbox_inches="tight")
    plt.clf()
    return filename, n_months, pct_inc

