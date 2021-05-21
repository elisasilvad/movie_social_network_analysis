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
from movies import Movies


# Compute the mean strenght for female-female relationships and female-male relationships
# female-female
Tot_female_strenght = []
Tot_movie_ff_strenght = []

for G in Movie_networks:
    female = list()
    male = list()
    for n in G.nodes():
        if G.nodes[n]['gender'] == 'female':
            female.append(n)
        # elif G.nodes[n]['gender'] == 'male':
        #     male.append(n)
    for f in female:
        for w in female:
            if G.has_edge(f,w):
                Tot_female_strenght.append(G[f][w]['w'])
    Tot_movie_ff_strenght.append(statistics.mean(Tot_female_strenght))

#print(Tot_female_strenght)
print('Average female-female relationship strenght: ', statistics.mean(Tot_movie_ff_strenght)) #/len(Tot_female_strenght))
print('Female-female relationshp strenght standard deviation: ', statistics.pstdev(Tot_movie_ff_strenght))

ff_strenght_distribution = np.array(sorted(Tot_female_strenght))
# plt.plot(ff_strenght_distribution)
# plt.show()

# male-male
Tot_male_strenght = []
Tot_movie_mm_strenght = []

for G in Movie_networks:
    female = list()
    male = list()
    for n in G.nodes():
        if G.nodes[n]['gender'] == 'male':
            male.append(n)
    for f in male:
        for w in male:
            if G.has_edge(f,w):
                Tot_male_strenght.append(G[f][w]['w'])
    Tot_movie_mm_strenght.append(statistics.mean(Tot_male_strenght))

#print(Tot_male_strenght)
print('Average male-male relationship strenght: ', statistics.mean(Tot_movie_mm_strenght)) #/len(Tot_female_strenght))
print('Male-male relationshp strenght standard deviation: ', statistics.pstdev(Tot_movie_mm_strenght))

mm_strenght_distribution = np.array(sorted(Tot_male_strenght))
# plt.plot(mm_strenght_distribution)
# plt.show()

# male-female
Tot_male_female_strenght = []
Tot_movie_mf_strenght = []

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
                Tot_male_female_strenght.append(G[f][w]['w'])
    Tot_movie_mf_strenght.append(statistics.mean(Tot_male_female_strenght))

#print(Tot_male_strenght)
print('Average male-female relationship strenght: ', statistics.mean(Tot_movie_mf_strenght)) #/len(Tot_female_strenght))
print('Male-female relationshp strenght standard deviation: ', statistics.pstdev(Tot_movie_mf_strenght))

mf_strenght_distribution = np.array(sorted(Tot_male_female_strenght))


# tot strength
Tot_strenght = []
Tot_movie_strenght = []

for G in Movie_networks:
    for n in G.nodes():
        for m in G.nodes():
            if G.has_edge(n,m):
                Tot_strenght.append(G[n][m]['w'])
    Tot_movie_strenght.append(statistics.mean(Tot_strenght))


#print(Tot_movie_strenght)
print('Average relationship strength regardless the gender: ', statistics.mean(Tot_movie_strenght))
print('Relationshp strenght regardless the gender standard deviation: ', statistics.pstdev(Tot_movie_strenght))

tot_strenght_distribution = np.array(sorted(Tot_strenght))
# plt.plot(mf_strenght_distribution)
# plt.show()

plt.plot(ff_strenght_distribution, color='purple')
plt.plot(mm_strenght_distribution, color='turquoise')
plt.plot(mf_strenght_distribution, color='gold')
plt.plot(tot_strenght_distribution, color='orange')
plt.legend(['Female-female strength', 'Male-male strength', 'Male-female strength', 'Strength regardless the gender'])
plt.title('Simil power-law distribution of ranking of relationship strength')
plt.show()

# movie_mean = np.array(sorted(Tot_movie_strenght))
# # y = np.array(Tot_female_strenght)
# plt.plot(movie_mean)
# plt.show()

ff_data = Tot_movie_ff_strenght
mm_data = Tot_movie_mm_strenght
mf_data = Tot_movie_mf_strenght
tot_data = Tot_movie_strenght

df = pd.DataFrame({
      'Female-female strenght': ff_data,
      'Male-male strenght': mm_data,
      'Male-female strenght': mf_data,
      'Total strenght': tot_data})

color = {
    "boxes": "purple",
    "whiskers": "purple",
    "medians": "orange",
    "caps": "magenta",
    }
df.boxplot(grid=False, color=color)
plt.show()

# Calculate differences in movies
Strenght_per_movie = dict(zip(Movies, Tot_movie_mf_strenght))
print(Strenght_per_movie)

Sorted_strenght_per_movie = {k: v for k, v in sorted(Strenght_per_movie.items(), key=lambda item: item[1])}

df = pd.DataFrame.from_dict(Sorted_strenght_per_movie, orient='index')
df.plot.barh()
plt.xlabel("Male-female average relationship strenght")
plt.ylabel("Movie title")
plt.yticks(fontsize=6)
plt.show()


#Perform the t-test
## Define 2 distributions -> mf_strenght_distribution, tot_strenght_distribution
N = len(tot_strenght_distribution)
#Calculate the Standard Deviation
#Calculate the variance to get the standard deviation

#For unbiased max likelihood estimate we have to divide the var by N-1, and therefore the parameter ddof = 1
var_mf = mf_strenght_distribution.var(ddof=1)
var_tot = tot_strenght_distribution.var(ddof=1)

#std deviation
s = np.sqrt((var_mf + var_tot)/2)
s

## Calculate the t-statistics
t = (mf_strenght_distribution.mean() - tot_strenght_distribution.mean())/(s*np.sqrt(2/N))

## Compare with the critical t-value
#Degrees of freedom
df = 2*N - 2

#p-value after comparison with the t
p = 1 - stats.t.cdf(t,df=df)

print("t = " + str(t))
print("p = " + str(2*p))

## Cross Checking with the internal scipy function
t2, p2 = stats.ttest_ind(mf_strenght_distribution, tot_strenght_distribution)
print("t2 = " + str(t2))
print("p2 = " + str(p2))

print(mf_strenght_distribution)
print(tot_strenght_distribution)

print(len(Tot_male_female_strenght))
print(len(Tot_strenght))

# Perform t-test for one sample
#x = Tot_male_female_strenght
#exp_mean = statistics.mean(Tot_movie_strenght)
#tscore, pvalue = ttest_1samp(x, popmean=exp_mean)
#print("t Statistic: ", tscore)
#print("P Value: ", pvalue)

#Perform t-test for independent samples
# HO: relationships weight between characters of the opposite gender is the same as the one between characters of the same gender
# H!: relationships weight between characters of the opposite gender is stronger than the one between characters of the same gender
Tot_same_gender_strength = Tot_movie_mm_strenght + Tot_movie_ff_strenght
tscore, pvalue = stats.ttest_ind(Tot_same_gender_strength, Tot_movie_mf_strenght)
print("t Statistic: ", tscore)
print("P Value: ", pvalue)
print(len(Tot_movie_mm_strenght), len(Tot_movie_ff_strenght), len(Tot_movie_mf_strenght)) # Check if the mean of the average strength of movie character relationships between characters of the opposite gender is stronger than the average of movie relationships between character of the same gender