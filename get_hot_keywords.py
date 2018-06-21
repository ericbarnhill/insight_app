import pickle
import networkx as nx
import operator

def get_graph():
    with open("G.txt", "rb") as fp:
        G = pickle.load(fp)
    return G

def get_hot_keywords(N=20):
    G = get_graph()
    keywords =  {}
    for node in G.nodes(data=True):
        if node[1]['is_key']:
            total_wt = 0
            for edge in G.edges(node[0], data=True):
                total_wt += edge[2]['weight']
            keywords.update({node[0]: total_wt})
    hot_keywords = []
    n = 0
    for item in sorted(keywords.items(), key=operator.itemgetter(1), reverse=True):
        hot_keywords.append(item)
        n += 1
        if n >= N:
            break
    return hot_keywords
