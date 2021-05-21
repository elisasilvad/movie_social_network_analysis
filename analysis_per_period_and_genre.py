import networkx.algorithms.community as nx_comm
import statistics
import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import table

from movie_networks import Movie_networks
from movies import Movies, Movies_10s, Movies_30s, Movies_40s, Movies_50s, Movies_60s, Movies_70s, Movies_80s, Movies_90s, Movies_2000s, RomanticComedy, ScienceFiction, Horror, Western, History, AnimatedFilm, Thriller, Drama, Comedy


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
plt.title('Ranking of movie for decreasing modularity (periods)')
plt.show()

# Plot average modularity per decades
Modularity_10s = list()
Modularity_30s = list()
Modularity_40s = list()
Modularity_50s = list()
Modularity_60s = list()
Modularity_70s = list()
Modularity_80s = list()
Modularity_90s = list()
Modularity_2000s = list()
# Mod_trend = list()

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

Mod_RC = statistics.mean(Modularity_10s)
Mod_SF = statistics.mean(Modularity_30s)
Mod_HR = statistics.mean(Modularity_40s)
Mod_WS = statistics.mean(Modularity_50s)
Mod_HIS = statistics.mean(Modularity_60s)
Mod_AF = statistics.mean(Modularity_70s)
Mod_TH = statistics.mean(Modularity_80s)
Mod_DR = statistics.mean(Modularity_90s)
Mod_CY = statistics.mean(Modularity_2000s)

df = pd.DataFrame({'lab':['1910s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s'],
                   'val':[Mod_RC, Mod_SF, Mod_HR, Mod_WS, Mod_HIS, Mod_AF, Mod_TH, Mod_DR, Mod_CY]})
ax = df.plot.bar(x='lab', y='val', rot=0, color={'#cc0099', '#ff00bf', '#e60073', '#ff1a75', '#ff6666','#ff6600', '#ff9933', '#ff9966', '#ffbb33'})
ax.yaxis.grid(True, linestyle='--')
ax.set_xlabel("Movie decade")
ax.set_ylabel("Average modularity")
ax.get_legend().remove()
plt.title('Average modularity per decade')
plt.show()


# Plot ranking of movies for modularity (genre)
Movie_genre = dict()
colors = list()
for k, v in Sorted_modularity_per_movie.items():
    if k in RomanticComedy:
        Movie_genre[v] = 'RomanticComedy'
        colors.append('#000000')
    elif k in ScienceFiction:
        Movie_genre[v] = 'ScienceFiction'
        colors.append('#4d0039')
    elif k in Horror:
        Movie_genre[v] = 'Horror'
        colors.append('#800060')
    elif k in Western:
        Movie_genre[v] = 'Western'
        colors.append('#b30086')
    elif k in History:
        Movie_genre[v] = 'History'
        colors.append('#e600ac')
    elif k in AnimatedFilm:
        Movie_genre[v] = 'AnimatedFilm'
        colors.append('#ff1ac6')
    elif k in Thriller:
        Movie_genre[v] = 'Thriller'
        colors.append('#ff4dd2')
    elif k in Drama:
        Movie_genre[v] = 'Drama'
        colors.append('#ff80df')
    elif k in Comedy:
        Movie_genre[v] = 'Comedy'
        colors.append('#ffb3ec')
print('Movie genre: ', Movie_genre)

df = pd.DataFrame.from_dict(Sorted_modularity_per_movie, orient='index')
df['group'] = df[0].map(Movie_genre)
print(df)

ax = df.plot.barh(color=colors)

for i in RomanticComedy:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#ff3399')
for i in ScienceFiction:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#00ff00')
for i in Horror:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#b300b3')
for i in Western:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#ff8000')
for i in History:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#ffcc00')
for i in AnimatedFilm:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#00ffff')
for i in Thriller:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#ff0000')
for i in Drama:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#0066ff')
for i in Comedy:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#669999')

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=2)
plt.yticks(fontsize=6)
plt.title('Ranking of movies for decreasing modularity (genre)')
plt.show()

# Plot average modularity per genre
Modularity_RomanticComedy = list()
Modularity_ScienceFiction = list()
Modularity_Horror = list()
Modularity_Western = list()
Modularity_History = list()
Modularity_AnimatedFilm = list()
Modularity_Thriller = list()
Modularity_Drama = list()
Modularity_Comedy = list()
# Mod_trend = list()

for k,v in Modularity_per_movie.items():
    if k in RomanticComedy:
        Modularity_RomanticComedy.append(v)
    elif k in ScienceFiction:
        Modularity_ScienceFiction.append(v)
    elif k in Horror:
        Modularity_Horror.append(v)
    elif k in Western:
        Modularity_Western.append(v)
    elif k in History:
        Modularity_History.append(v)
    elif k in AnimatedFilm:
        Modularity_AnimatedFilm.append(v)
    elif k in Thriller:
        Modularity_Thriller.append(v)
    elif k in Drama:
        Modularity_Drama.append(v)
    elif k in Comedy:
        Modularity_Comedy.append(v)

Mod_RC = statistics.mean(Modularity_RomanticComedy)
Mod_SF = statistics.mean(Modularity_ScienceFiction)
Mod_HR = statistics.mean(Modularity_Horror)
Mod_WS = statistics.mean(Modularity_Western)
Mod_HIS = statistics.mean(Modularity_History)
Mod_AF = statistics.mean(Modularity_AnimatedFilm)
Mod_TH = statistics.mean(Modularity_Thriller)
Mod_DR = statistics.mean(Modularity_Drama)
Mod_CY = statistics.mean(Modularity_Comedy)

df = pd.DataFrame({'lab':['Romantic', 'Science Fiction', 'Horror', 'Western', 'History', 'Animation', 'Thriller', 'Drama', 'Comedy'],
                   'val':[Mod_RC, Mod_SF, Mod_HR, Mod_WS, Mod_HIS, Mod_AF, Mod_TH, Mod_DR, Mod_CY]})
ax = df.plot.bar(x='lab', y='val', rot=0, color={'#ff3399', '#00ff00', '#b300b3', '#ff8000', '#ffcc00','#00ffff', '#ff0000', '#0066ff', '#669999'})
ax.yaxis.grid(True, linestyle='--')
ax.set_xlabel("Movie genre")
ax.set_ylabel("Average modularity")
ax.get_legend().remove()
plt.title('Average modularity per genre')
plt.show()


# STRENGTH --------------------------------------------------------------------------------------------------------------------------
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
Mean_mf_strength = (statistics.mean(Tot_mf_strenght))
print('Mean male-female strength: ', Mean_mf_strength)

# Calculate differences in movies per decade
Strenght_per_movie = dict(zip(Movies, Movies_mean_mf_strenght))
print(Strenght_per_movie)

Sorted_strenght_per_movie = {k: v for k, v in sorted(Strenght_per_movie.items(), key=lambda item: item[1])}

df = pd.DataFrame.from_dict(Sorted_strenght_per_movie, orient='index')
ax = df.plot.barh()

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


df = pd.DataFrame({
    'Male-female relationships strenght per decades': Strength_trend,
    'Average strength': Mean_mf_strength})
print(df)

colors = ['purple', 'orange']
ax = df.plot(color=colors)
ax.xaxis.grid(True, linestyle='--')
ax.set_xlabel("Movie decades")
ax.set_ylabel("Average male-female strength per decade")
plt.title('Average movie male-female relationship strength per decade')
plt.show()

# Calculate differences in movies per genre
Strenght_per_movie = dict(zip(Movies, Movies_mean_mf_strenght))
print(Strenght_per_movie)

Sorted_strenght_per_movie = {k: v for k, v in sorted(Strenght_per_movie.items(), key=lambda item: item[1])}

df = pd.DataFrame.from_dict(Sorted_strenght_per_movie, orient='index')
ax = df.plot.barh()

for i in RomanticComedy:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#ff3399')
for i in ScienceFiction:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#00ff00')
for i in Horror:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#b300b3')
for i in Western:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#ff8000')
for i in History:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#ffcc00')
for i in AnimatedFilm:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#00ffff')
for i in Thriller:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#ff0000')
for i in Drama:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#0066ff')
for i in Comedy:
    ax.patches[df.index.get_indexer([i])[0]].set_facecolor('#669999')

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=2)
plt.yticks(fontsize=6)
plt.title('Ranking of movies for decreasing strength')
plt.show()

#Plotting average male-female strength per decade
Strength_10s = list()
Strength_30s = list()
Strength_40s = list()
Strength_50s = list()
Strength_60s = list()
Strength_70s = list()
Strength_80s = list()
Strength_90s = list()
Strength_2000s = list()


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

Str_RC = statistics.mean(Strength_10s)
Str_SF = statistics.mean(Strength_30s)
Str_HR = statistics.mean(Strength_40s)
Str_WS = statistics.mean(Strength_50s)
Str_HIS = statistics.mean(Strength_60s)
Str_AF = statistics.mean(Strength_70s)
Str_TH = statistics.mean(Strength_80s)
Str_DR = statistics.mean(Strength_90s)
Str_CY = statistics.mean(Strength_2000s)

df = pd.DataFrame({'lab':['1910s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s'],
                   'val':[Str_RC, Str_SF, Str_HR, Str_WS, Str_HIS, Str_AF, Str_TH, Str_DR, Str_CY]})
ax = df.plot.bar(x='lab', y='val', rot=0, color={'#cc0099', '#ff00bf', '#e60073', '#ff1a75', '#ff6666','#ff6600', '#ff9933', '#ff9966', '#ffbb33'})
ax.yaxis.grid(True, linestyle='--')
ax.set_xlabel("Movie genre")
ax.set_ylabel("Average male-female strength")
ax.get_legend().remove()
plt.title("Average male-female strength for movie decade")
plt.show()


# Plotting average male-female strength per genre
Strength_RomanticComedy = list()
Strength_ScienceFiction = list()
Strength_Horror = list()
Strength_Western = list()
Strength_History = list()
Strength_AnimatedFilm = list()
Strength_Thriller = list()
Strength_Drama = list()
Strength_Comedy = list()


for k,v in Strenght_per_movie.items():
    if k in RomanticComedy:
        Strength_RomanticComedy.append(v)
    elif k in ScienceFiction:
        Strength_ScienceFiction.append(v)
    elif k in Horror:
        Strength_Horror.append(v)
    elif k in Western:
        Strength_Western.append(v)
    elif k in History:
        Strength_History.append(v)
    elif k in AnimatedFilm:
        Strength_AnimatedFilm.append(v)
    elif k in Thriller:
        Strength_Thriller.append(v)
    elif k in Drama:
        Strength_Drama.append(v)
    elif k in Comedy:
        Strength_Comedy.append(v)

Str_RC = statistics.mean(Strength_RomanticComedy)
Str_SF = statistics.mean(Strength_ScienceFiction)
Str_HR = statistics.mean(Strength_Horror)
Str_WS = statistics.mean(Strength_Western)
Str_HIS = statistics.mean(Strength_History)
Str_AF = statistics.mean(Strength_AnimatedFilm)
Str_TH = statistics.mean(Strength_Thriller)
Str_DR = statistics.mean(Strength_Drama)
Str_CY = statistics.mean(Strength_Comedy)

df = pd.DataFrame({'lab':['Romantic', 'Science Fiction', 'Horror', 'Western', 'History', 'Animation', 'Thriller', 'Drama', 'Comedy'],
                   'val':[Str_RC, Str_SF, Str_HR, Str_WS, Str_HIS, Str_AF, Str_TH, Str_DR, Str_CY]})
ax = df.plot.bar(x='lab', y='val', rot=0, color={'#ff3399', '#00ff00', '#b300b3', '#ff8000', '#ffcc00','#00ffff', '#ff0000', '#0066ff', '#669999'})
ax.yaxis.grid(True, linestyle='--')
ax.set_xlabel("Movie genre")
ax.set_ylabel("Average male-female strength")
ax.get_legend().remove()
plt.title("Average male-female strength for movie genre")
plt.show()


Movie_tab = dict(zip(Movies, Movie_modularity))
df = pd.DataFrame.from_dict(Movie_tab, orient='index')
df['MF strength'] = df[0].map(Strenght_per_movie)
#df['Decade'] = df[0].map(Movie_decades)
df['Genre'] = df[0].map(Movie_genre)
df.rename(columns={0: 'Modularity'}, inplace=True)

print(df.columns)
print(df)


Strenght_per_movie = dict(zip(Movies, Movies_mean_mf_strenght))
df = pd.DataFrame.from_dict(Strenght_per_movie, orient='index')
print(df)