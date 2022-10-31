#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:54:54 2021

@author: noahjohnson
"""

import tmdbsimple as tmdb
from datetime import datetime
import csv
import json
import pandas as pd
import numpy as np

#file = open("movie_ids_11_20_2021.txt",)
#csv_output = open("movies_original.csv","w")
csv_test_output = open("movie_gross_testing_set.csv", "w")
# id_list = []
# lines = file.readlines()

# for i in lines:
#     s = '{' + i.partition(',')[2]
#     s = s.partition(',"v')[0] + '}'
#     temp_dict = json.loads(s)
#     if temp_dict["popularity"] >= 2:
#         id_list.append(temp_dict["id"])

# writer = csv.writer(csv_output)
important_attrs = ["belongs_to_collection", "budget", "id", "imdb_id", "overview", "popularity", "release_date", "revenue", "runtime", "tagline", "title", "vote_average", "vote_count"]  
# writer.writerow(important_attrs)    
        
# for j in range(len(id_list)):
#      search = tmdb.Movies(id_list[j]).info()
#      search = {key : search[key] for key in important_attrs}
#      if search['release_date'] != '':
#          new_date = datetime.strptime(search['release_date'], "%Y-%m-%d")
#          if ((new_date.year >= 1991 and search['popularity'] >= 5) or new_date.year >= 2011) and search['revenue'] > 0:
#                  writer.writerow(search.values())
#                  print("Adding", search['title'], "to training set")

df1 = pd.read_csv("movies_original_with_imdb_2.csv")
csv_genres = open("movie_genres.csv", 'w')
writer_genres = csv.writer(csv_genres)
writer_genres.writerow(['title', 'genres'])
for i in df1['title']:
    genre_list = tmdb.Search().movie(query = i)['results'][0]['genre_ids']
    writer_genres.writerow([i, genre_list])
    
df2 = pd.read_csv('movie_genres.csv')
df1 = df1.merge(df2, how = 'inner', left_on = df1['title'], right_on = df2['title'])
genre_dict = {'28' : 'action', '16' : 'animated', '18' : 'drama', '10751' : 'family', 
              '14' : 'fantasy', '36' : 'history', '35' : 'comedy', '10752' : 'war', '80' : 'crime',
              '99' : 'documentary', '10402' : 'music', '9648' : 'mystery', '10749' : 'romance', 
              '878' : 'sci-fi', '27' : 'horror', '53' : 'thriller', '37' : 'western', '12' : 'adventure'}

for i in range(len(df1['genres'])):
    temp_list = df1['genres'][i]   
    temp_list = temp_list.strip('][').split(', ')
    for j in range(len(temp_list)):
        if temp_list[j] in list(genre_dict.keys()):
            temp_list[j] = genre_dict[temp_list[j]]
        else:
            temp_list[j] = 'other'
        df1['genres'][i] = temp_list

df1['genreAdventure'] = [False for i in range(len(df1['genres']))]

for i in range(len(df1['genres'])):
    df1['genreAction'][i] = 'action' in df1['genres'][i]
    df1['genreAnimated'][i] = 'animated' in df1['genres'][i]
    df1['genreDrama'][i] = 'drama' in df1['genres'][i]
    df1['genreFamily'][i] = 'family' in df1['genres'][i]
    df1['genreFantasy'][i] = 'fantasy' in df1['genres'][i]
    df1['genreHistory'][i] = 'history' in df1['genres'][i]
    df1['genreComedy'][i] = 'comedy' in df1['genres'][i]
    df1['genreWar'][i] = 'war' in df1['genres'][i]
    df1['genreCrime'][i] = 'crime' in df1['genres'][i]
    df1['genreDocumentary'][i] = 'documentary' in df1['genres'][i]
    df1['genreMusic'][i] = 'music' in df1['genres'][i]
    df1['genreMystery'][i] = 'mystery' in df1['genres'][i]
    df1['genreRomance'][i] = 'romance' in df1['genres'][i]
    df1['genreSciFi'][i] = 'sci-fi' in df1['genres'][i]
    df1['genreHorror'][i] = 'horror' in df1['genres'][i]
    df1['genreThriller'][i] = 'thriller' in df1['genres'][i]
    df1['genreWestern'][i] = 'western' in df1['genres'][i]
    df1['genreAdventure'][i] = 'adventure' in df1['genres'][i]
df1 = df1.drop('genres', axis = 1)

for j in range(len(df1['genreAction'])):
    #df1['genreAction'] = np.where(df1['genreAction'] == True, 1, 0)
    df1['genreAnimated'] = np.where(df1['genreAnimated'] == True, 1, 0)
    df1['genreDrama'] = np.where(df1['genreDrama'] == True, 1, 0)
    df1['genreFamily'] = np.where(df1['genreFamily'] == True, 1, 0)
    df1['genreFantasy'] = np.where(df1['genreFantasy'] == True, 1, 0)
    df1['genreHistory'] = np.where(df1['genreHistory'] == True, 1, 0)
    df1['genreComedy'] = np.where(df1['genreComedy'] == True, 1, 0)
    df1['genreWar'] = np.where(df1['genreWar'] == True, 1, 0)
    df1['genreCrime'] = np.where(df1['genreCrime'] == True, 1, 0)
    df1['genreDocumentary'] = np.where(df1['genreDocumentary'] == True, 1, 0)
    df1['genreMusic'] = np.where(df1['genreMusic'] == True, 1, 0)
    df1['genreMystery'] = np.where(df1['genreMystery'] == True, 1, 0)
    df1['genreRomance'] = np.where(df1['genreRomance'] == True, 1, 0)
    df1['genreSciFi'] = np.where(df1['genreSciFi'] == True, 1, 0)
    df1['genreHorror'] = np.where(df1['genreHorror'] == True, 1, 0)
    df1['genreThriller'] = np.where(df1['genreThriller'] == True, 1, 0)
    df1['genreWestern'] = np.where(df1['genreWestern'] == True, 1, 0)
    df1['genreAdventure'] = np.where(df1['genreAdventure'] == True, 1, 0)

df1.to_csv('movies_original_with_imdb_2.csv', index = False)


final_testing_movies = ["Encanto", "House of Gucci", "Resident Evil: Welcome to Raccoon City"]

# for i in range(len(final_testing_movies)):
#     test = tmdb.Search().movie(query = final_testing_movies[i])
#     for j in range(len(important_attrs)):
        
writer_test = csv.writer(csv_test_output)
writer_test.writerow(important_attrs)

result = tmdb.Search().movie(query = 'House of Gucci')['results'][0]
id_val = result['id']
search = tmdb.Movies(id_val).info()
search = {key : search[key] for key in important_attrs}
search['genres'] = result['genre_ids']
writer_test.writerow(search.values())

tmdb.API_KEY = "f61426bf8c6b7c1ad48547a6904cfdbf"

tmdb.Movies(69).info()['release_date']
test = tmdb.Search().movie(query = "Encanto")
#tmdb.Movies(252).info()
movie_id = test['results'][0]['id']
tmdb.Movies(id_list.index(movie_id)).info()['revenue']
#tmdb.Movies(movie_id).info()
tmdb.Genres().
