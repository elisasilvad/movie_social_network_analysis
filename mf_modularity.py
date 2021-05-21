import networkx.algorithms.community as nx_comm
import statistics
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl

from movie_networks import Movie_networks
from movies import Movies, Movies_10s, Movies_30s, Movies_40s, Movies_50s, Movies_60s, Movies_70s, Movies_80s, Movies_90s, Movies_2000s

# MODULARITY --------------------------------------------------------------------------------------------------------------------------
Movie_modularity = list()

for G in Movie_networks:
    female = list()
    male = list()
    for n in G.nodes():
        if G.nodes[n]['gender'] == 'female':
            female.append(n)
        elif G.nodes[n]['gender'] == 'male':
            male.append(n)

    G_modularity = nx_comm.modularity(G, [male, female], weight='w')
    Movie_modularity.append(G_modularity)

print(Movie_modularity)


# Use statistics module to compute modularity mean and standard deviation
print('Modularity mean:', statistics.mean(Movie_modularity))
print('Modularity standard deviation: ', statistics.pstdev(Movie_modularity))

df = pd.DataFrame({
    'Movie modularity': Movie_modularity,
    'Modularity mean': statistics.mean(Movie_modularity)})

colors = ['purple', 'orange']
df.plot(grid=False, color=colors)
plt.title("Modularity values in the sampled movies")
plt.legend(loc='lower left')
plt.show()


df = pd.DataFrame({
    'Movie modularity': Movie_modularity,
    })

color = {
    "boxes": "purple",
    "whiskers": "purple",
    "medians": "orange",
    "caps": "magenta",
    }
df.boxplot(grid=False, color=color)
plt.title('Standard deviation of modularity in the sampled movies')
plt.show()

# Print modularity for movies
Modularity_per_movie = dict(zip(Movies, Movie_modularity))
print(Modularity_per_movie)
Sorted_modularity_per_movie = {k: v for k, v in sorted(Modularity_per_movie.items(), key=lambda item: item[1])}
print(Sorted_modularity_per_movie)

# Plot ranking of movie for decreasing modularity (periods)
Movie_decades = dict()
colors = list()
for k, v in Sorted_modularity_per_movie.items():
    if k in Movies_10s:
        Movie_decades[v] = '10s'
        colors.append('#000000')
    elif k in Movies_30s:
        Movie_decades[v] = '30s'
        colors.append('#4d0039')
    elif k in Movies_40s:
        Movie_decades[v] = '40s'
        colors.append('#800060')
    elif k in Movies_50s:
        Movie_decades[v] = '50s'
        colors.append('#b30086')
    elif k in Movies_60s:
        Movie_decades[v] = '60s'
        colors.append('#e600ac')
    elif k in Movies_70s:
        Movie_decades[v] = '70s'
        colors.append('#ff1ac6')
    elif k in Movies_80s:
        Movie_decades[v] = '80s'
        colors.append('#ff4dd2')
    elif k in Movies_90s:
        Movie_decades[v] = '90s'
        colors.append('#ff80df')
    elif k in Movies_2000s:
        Movie_decades[v] = '00s'
        colors.append('#ffb3ec')
print('Movie decades: ', Movie_decades)

df = pd.DataFrame.from_dict(Sorted_modularity_per_movie, orient='index')

df['group'] = df[0].map(Movie_decades)
print(df)

ax = df.plot.barh(color=colors)

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
plt.title('Movies sorted for decreasing modularity')
#plt.show()

# Plotting average modularity trend in decades
Modularity_10s = list()
Modularity_30s = list()
Modularity_40s = list()
Modularity_50s = list()
Modularity_60s = list()
Modularity_70s = list()
Modularity_80s = list()
Modularity_90s = list()
Modularity_2000s = list()
Mod_trend = list()

for k,v in Modularity_per_movie.items():
    if k in Movies_10s:
        Modularity_10s.append(v)
    elif k in Movies_30s:
        Modularity_30s.append(v)
    elif k in Movies_40s:
        Modularity_40s.append(v)
    elif k in Movies_50s:
        Modularity_50s.append(v)
    elif k in Movies_60s:
        Modularity_60s.append(v)
    elif k in Movies_70s:
        Modularity_70s.append(v)
    elif k in Movies_80s:
        Modularity_80s.append(v)
    elif k in Movies_90s:
        Modularity_90s.append(v)
    elif k in Movies_2000s:
        Modularity_2000s.append(v)

Mod_10s = statistics.mean(Modularity_10s)
Mod_30s = statistics.mean(Modularity_30s)
Mod_40s = statistics.mean(Modularity_40s)
Mod_50s = statistics.mean(Modularity_50s)
Mod_60s = statistics.mean(Modularity_60s)
Mod_70s = statistics.mean(Modularity_70s)
Mod_80s = statistics.mean(Modularity_80s)
Mod_90s = statistics.mean(Modularity_90s)
Mod_2000s = statistics.mean(Modularity_2000s)
Mod_trend = [Mod_10s, Mod_30s, Mod_40s, Mod_50s, Mod_60s, Mod_70s, Mod_80s, Mod_90s, Mod_2000s]
#Decades = ['10s', '20s', '30s', '40s', '50s', '60s', '70s', '80s', '90s', '2000s']

df = pd.DataFrame({
    'Movie modularity per decades': Mod_trend,
    'Modularity mean': statistics.mean(Movie_modularity)})
print(df)

colors = ['purple', 'orange']
ax = df.plot(color=colors)
ax.xaxis.grid(True, linestyle='--')
ax.set_xlabel("Movie decades")
ax.set_ylabel("Average modularity per decade")
#for d in Decades:
#    ax.set_xticklabels(d)
plt.show()