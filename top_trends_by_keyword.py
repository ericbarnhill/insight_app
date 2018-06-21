import operator
from get_hot_keywords import get_graph

def top_N_trends(keyword, N=10):
    G = get_graph()
    node_edges = G.edges(keyword.lower())
    edges_dict = {}
    for edge in node_edges:
        key = edge[1]
        value = G[edge[0]][edge[1]]['weight']
        edges_dict.update({key:value})
    index = 0
    trends = []
    for key, value in sorted(edges_dict.items(), key=operator.itemgetter(1), reverse=True):
        trends.append(' '.join([key, str(value)]))
        index += 1
        if index >= N:
            break
    return trends
