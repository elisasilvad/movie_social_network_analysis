import json
import networkx as nx
import statistics
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from cdlib import algorithms
from community import community_louvain
from collections import defaultdict
from networkx.algorithms.community.centrality import girvan_newman
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats

from movie_networks import Movie_networks
from movies import Movies


# COMMUNITY DETECTION WITH LOUVAIN ALGORITHM
plotdata = list()
p_values = list()

communities = defaultdict(list)
for G in Movie_networks:
    partition = community_louvain.best_partition(G) #It’s a dictionary where keys are their nodes and values the communities
    print('Best partition', partition)

    for key, val in sorted(partition.items()):
        communities[val].append(key)
    Community_dictionary = dict(communities)
    communities.clear()
    #print("Grouped dictionary is : ", Community_dictionary)

    female = list()
    male = list()
    for n in G.nodes():
        if G.nodes[n]['gender'] == 'female':
            female.append(n)
        elif G.nodes[n]['gender'] == 'male':
            male.append(n)

    # Communities_with_female = set()
    # Female_distribution = list()
    # for k in Community_dictionary.keys():
    #     Female_for_community = list()
    #     for f in female:
    #         if f in Community_dictionary[k]:
    #             Communities_with_female.add(k)
    #             Female_for_community.append(f)
    #     Female_distribution.append(Female_for_community)
    #
    # print('Female characters are distributed on ', len(Communities_with_female), 'on', len(Community_dictionary), 'of overall communitites: ', Communities_with_female)
    # print('Female are distributed in this way: ', Female_distribution)
    #
    # N_female = list()
    # for l in Female_distribution:
    #     N_female.append(len(l))
    #
    # df = pd.DataFrame(data=N_female)
    # print(df)
    # ax = df.plot.bar(color='r')
    #plt.show()

    Communities_with_female = set()
    Female_distribution = list()
    Male_distribution = list()
    for k in Community_dictionary.keys():
        Female_for_community = list()
        Male_for_community = list()
        for f in female:
            if f in Community_dictionary[k]:
                Communities_with_female.add(k)
                Female_for_community.append(f)
        for m in male:
            if m in Community_dictionary[k]:
                Male_for_community.append(m)
        Female_distribution.append(Female_for_community)
        Male_distribution.append(Male_for_community)
        # print('F for community:', Female_for_community)
        #print('F distribution: ', Female_distribution)

    N_female = list()
    N_male = list()
    for l in Female_distribution:
        N_female.append(len(l))
    for l in Male_distribution:
        N_male.append(len(l))

    if len(N_female) >= 3:
        statistics, pvalue = stats.shapiro(N_female)  #The normal distribution is a probability distribution of a continuous random variable whose values spread symmetrically around the mean.
        p_values.append(pvalue)

    df = pd.DataFrame({
        "N° male": N_male,
        "N° female": N_female})

    # Print distribution plot for each movie
    #df[["N° male", "N° female"]].plot(kind='bar', stacked=True)
    #plt.show()

    plotdata.append(df)

Tot_df = pd.concat(plotdata)
colors = ['purple', 'orange']
Tot_df.plot(kind="bar", stacked=True, color=colors)
plt.title("Male and female distribution in communities")
plt.xticks(rotation=0, fontsize=4)
plt.xlabel('movie communities')
plt.ylabel('characters per community')
plt.show()

print(len(p_values))
Pvalue_per_movie = dict(zip(Movies, p_values))
Sorted_pvalue_per_movie = {k: v for k, v in sorted(Pvalue_per_movie.items(), key=lambda item: item[1])}

df = pd.DataFrame.from_dict(Sorted_pvalue_per_movie, orient='index')
print(df)

ax = df.plot.barh()
plt.yticks(rotation=0, fontsize=6)
plt.show()



    # pos = nx.spring_layout(G) # draw the graph
    # cmap = cm.get_cmap('viridis', max(partition.values()) + 1)     # color the nodes according to their partition
    # nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40, cmap = cmap, node_color = list(partition.values()))
    # nx.draw_networkx_edges(G, pos, alpha=0.5)
    # plt.show()

# Girvan-Newman Algorithm --> relies on the iterative elimination of edges that have the highest number of shortest paths between nodes passing through them. By removing edges from the graph one-by-one, the network breaks down into smaller pieces, so-called communities. The algorithm was introduced by Michelle Girvan and Mark Newman.
# for G in Movie_networks:
#     communities = girvan_newman(G)
#
#     node_groups = []
#     for com in next(communities):
#         node_groups.append(list(com))
#
#     print(node_groups)
#
#     color_map = []
#     for node in G:
#         if node in node_groups[0]:
#             color_map.append('blue')
#         else:
#             color_map.append('green')
#     nx.draw(G, node_color=color_map, with_labels=True)
#     plt.show()