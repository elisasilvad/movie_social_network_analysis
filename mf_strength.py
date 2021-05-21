import json
import networkx as nx
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import ttest_1samp

from movie_networks import Movie_networks
from movies import Movies, Movies_10s, Movies_30s, Movies_40s, Movies_50s, Movies_60s, Movies_70s, Movies_80s, Movies_90s, Movies_2000s


# Compute the mean strenght for female-female relationships and female-male relationships
# female-female
Tot_ff_strenght = list()
Movies_mean_ff_strenght = list()

for G in Movie_networks:
    female = list()
    for n in G.nodes():
        if G.nodes[n]['gender'] == 'female':
            female.append(n)
    for f in female:
        for w in female:
            if G.has_edge(f,w):
                Tot_ff_strenght.append(G[f][w]['w'])
    Movies_mean_ff_strenght.append(statistics.mean(Tot_ff_strenght))

print(Tot_ff_strenght)
Mean_ff_strength = statistics.mean(Tot_ff_strenght)
print('Mean female-female strength: ', Mean_ff_strength)

# male-male
Tot_mm_strenght = list()
Movies_mean_mm_strenght = list()

for G in Movie_networks:
    male = list()
    for n in G.nodes():
        if G.nodes[n]['gender'] == 'male':
            male.append(n)
    for f in male:
        for w in male:
            if G.has_edge(f,w):
                Tot_mm_strenght.append(G[f][w]['w'])
    Movies_mean_mm_strenght.append(statistics.mean(Tot_mm_strenght))

print(Tot_mm_strenght)
Mean_mm_strength = statistics.mean(Tot_mm_strenght)
print('Mean male-male strength: ', Mean_mm_strength)

# male-female
Tot_mf_strenght = list()
Movies_mean_mf_strenght = list()

for G in Movie_networks:
    female = list()
    male = list()
    for n in G.nodes():
        if G.nodes[n]['gender'] == 'male':
            male.append(n)
        elif G.nodes[n]['gender'] == 'female':
            female.append(n)
    for f in male:
        for w in female:
            if G.has_edge(f,w):
                Tot_mf_strenght.append(G[f][w]['w'])
    Movies_mean_mf_strenght.append(statistics.mean(Tot_mf_strenght))

print(Tot_mf_strenght)
Mean_mf_strength = statistics.mean(Tot_mf_strenght)
print('Mean male-female strength: ', Mean_mf_strength)


# no gender
Tot_strenght = list()
Movies_mean_tot_strenght = list()

for G in Movie_networks:
    for f in G.nodes():
        for w in G.nodes():
            if G.has_edge(f,w):
                Tot_strenght.append(G[f][w]['w'])
    Movies_mean_tot_strenght.append(statistics.mean(Tot_strenght))

print(Tot_strenght)
Mean_tot_strength = statistics.mean(Tot_strenght)
print('Mean tot strength: ', Mean_tot_strength)


# Perform t-test for independent sample
# HO: relationships weight between characters of the opposite gender is the same as the one between characters of the same gender
# H1: relationships weight between characters of the opposite gender is stronger than the one between characters of the same gender
Tot_same_gender_strength = Tot_mm_strenght + Tot_ff_strenght
tscore, pvalue = stats.ttest_ind(Tot_same_gender_strength, Tot_mf_strenght)
print("t Statistic: ", tscore)
print("P Value: ", pvalue)


df = pd.DataFrame({
      'Female-female strenght': Movies_mean_ff_strenght,
      'Male-male strenght': Movies_mean_mm_strenght,
      'Male-female strenght': Movies_mean_mf_strenght,
      'Total strenght': Movies_mean_tot_strenght})

color = {
    "boxes": "purple",
    "whiskers": "purple",
    "medians": "orange",
    "caps": "magenta",
    }
df.boxplot(grid=False, color=color)
plt.show()

# Calculate differences in movies
Strenght_per_movie = dict(zip(Movies, Movies_mean_mf_strenght))
print(Strenght_per_movie)

Sorted_strenght_per_movie = {k: v for k, v in sorted(Strenght_per_movie.items(), key=lambda item: item[1])}

df = pd.DataFrame.from_dict(Sorted_strenght_per_movie, orient='index')
ax = df.plot.barh()

ax.patches[df.index.get_indexer(Movies_10s)[0]].set_facecolor('#000000')
ax.patches[df.index.get_indexer(Movies_30s)[0]].set_facecolor('#4d0039')
for i in Movies_40s:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#800060')
for i in Movies_50s:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#b30086')
for i in Movies_60s:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#e600ac')
for i in Movies_70s:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#ff1ac6')
for i in Movies_80s:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#ff4dd2')
for i in Movies_90s:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#ff80df')
for i in Movies_2000s:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#ffb3ec')

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=2)
plt.yticks(fontsize=6)

plt.xlabel("Male-female average relationship strenght")
plt.ylabel("Movie title")
plt.yticks(fontsize=6)
plt.show()


# Plotting average male-female strength trend in decades
Strength_10s = list()
Strength_30s = list()
Strength_40s = list()
Strength_50s = list()
Strength_60s = list()
Strength_70s = list()
Strength_80s = list()
Strength_90s = list()
Strength_2000s = list()
Strength_trend = list()

for k,v in Strenght_per_movie.items():
    if k in Movies_10s:
        Strength_10s.append(v)
    elif k in Movies_30s:
        Strength_30s.append(v)
    elif k in Movies_40s:
        Strength_40s.append(v)
    elif k in Movies_50s:
        Strength_50s.append(v)
    elif k in Movies_60s:
        Strength_60s.append(v)
    elif k in Movies_70s:
        Strength_70s.append(v)
    elif k in Movies_80s:
        Strength_80s.append(v)
    elif k in Movies_90s:
        Strength_90s.append(v)
    elif k in Movies_2000s:
        Strength_2000s.append(v)

Mod_10s = statistics.mean(Strength_10s)
Mod_30s = statistics.mean(Strength_30s)
Mod_40s = statistics.mean(Strength_40s)
Mod_50s = statistics.mean(Strength_50s)
Mod_60s = statistics.mean(Strength_60s)
Mod_70s = statistics.mean(Strength_70s)
Mod_80s = statistics.mean(Strength_80s)
Mod_90s = statistics.mean(Strength_90s)
Mod_2000s = statistics.mean(Strength_2000s)
Strength_trend = [Mod_10s, Mod_30s, Mod_40s, Mod_50s, Mod_60s, Mod_70s, Mod_80s, Mod_90s, Mod_2000s]
print(Strength_trend)
#Decades = ['10s', '20s', '30s', '40s', '50s', '60s', '70s', '80s', '90s', '2000s']

df = pd.DataFrame({
    'Male-female relationships strenght per decades': Strength_trend,
    'Average strength': Mean_mf_strength})
print(df)

colors = ['purple', 'orange']
ax = df.plot(color=colors)
ax.xaxis.grid(True, linestyle='--')
ax.set_xlabel("Movie decades")
ax.set_ylabel("Average male-female strength per decade")
plt.show()