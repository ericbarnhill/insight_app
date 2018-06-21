import operator
from get_hot_search_terms import get_graph

def top_N_trends(keyword, N=10):
    G = get_graph()
    node_edges = G.edges(keyword.lower())
    edges_dict = {}
    total_weight = 0
    for edge in node_edges:
        key = edge[1]
        value = G[edge[0]][edge[1]]['weight']
        total_weight += value
        edges_dict.update({key:value})
    index = 0
    trends = []
    trends_pct = []
    for key, value in sorted(edges_dict.items(), key=operator.itemgetter(1), reverse=True):
        value_pct = value / total_weight * 100
        value_str = "{:.1f}%".format(value_pct)
        trends.append(key)
        trends_pct.append(value_str)
        index += 1
        if index >= N:
            break
    return trends, trends_pct
