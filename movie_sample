import csv
from random import sample

movie_d = {}
with open('data/network_metadata.tab', 'r') as f:
    for row in csv.reader(f, delimiter='\t'):
        movie_d[row[0]] = row[1:]
del movie_d['GexfID']
print(movie_d)

release_dates = list()
for k in movie_d:
    release_dates.append(movie_d[k][2])
    if movie_d[k][2] == 'ReleaseDate':
        release_dates.remove(movie_d[k][2])
print(sorted(release_dates))

y10s = list()
y20s = list()
y30s = list()
y40s = list()
y50s = list()
y60s = list()
y70s = list()
y80s = list()
y90s = list()
y2000s = list()
y2010s = list()
for d in release_dates:
    d = int(d)
    if d >= 1915 and d <= 1920:
        y10s.append(d)
    elif d > 1920 and d <= 1930:
        y20s.append(d)
    elif d > 1930 and d <= 1940:
        y30s.append(d)
    elif d > 1940 and d <= 1950:
        y40s.append(d)
    elif d > 1950 and d <= 1960:
        y50s.append(d)
    elif d > 1960 and d <= 1970:
        y60s.append(d)
    elif d > 1970 and d <= 1980:
        y70s.append(d)
    elif d > 1980 and d <= 1990:
        y80s.append(d)
    elif d > 1990 and d <= 2000:
        y90s.append(d)
    elif d > 2000 and d <= 2010:
        y2000s.append(d)
    elif d > 2010:
        y2010s.append(d)

print('10s: ', 60*(len(y10s)*100/773)/100)
print('20s: ', 60*(len(y20s)*100/773)/100)
print('30s: ', 60*(len(y30s)*100/773)/100)
print('40s: ', 60*(len(y40s)*100/773)/100)
print('50s: ', 60*(len(y50s)*100/773)/100)
print('60s: ', 60*(len(y60s)*100/773)/100)
print('70s: ', 60*(len(y70s)*100/773)/100)
print('80s: ', 60*(len(y80s)*100/773)/100)
print('90s: ', 60*(len(y90s)*100/773)/100)
print('2000s: ', 60*(len(y2000s)*100/773)/100)
print('2010s: ', 60*(len(y2010s)*100/773)/100)

my10s = list()
my20s = list()
my30s = list()
my40s = list()
my50s = list()
my60s = list()
my70s = list()
my80s = list()
my90s = list()
my2000s = list()
my2010s = list()
for k in movie_d:
    movie_title = movie_d[k][0]
    y = int(movie_d[k][2])
    if y >= 1915 and y <= 1920:
        my10s.append(movie_title)
    elif y > 1920 and y <= 1930:
        my20s.append(movie_title)
    elif y > 1930 and y <= 1940:
        my30s.append(movie_title)
    elif y > 1940 and y <= 1950:
        my40s.append(movie_title)
    elif y > 1950 and y <= 1960:
        my50s.append(movie_title)
    elif y > 1960 and y <= 1970:
        my60s.append(movie_title)
    elif y > 1970 and y <= 1980:
        my70s.append(movie_title)
    elif y > 1980 and y <= 1990:
        my80s.append(movie_title)
    elif y > 1990 and y <= 2000:
        my90s.append(movie_title)
    elif y > 2000 and y <= 2010:
        my2000s.append(movie_title)
    elif y > 2010:
        my2010s.append(movie_title)
print('Movies from 10s: ', my10s)
print('Movies from 20s: ', my20s)
print('Movies from 30s: ', my30s)
print('Movies from 40s: ', my40s)
print('Movies from 50s: ', my50s)
print('Movies from 60s: ', my60s)
print('Movies from 70s: ', my70s)
print('Movies from 80s: ', my80s)
print('Movies from 90s: ', my90s)
print('Movies from 2000s: ', my2000s)
print('Movies from 2010s: ', my2010s)

print(sample(my10s, 1))
print(sample(my30s, 1))
print(sample(my40s, 2))
print(sample(my50s, 2))
print(sample(my60s, 3))
print(sample(my70s, 4))
print(sample(my80s, 9))
print(sample(my90s, 24))
print(sample(my2000s, 22))
print(sample(my2010s, 1))