import json
import networkx as nx
import statistics
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# FOUR FEATHERS
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Four_Feathers.json", "r", encoding='utf-8') as data:
    Four_Feathers = json.load(data)

# Create the movie graph
Four_Feathers_node_names = []
Four_Feathers_edges = []

for i in Four_Feathers['network']['nodes']:
     id = (i['id'])
     Four_Feathers_node_names.append(id)

for i in Four_Feathers['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Four_Feathers_edges.append(tuple)

Four_Feathers_G = nx.Graph()
Four_Feathers_G.add_nodes_from(Four_Feathers_node_names)
Four_Feathers_G.add_edges_from(Four_Feathers_edges)

# Create male and female groups
Four_Feathers_female = ['ETHNE', 'CAROLINE']
Four_Feathers_male = []

for m in Four_Feathers_node_names:
    if m not in Four_Feathers_female:
        Four_Feathers_male.append(m)

# Assign gender property to each nodes
# Create empty dictionaries for nodes' attributes
gender = {}

# Set node attributes through nx built-in function allowing to associate each node with attributes.
# The set_node_attributes function takes three variables: the Graph to which you’re adding the attribute,
# the dictionary of id-attribute pairs, and the name of the new attribute.
for n in Four_Feathers_female:
    gender[n] = 'female'

for n in Four_Feathers_male:
    gender[n] = 'male'

nx.set_node_attributes(Four_Feathers_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks = list()
Movie_networks.append(Four_Feathers_G)


# LOST HORIZON
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Lost_Horizon.json", "r", encoding='utf-8') as data:
    Lost_Horizon = json.load(data)

# Create the movie graph
Lost_Horizon_node_names = []
Lost_Horizon_edges = []

for i in Lost_Horizon['network']['nodes']:
     id = (i['id'])
     Lost_Horizon_node_names.append(id)

for i in Lost_Horizon['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w': w})
        Lost_Horizon_edges.append(tuple)

Lost_Horizon_G = nx.Graph()
Lost_Horizon_G.add_nodes_from(Lost_Horizon_node_names)
Lost_Horizon_G.add_edges_from(Lost_Horizon_edges)

# Create male and female groups
Lost_Horizon_female = ['GLORIA', 'SONDRA', 'MARIA', 'NATIVE GIRL']
Lost_Horizon_male = []

for m in Lost_Horizon_node_names:
    if m not in Lost_Horizon_female:
        Lost_Horizon_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Lost_Horizon_female:
    gender[n] = 'female'

for n in Lost_Horizon_male:
    gender[n] = 'male'

nx.set_node_attributes(Lost_Horizon_G, gender, 'gender')

# Add the graph to movie network list
#Movie_networks = list()
Movie_networks.append(Lost_Horizon_G)


# IT'S A WONDERFUL LIFE
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Wonderful_Life.json", "r", encoding='utf-8') as data:
    Wonderful_Life = json.load(data)

# Create the movie graph
Wonderful_Life_node_names = []
Wonderful_Life_edges = []

for i in Wonderful_Life['network']['nodes']:
     id = (i['id'])
     Wonderful_Life_node_names.append(id)

for i in Wonderful_Life['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Wonderful_Life_edges.append(tuple)

Wonderful_Life_G = nx.Graph()
Wonderful_Life_G.add_nodes_from(Wonderful_Life_node_names)
Wonderful_Life_G.add_edges_from(Wonderful_Life_edges)

# Create male and female groups
Wonderful_Life_female = ['MARY', 'MOTHER', 'ANNIE', 'WOMAN', 'ZUZU', 'MRS HATCH', 'MRS THOMPSON', 'SECRETARY', 'VIOLET', 'MARIA', 'COUSIN TILLY', 'JANIE', 'RUTH', 'JANE', 'MRS DAVIS', 'MRS BAILEY']
Wonderful_Life_male = []

for m in Wonderful_Life_node_names:
    if m not in Wonderful_Life_female:
        Wonderful_Life_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Wonderful_Life_female:
    gender[n] = 'female'

for n in Wonderful_Life_male:
    gender[n] = 'male'

nx.set_node_attributes(Wonderful_Life_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Wonderful_Life_G)


# MR BLANDINGS BUILDS HIS DREAM HOUSE
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Mr_Blandings.json", "r", encoding='utf-8') as data:
    Mr_Blandings = json.load(data)

# Create the movie graph
Mr_Blandings_node_names = []
Mr_Blandings_edges = []

for i in Mr_Blandings['network']['nodes']:
     id = (i['id'])
     Mr_Blandings_node_names.append(id)

for i in Mr_Blandings['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Mr_Blandings_edges.append(tuple)

Mr_Blandings_G = nx.Graph()
Mr_Blandings_G.add_nodes_from(Mr_Blandings_node_names)
Mr_Blandings_G.add_edges_from(Mr_Blandings_edges)

# Create male and female groups
Mr_Blandings_female = ['MARY', 'GUSSIE', 'THE GIRLS', 'MURIEL', 'JOAN', 'BETSY']
Mr_Blandings_male = []

for m in Mr_Blandings_node_names:
    if m not in Mr_Blandings_female:
        Mr_Blandings_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Mr_Blandings_female:
    gender[n] = 'female'

for n in Mr_Blandings_male:
    gender[n] = 'male'

nx.set_node_attributes(Mr_Blandings_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Mr_Blandings_G)


# GUNSMOKE
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Gunsmoke.json", "r", encoding='utf-8') as data:
    Gunsmoke = json.load(data)

# Create the movie graph
Gunsmoke_node_names = []
Gunsmoke_edges = []

for i in Gunsmoke['network']['nodes']:
     id = (i['id'])
     Gunsmoke_node_names.append(id)

for i in Gunsmoke['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Gunsmoke_edges.append(tuple)

Gunsmoke_G = nx.Graph()
Gunsmoke_G.add_nodes_from(Gunsmoke_node_names)
Gunsmoke_G.add_edges_from(Gunsmoke_edges)

# Create male and female groups
Gunsmoke_female = ['ELAINE', 'MARCIA', 'MARY', 'HELEN', 'MRS WYATT', ]
Gunsmoke_male = []

for m in Gunsmoke_node_names:
    if m not in Gunsmoke_female:
        Gunsmoke_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Gunsmoke_female:
    gender[n] = 'female'

for n in Gunsmoke_male:
    gender[n] = 'male'

nx.set_node_attributes(Gunsmoke_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Gunsmoke_G)



# WHITE CHRISTMAS
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/White_Christmas.json", "r", encoding='utf-8') as data:
    White_Christmas = json.load(data)

# Create the movie graph
White_Christmas_node_names = []
White_Christmas_edges = []

for i in White_Christmas['network']['nodes']:
     id = (i['id'])
     White_Christmas_node_names.append(id)

for i in White_Christmas['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        White_Christmas_edges.append(tuple)

White_Christmas_G = nx.Graph()
White_Christmas_G.add_nodes_from(White_Christmas_node_names)
White_Christmas_G.add_edges_from(White_Christmas_edges)

# Create male and female groups
White_Christmas_female = ['SYLVIA', 'MARTHA', 'BETTY', 'RITA', 'GIRLS', 'JUDY', 'SUSAN']
White_Christmas_male = []

for m in White_Christmas_node_names:
    if m not in White_Christmas_female:
        White_Christmas_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in White_Christmas_female:
    gender[n] = 'female'

for n in White_Christmas_male:
    gender[n] = 'male'

nx.set_node_attributes(White_Christmas_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(White_Christmas_G)


# THE MANCHURIAN CANDIDATE
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/The_Manchurian_Candidate.json", "r", encoding='utf-8') as data:
    The_Manchurian_Candidate = json.load(data)

# Create the movie graph
The_Manchurian_Candidate_node_names = []
The_Manchurian_Candidate_edges = []

for i in The_Manchurian_Candidate['network']['nodes']:
     id = (i['id'])
     The_Manchurian_Candidate_node_names.append(id)

for i in The_Manchurian_Candidate['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        The_Manchurian_Candidate_edges.append(tuple)

The_Manchurian_Candidate_G = nx.Graph()
The_Manchurian_Candidate_G.add_nodes_from(The_Manchurian_Candidate_node_names)
The_Manchurian_Candidate_G.add_edges_from(The_Manchurian_Candidate_edges)

# Create male and female groups
The_Manchurian_Candidate_female = ['MIRELLA', 'ROSIE', 'MYSTERIOUS WOMAN', 'WOMAN', 'JOCELYN', 'ELLIE']
The_Manchurian_Candidate_male = []

for m in The_Manchurian_Candidate_node_names:
    if m not in The_Manchurian_Candidate_female:
        The_Manchurian_Candidate_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in The_Manchurian_Candidate_female:
    gender[n] = 'female'

for n in The_Manchurian_Candidate_male:
    gender[n] = 'male'

nx.set_node_attributes(The_Manchurian_Candidate_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(The_Manchurian_Candidate_G)


# PLANET OF APES
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Planet_of_Apes.json", "r", encoding='utf-8') as data:
    Planet_of_Apes = json.load(data)

# Create the movie graph
Planet_of_Apes_node_names = []
Planet_of_Apes_edges = []

for i in Planet_of_Apes['network']['nodes']:
     id = (i['id'])
     Planet_of_Apes_node_names.append(id)

for i in Planet_of_Apes['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Planet_of_Apes_edges.append(tuple)

Planet_of_Apes_G = nx.Graph()
Planet_of_Apes_G.add_nodes_from(Planet_of_Apes_node_names)
Planet_of_Apes_G.add_edges_from(Planet_of_Apes_edges)

# Create male and female groups
Planet_of_Apes_female = ['NURSE', 'ZIRA']
Planet_of_Apes_male = []

for m in Planet_of_Apes_node_names:
    if m not in Planet_of_Apes_female:
        Planet_of_Apes_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Planet_of_Apes_female:
    gender[n] = 'female'

for n in Planet_of_Apes_male:
    gender[n] = 'male'

nx.set_node_attributes(Planet_of_Apes_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Planet_of_Apes_G)


# PLANET OF APES
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Rocky.json", "r", encoding='utf-8') as data:
    Rocky = json.load(data)

# Create the movie graph
Rocky_node_names = []
Rocky_edges = []

for i in Rocky['network']['nodes']:
     id = (i['id'])
     Rocky_node_names.append(id)

for i in Rocky['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Rocky_edges.append(tuple)

Rocky_G = nx.Graph()
Rocky_G.add_nodes_from(Rocky_node_names)
Rocky_G.add_edges_from(Rocky_edges)

# Create male and female groups
Rocky_female = ['MARIE', 'ADRIAN', 'SECRETARY', 'WOMAN', ]
Rocky_male = []

for m in Rocky_node_names:
    if m not in Rocky_female:
        Rocky_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Rocky_female:
    gender[n] = 'female'

for n in Rocky_male:
    gender[n] = 'male'

nx.set_node_attributes(Rocky_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Rocky_G)


# BARRY LYNDON
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Barry_Lyndon.json", "r", encoding='utf-8') as data:
    Barry_Lyndon = json.load(data)

# Create the movie graph
Barry_Lyndon_node_names = []
Barry_Lyndon_edges = []

for i in Barry_Lyndon['network']['nodes']:
     id = (i['id'])
     Barry_Lyndon_node_names.append(id)

for i in Barry_Lyndon['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Barry_Lyndon_edges.append(tuple)

Barry_Lyndon_G = nx.Graph()
Barry_Lyndon_G.add_nodes_from(Barry_Lyndon_node_names)
Barry_Lyndon_G.add_edges_from(Barry_Lyndon_edges)

# Create male and female groups
Barry_Lyndon_female = ['COUNTESS', 'DOROTHY', 'AUNT', "MRS O'REILLY", 'CHAMBERMAID', 'MOTHER']
Barry_Lyndon_male = []

for m in Barry_Lyndon_node_names:
    if m not in Barry_Lyndon_female:
        Barry_Lyndon_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Barry_Lyndon_female:
    gender[n] = 'female'

for n in Barry_Lyndon_male:
    gender[n] = 'male'

nx.set_node_attributes(Barry_Lyndon_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Barry_Lyndon_G)


# THE GETAWAY
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/The_Getaway.json", "r", encoding='utf-8') as data:
    The_Getaway = json.load(data)

# Create the movie graph
The_Getaway_node_names = []
The_Getaway_edges = []

for i in The_Getaway['network']['nodes']:
     id = (i['id'])
     The_Getaway_node_names.append(id)

for i in The_Getaway['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        The_Getaway_edges.append(tuple)

The_Getaway_G = nx.Graph()
The_Getaway_G.add_nodes_from(The_Getaway_node_names)
The_Getaway_G.add_edges_from(The_Getaway_edges)

# Create male and female groups
The_Getaway_female = ['SECRETARY', 'GIRL', 'FRAN', 'CAROL']
The_Getaway_male = []

for m in The_Getaway_node_names:
    if m not in The_Getaway_female:
        The_Getaway_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in The_Getaway_female:
    gender[n] = 'female'

for n in The_Getaway_male:
    gender[n] = 'male'

nx.set_node_attributes(The_Getaway_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(The_Getaway_G)


# GREMLINS
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Gremlins.json", "r", encoding='utf-8') as data:
    Gremlins = json.load(data)

# Create the movie graph
Gremlins_node_names = []
Gremlins_edges = []

for i in Gremlins['network']['nodes']:
     id = (i['id'])
     Gremlins_node_names.append(id)

for i in Gremlins['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Gremlins_edges.append(tuple)

Gremlins_G = nx.Graph()
Gremlins_G.add_nodes_from(Gremlins_node_names)
Gremlins_G.add_edges_from(Gremlins_edges)

# Create male and female groups
Gremlins_female = ['LYNN', 'PEGGY', 'MOTHER', 'MRS DEAGLE', 'TRACY', 'STEWARDESS']
Gremlins_male = []

for m in Gremlins_node_names:
    if m not in Gremlins_female:
        Gremlins_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Gremlins_female:
    gender[n] = 'female'

for n in Gremlins_male:
    gender[n] = 'male'

nx.set_node_attributes(Gremlins_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Gremlins_G)


# HARD TO KILL
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Hard_To_Kill.json", "r", encoding='utf-8') as data:
    Hard_To_Kill = json.load(data)

# Create the movie graph
Hard_To_Kill_node_names = []
Hard_To_Kill_edges = []

for i in Hard_To_Kill['network']['nodes']:
     id = (i['id'])
     Hard_To_Kill_node_names.append(id)

for i in Hard_To_Kill['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Hard_To_Kill_edges.append(tuple)

Hard_To_Kill_G = nx.Graph()
Hard_To_Kill_G.add_nodes_from(Hard_To_Kill_node_names)
Hard_To_Kill_G.add_edges_from(Hard_To_Kill_edges)

# Create male and female groups
Hard_To_Kill_female = ['HOUSEWIFE', 'ANDY', 'FELICIA', 'MARTHA', 'MRS WADE', 'OLD LADY']
Hard_To_Kill_male = []

for m in Hard_To_Kill_node_names:
    if m not in Hard_To_Kill_female:
        Hard_To_Kill_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Hard_To_Kill_female:
    gender[n] = 'female'

for n in Hard_To_Kill_male:
    gender[n] = 'male'

nx.set_node_attributes(Hard_To_Kill_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Hard_To_Kill_G)


# TOP GUN
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Top_Gun.json", "r", encoding='utf-8') as data:
    Top_Gun = json.load(data)

# Create the movie graph
Top_Gun_node_names = []
Top_Gun_edges = []

for i in Top_Gun['network']['nodes']:
     id = (i['id'])
     Top_Gun_node_names.append(id)

for i in Top_Gun['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Top_Gun_edges.append(tuple)

Top_Gun_G = nx.Graph()
Top_Gun_G.add_nodes_from(Top_Gun_node_names)
Top_Gun_G.add_edges_from(Top_Gun_edges)

# Create male and female groups
Top_Gun_female = ['GIRL', 'FIRST GIRL', 'SECOND GIRL', 'CHARLIE', 'CAROL']
Top_Gun_male = []

for m in Top_Gun_node_names:
    if m not in Top_Gun_female:
        Top_Gun_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Top_Gun_female:
    gender[n] = 'female'

for n in Top_Gun_male:
    gender[n] = 'male'

nx.set_node_attributes(Top_Gun_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Top_Gun_G)


# RAISING ARIZONA
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Raising_Arizona.json", "r", encoding='utf-8') as data:
    Raising_Arizona = json.load(data)

# Create the movie graph
Raising_Arizona_node_names = []
Raising_Arizona_edges = []

for i in Raising_Arizona['network']['nodes']:
     id = (i['id'])
     Raising_Arizona_node_names.append(id)

for i in Raising_Arizona['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Raising_Arizona_edges.append(tuple)

Raising_Arizona_G = nx.Graph()
Raising_Arizona_G.add_nodes_from(Raising_Arizona_node_names)
Raising_Arizona_G.add_edges_from(Raising_Arizona_edges)

# Create male and female groups
Raising_Arizona_female = ['FLORENCE', 'CASHIER', 'SECRETARY', 'WOMAN']
Raising_Arizona_male = []

for m in Raising_Arizona_node_names:
    if m not in Raising_Arizona_female:
        Raising_Arizona_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Raising_Arizona_female:
    gender[n] = 'female'

for n in Raising_Arizona_male:
    gender[n] = 'male'

nx.set_node_attributes(Raising_Arizona_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Raising_Arizona_G)


# BABETTE'S FEAST
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Babette_Feast.json", "r", encoding='utf-8') as data:
    Babette_Feast = json.load(data)

# Create the movie graph
Babette_Feast_node_names = []
Babette_Feast_edges = []

for i in Babette_Feast['network']['nodes']:
     id = (i['id'])
     Babette_Feast_node_names.append(id)

for i in Babette_Feast['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Babette_Feast_edges.append(tuple)

Babette_Feast_G = nx.Graph()
Babette_Feast_G.add_nodes_from(Babette_Feast_node_names)
Babette_Feast_G.add_edges_from(Babette_Feast_edges)

# Create male and female groups
Babette_Feast_female = ['HEROINE', 'LITTLE GIRL', 'GRANDMA', 'BELLE']
Babette_Feast_male = []

for m in Babette_Feast_node_names:
    if m not in Babette_Feast_female:
        Babette_Feast_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Babette_Feast_female:
    gender[n] = 'female'

for n in Babette_Feast_male:
    gender[n] = 'male'

nx.set_node_attributes(Babette_Feast_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Babette_Feast_G)


# AMADEUS
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Amadeus.json", "r", encoding='utf-8') as data:
    Amadeus = json.load(data)

# Create the movie graph
Amadeus_node_names = []
Amadeus_edges = []

for i in Amadeus['network']['nodes']:
     id = (i['id'])
     Amadeus_node_names.append(id)

for i in Amadeus['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Amadeus_edges.append(tuple)

Amadeus_G = nx.Graph()
Amadeus_G.add_nodes_from(Amadeus_node_names)
Amadeus_G.add_edges_from(Amadeus_edges)

# Create male and female groups
Amadeus_female = ['SECOND LADY', 'LORL', 'FRAU SCHLUMBERG', 'MADAME WEBER', 'CONSTANZE', 'ACTRESSES', 'CAVALIERI', 'GERTRUDE', 'THIRD LADY', 'THREE LADIES', 'FIRST LADY', 'UGLY OLD WOMAN', ]
Amadeus_male = []

for m in Amadeus_node_names:
    if m not in Amadeus_female:
        Amadeus_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Amadeus_female:
    gender[n] = 'female'

for n in Amadeus_male:
    gender[n] = 'male'

nx.set_node_attributes(Amadeus_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Amadeus_G)


# ESCAPE FROM NEW YORK
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Escape_From_New_York.json", "r", encoding='utf-8') as data:
    Escape_From_New_York = json.load(data)


# Create the movie graph
Escape_From_New_York_node_names = []
Escape_From_New_York_edges = []

for i in Escape_From_New_York['network']['nodes']:
     id = (i['id'])
     Escape_From_New_York_node_names.append(id)

for i in Escape_From_New_York['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Escape_From_New_York_edges.append(tuple)

Escape_From_New_York_G = nx.Graph()
Escape_From_New_York_G.add_nodes_from(Escape_From_New_York_node_names)
Escape_From_New_York_G.add_edges_from(Escape_From_New_York_edges)


# Create male and female groups
Escape_From_New_York_female = ['MAGGIE', "GIRL IN CHOCK FULL O' NUTS"]
Escape_From_New_York_male = []

for m in Escape_From_New_York_node_names:
    if m not in Escape_From_New_York_female:
        Escape_From_New_York_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Escape_From_New_York_female:
    gender[n] = 'female'

for n in Escape_From_New_York_male:
    gender[n] = 'male'

nx.set_node_attributes(Escape_From_New_York_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Escape_From_New_York_G)


# BATMAN
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Batman.json", "r", encoding='utf-8') as data:
    Batman = json.load(data)

# Create the movie graph
Batman_node_names = []
Batman_edges = []

for i in Batman['network']['nodes']:
     id = (i['id'])
     Batman_node_names.append(id)

for i in Batman['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Batman_edges.append(tuple)

Batman_G = nx.Graph()
Batman_G.add_nodes_from(Batman_node_names)
Batman_G.add_edges_from(Batman_edges)

# Create male and female groups
Batman_female = ['ANCHORWOMAN', 'ALICIA', 'MIRANDA', 'CLAIRE', 'VICKI']
Batman_male = []

for m in Batman_node_names:
    if m not in Batman_female:
        Batman_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Batman_female:
    gender[n] = 'female'

for n in Batman_male:
    gender[n] = 'male'

nx.set_node_attributes(Batman_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Batman_G)


# KUNDUN
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Kundun.json", "r", encoding='utf-8') as data:
    Kundun = json.load(data)

# Create the movie graph
Kundun_node_names = []
Kundun_edges = []

for i in Kundun['network']['nodes']:
     id = (i['id'])
     Kundun_node_names.append(id)

for i in Kundun['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Kundun_edges.append(tuple)

Kundun_G = nx.Graph()
Kundun_G.add_nodes_from(Kundun_node_names)
Kundun_G.add_edges_from(Kundun_edges)

# Create male and female groups
Kundun_female = ['MOTHER', 'OLD WOMAN', 'TIBETAN WOMAN']
Kundun_male = []

for m in Kundun_node_names:
    if m not in Kundun_female:
        Kundun_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Kundun_female:
    gender[n] = 'female'

for n in Kundun_male:
    gender[n] = 'male'

nx.set_node_attributes(Kundun_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Kundun_G)


# LOST IN SPACE
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Lost_In_Space.json", "r", encoding='utf-8') as data:
    Lost_In_Space = json.load(data)

# Create the movie graph
Lost_In_Space_node_names = []
Lost_In_Space_edges = []

for i in Lost_In_Space['network']['nodes']:
     id = (i['id'])
     Lost_In_Space_node_names.append(id)

for i in Lost_In_Space['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Lost_In_Space_edges.append(tuple)

Lost_In_Space_G = nx.Graph()
Lost_In_Space_G.add_nodes_from(Lost_In_Space_node_names)
Lost_In_Space_G.add_edges_from(Lost_In_Space_edges)

# Create male and female groups
Lost_In_Space_female = ['REPORTER', 'PENNY', 'MAUREEN', 'PRINCIPAL', 'ANNIE', 'JUDY']
Lost_In_Space_male = []

for m in Lost_In_Space_node_names:
    if m not in Lost_In_Space_female:
        Lost_In_Space_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Lost_In_Space_female:
    gender[n] = 'female'

for n in Lost_In_Space_male:
    gender[n] = 'male'

nx.set_node_attributes(Lost_In_Space_G, gender, 'gender')

# Add the graph to movie network list
Movie_networks.append(Lost_In_Space_G)


# FRENCH KISS
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/French_Kiss.json", "r", encoding='utf-8') as data:
    French_Kiss = json.load(data)

# Create the movie graph
French_Kiss_node_names = []
French_Kiss_edges = []

for i in French_Kiss['network']['nodes']:
     id = (i['id'])
     French_Kiss_node_names.append(id)

for i in French_Kiss['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        French_Kiss_edges.append(tuple)

French_Kiss_G = nx.Graph()
French_Kiss_G.add_nodes_from(French_Kiss_node_names)
French_Kiss_G.add_edges_from(French_Kiss_edges)

# Create male and female groups
French_Kiss_female = ["JUDGE HILLIER'S WIFE", 'CLAIRE', 'GIRL #1', 'MATRON', 'LILLIAN', 'CONNIE', 'GIRL #2', 'OLDER NURSE', 'NURSE WITH HYPO', 'WOMAN', 'NURSE', 'WARDROBE MISTRESS', 'WOMEN IN WARD', 'YOUNG NURSE']
French_Kiss_male = []

for m in French_Kiss_node_names:
    if m not in French_Kiss_female:
        French_Kiss_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in French_Kiss_female:
    gender[n] = 'female'

for n in French_Kiss_male:
    gender[n] = 'male'

nx.set_node_attributes(French_Kiss_G, gender, 'gender')
print(French_Kiss_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(French_Kiss_G)


# JACKIE BROWN
# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Jackie_Brown.json", "r", encoding='utf-8') as data:
    Jackie_Brown = json.load(data)
print(Jackie_Brown)

# Create the movie graph
Jackie_Brown_node_names = []
Jackie_Brown_edges = []

for i in Jackie_Brown['network']['nodes']:
     id = (i['id'])
     Jackie_Brown_node_names.append(id)

for i in Jackie_Brown['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Jackie_Brown_edges.append(tuple)

Jackie_Brown_G = nx.Graph()
Jackie_Brown_G.add_nodes_from(Jackie_Brown_node_names)
Jackie_Brown_G.add_edges_from(Jackie_Brown_edges)
print(nx.info(Jackie_Brown_G))

# Create male and female groups
Jackie_Brown_female = ['NICOLE', 'WANDA', 'AMY', 'ANITA', 'MELANI', 'MELANIE', 'SHERONDA', 'JACKIE', 'YOUNG GIRL', 'SALESGIRL']
Jackie_Brown_male = []

for m in Jackie_Brown_node_names:
    if m not in Jackie_Brown_female:
        Jackie_Brown_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Jackie_Brown_female:
    gender[n] = 'female'

for n in Jackie_Brown_male:
    gender[n] = 'male'

nx.set_node_attributes(Jackie_Brown_G, gender, 'gender')
print(Jackie_Brown_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Jackie_Brown_G)
print(Movie_networks)


# THE MATRIX
print("------The_Matrix------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/The_Matrix.json", "r", encoding='utf-8') as data:
    The_Matrix = json.load(data)
print(The_Matrix)

# Create the movie graph
The_Matrix_node_names = []
The_Matrix_edges = []

for i in The_Matrix['network']['nodes']:
     id = (i['id'])
     The_Matrix_node_names.append(id)

for i in The_Matrix['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        The_Matrix_edges.append(tuple)

The_Matrix_G = nx.Graph()
The_Matrix_G.add_nodes_from(The_Matrix_node_names)
The_Matrix_G.add_edges_from(The_Matrix_edges)
print(nx.info(The_Matrix_G))

# Create male and female groups
The_Matrix_female = ['ORACLE', 'WOMAN', 'TRINITY', 'SWITCH', 'DUJOUR', 'PRIESTESS']
The_Matrix_male = []

for m in The_Matrix_node_names:
    if m not in The_Matrix_female:
        The_Matrix_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in The_Matrix_female:
    gender[n] = 'female'

for n in The_Matrix_male:
    gender[n] = 'male'

nx.set_node_attributes(The_Matrix_G, gender, 'gender')
print(The_Matrix_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(The_Matrix_G)
print(Movie_networks)


# ENEMY OF THE STATE
print("------Enemy_Of_The_State------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Enemy_Of_The_State.json", "r", encoding='utf-8') as data:
    Enemy_Of_The_State = json.load(data)
print(Enemy_Of_The_State)

# Create the movie graph
Enemy_Of_The_State_node_names = []
Enemy_Of_The_State_edges = []

for i in Enemy_Of_The_State['network']['nodes']:
     id = (i['id'])
     Enemy_Of_The_State_node_names.append(id)

for i in Enemy_Of_The_State['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Enemy_Of_The_State_edges.append(tuple)

Enemy_Of_The_State_G = nx.Graph()
Enemy_Of_The_State_G.add_nodes_from(Enemy_Of_The_State_node_names)
Enemy_Of_The_State_G.add_edges_from(Enemy_Of_The_State_edges)
print(nx.info(Enemy_Of_The_State_G))

# Create male and female groups
Enemy_Of_The_State_female = ['MARTHA', 'CHRISTA', 'RACHEL', 'WOMAN', 'YOUNG WOMAN', 'BYSTANDER', 'JENNY', 'MEG', 'NANNY', 'SAL', 'STACY', 'REYNOLDS WIFE']
Enemy_Of_The_State_male = []

for m in Enemy_Of_The_State_node_names:
    if m not in Enemy_Of_The_State_female:
        Enemy_Of_The_State_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Enemy_Of_The_State_female:
    gender[n] = 'female'

for n in Enemy_Of_The_State_male:
    gender[n] = 'male'

nx.set_node_attributes(Enemy_Of_The_State_G, gender, 'gender')
print(Enemy_Of_The_State_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Enemy_Of_The_State_G)
print(Movie_networks)


# ONE EIGHT SEVEN
print("------One_Eight_Seven------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/One_Eight_Seven.json", "r", encoding='utf-8') as data:
    One_Eight_Seven = json.load(data)
print(One_Eight_Seven)

# Create the movie graph
One_Eight_Seven_node_names = []
One_Eight_Seven_edges = []

for i in One_Eight_Seven['network']['nodes']:
     id = (i['id'])
     One_Eight_Seven_node_names.append(id)

for i in One_Eight_Seven['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        One_Eight_Seven_edges.append(tuple)

One_Eight_Seven_G = nx.Graph()
One_Eight_Seven_G.add_nodes_from(One_Eight_Seven_node_names)
One_Eight_Seven_G.add_edges_from(One_Eight_Seven_edges)
print(nx.info(One_Eight_Seven_G))

# Create male and female groups
One_Eight_Seven_female = ['ANGLO WOMAN', 'MRS FORD', 'ASIAN GIRL', 'TEACHER #1', 'ELLEN', 'MRS SANCHEZ', 'LAKESIA', 'IRIS', 'RITA', 'SECRETARY']
One_Eight_Seven_male = []

for m in One_Eight_Seven_node_names:
    if m not in One_Eight_Seven_female:
        One_Eight_Seven_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in One_Eight_Seven_female:
    gender[n] = 'female'

for n in One_Eight_Seven_male:
    gender[n] = 'male'

nx.set_node_attributes(One_Eight_Seven_G, gender, 'gender')
print(One_Eight_Seven_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(One_Eight_Seven_G)
print(Movie_networks)


# BUFFY THE VAMPIRE SLAYER
print("------Buffy------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Buffy.json", "r", encoding='utf-8') as data:
    Buffy = json.load(data)
print(Buffy)

# Create the movie graph
Buffy_node_names = []
Buffy_edges = []

for i in Buffy['network']['nodes']:
     id = (i['id'])
     Buffy_node_names.append(id)

for i in Buffy['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Buffy_edges.append(tuple)

Buffy_G = nx.Graph()
Buffy_G.add_nodes_from(Buffy_node_names)
Buffy_G.add_edges_from(Buffy_edges)
print(nx.info(Buffy_G))

# Create male and female groups
Buffy_female = ['WAITRESS', 'BUFFY', 'GIRL', 'CHEERLEADERS', 'NICOLE', 'AMILYN', 'CASSANDRA', 'KIMBERLY', "BUFFY'S MOM", 'ANGLE - KIMBERLY', 'JENNIFER']
Buffy_male = []

for m in Buffy_node_names:
    if m not in Buffy_female:
        Buffy_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Buffy_female:
    gender[n] = 'female'

for n in Buffy_male:
    gender[n] = 'male'

nx.set_node_attributes(Buffy_G, gender, 'gender')
print(Buffy_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Buffy_G)
print(Movie_networks)


# THE CROW: CITY OF ANGELS
print("------The_Crow------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/The_Crow.json", "r", encoding='utf-8') as data:
    The_Crow = json.load(data)
print(The_Crow)

# Create the movie graph
The_Crow_node_names = []
The_Crow_edges = []

for i in The_Crow['network']['nodes']:
     id = (i['id'])
     The_Crow_node_names.append(id)

for i in The_Crow['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        The_Crow_edges.append(tuple)

The_Crow_G = nx.Graph()
The_Crow_G.add_nodes_from(The_Crow_node_names)
The_Crow_G.add_edges_from(The_Crow_edges)
print(nx.info(The_Crow_G))

# Create male and female groups
The_Crow_female = ['SARAH', 'HOLLY', 'SIBYL', 'GRACE', 'WOMAN', ]
The_Crow_male = []

for m in The_Crow_node_names:
    if m not in The_Crow_female:
        The_Crow_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in The_Crow_female:
    gender[n] = 'female'

for n in The_Crow_male:
    gender[n] = 'male'

nx.set_node_attributes(The_Crow_G, gender, 'gender')
print(The_Crow_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(The_Crow_G)
print(Movie_networks)


# DONNIE BRASCO
print("------Donnie_Brasco------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Donnie_Brasco.json", "r", encoding='utf-8') as data:
    Donnie_Brasco = json.load(data)
print(Donnie_Brasco)

# Create the movie graph
Donnie_Brasco_node_names = []
Donnie_Brasco_edges = []

for i in Donnie_Brasco['network']['nodes']:
     id = (i['id'])
     Donnie_Brasco_node_names.append(id)

for i in Donnie_Brasco['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Donnie_Brasco_edges.append(tuple)

Donnie_Brasco_G = nx.Graph()
Donnie_Brasco_G.add_nodes_from(Donnie_Brasco_node_names)
Donnie_Brasco_G.add_edges_from(Donnie_Brasco_edges)
print(nx.info(Donnie_Brasco_G))

# Create male and female groups
Donnie_Brasco_female = ['JUDY', 'NURSE', 'LOUISE', 'MAGGIE', 'MA GGIE']
Donnie_Brasco_male = []

for m in Donnie_Brasco_node_names:
    if m not in Donnie_Brasco_female:
        Donnie_Brasco_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Donnie_Brasco_female:
    gender[n] = 'female'

for n in Donnie_Brasco_male:
    gender[n] = 'male'

nx.set_node_attributes(Donnie_Brasco_G, gender, 'gender')
print(Donnie_Brasco_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Donnie_Brasco_G)
print(Movie_networks)


# WILD WILD WEST
print("------Wild_Wild_West------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Wild_Wild_West.json", "r", encoding='utf-8') as data:
    Wild_Wild_West = json.load(data)
print(Wild_Wild_West)

# Create the movie graph
Wild_Wild_West_node_names = []
Wild_Wild_West_edges = []

for i in Wild_Wild_West['network']['nodes']:
     id = (i['id'])
     Wild_Wild_West_node_names.append(id)

for i in Wild_Wild_West['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Wild_Wild_West_edges.append(tuple)

Wild_Wild_West_G = nx.Graph()
Wild_Wild_West_G.add_nodes_from(Wild_Wild_West_node_names)
Wild_Wild_West_G.add_edges_from(Wild_Wild_West_edges)
print(nx.info(Wild_Wild_West_G))

# Create male and female groups
Wild_Wild_West_female = ['SALOON GIRL', 'MISS EAST', 'DRAGON LADY', 'MISS LIPPENREIDER', 'MUNITIA', 'WOMAN', 'RITA', 'DORA', 'AMAZONIA']
Wild_Wild_West_male = []

for m in Wild_Wild_West_node_names:
    if m not in Wild_Wild_West_female:
        Wild_Wild_West_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Wild_Wild_West_female:
    gender[n] = 'female'

for n in Wild_Wild_West_male:
    gender[n] = 'male'

nx.set_node_attributes(Wild_Wild_West_G, gender, 'gender')
print(Wild_Wild_West_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Wild_Wild_West_G)
print(Movie_networks)



# BROKEN ARROW
print("------Broken_Arrow------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Broken_Arrow.json", "r", encoding='utf-8') as data:
    Broken_Arrow = json.load(data)
print(Broken_Arrow)

# Create the movie graph
Broken_Arrow_node_names = []
Broken_Arrow_edges = []

for i in Broken_Arrow['network']['nodes']:
     id = (i['id'])
     Broken_Arrow_node_names.append(id)

for i in Broken_Arrow['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Broken_Arrow_edges.append(tuple)

Broken_Arrow_G = nx.Graph()
Broken_Arrow_G.add_nodes_from(Broken_Arrow_node_names)
Broken_Arrow_G.add_edges_from(Broken_Arrow_edges)
print(nx.info(Broken_Arrow_G))

# Create male and female groups
Broken_Arrow_female = ['WANDA', 'TERRY']
Broken_Arrow_male = []

for m in Broken_Arrow_node_names:
    if m not in Broken_Arrow_female:
        Broken_Arrow_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Broken_Arrow_female:
    gender[n] = 'female'

for n in Broken_Arrow_male:
    gender[n] = 'male'

nx.set_node_attributes(Broken_Arrow_G, gender, 'gender')
print(Broken_Arrow_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Broken_Arrow_G)
print(Movie_networks)

# COPYCAT
print("------Copycat------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Copycat.json", "r", encoding='utf-8') as data:
    Copycat = json.load(data)
print(Copycat)

# Create the movie graph
Copycat_node_names = []
Copycat_edges = []

for i in Copycat['network']['nodes']:
     id = (i['id'])
     Copycat_node_names.append(id)

for i in Copycat['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Copycat_edges.append(tuple)

Copycat_G = nx.Graph()
Copycat_G.add_nodes_from(Copycat_node_names)
Copycat_G.add_edges_from(Copycat_edges)
print(nx.info(Copycat_G))

# Create male and female groups
Copycat_female = ['GIGI', 'WOMAN', 'SUSAN', 'HELEN']
Copycat_male = []

for m in Copycat_node_names:
    if m not in Copycat_female:
        Copycat_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Copycat_female:
    gender[n] = 'female'

for n in Copycat_male:
    gender[n] = 'male'

nx.set_node_attributes(Copycat_G, gender, 'gender')
print(Copycat_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Copycat_G)
print(Movie_networks)

# BEAN
print("------Bean------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Bean.json", "r", encoding='utf-8') as data:
    Bean = json.load(data)
print(Bean)

# Create the movie graph
Bean_node_names = []
Bean_edges = []

for i in Bean['network']['nodes']:
     id = (i['id'])
     Bean_node_names.append(id)

for i in Bean['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Bean_edges.append(tuple)

Bean_G = nx.Graph()
Bean_G.add_nodes_from(Bean_node_names)
Bean_G.add_edges_from(Bean_edges)
print(nx.info(Bean_G))

# Create male and female groups
Bean_female = ['NURSE 2', 'ANNIE', 'ALISON', 'OLD LADY 1', 'JENNIFER', 'MISS HUTCHINSON', 'NURSE', 'OLD LADY 2']
Bean_male = []

for m in Bean_node_names:
    if m not in Bean_female:
        Bean_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Bean_female:
    gender[n] = 'female'

for n in Bean_male:
    gender[n] = 'male'

nx.set_node_attributes(Bean_G, gender, 'gender')
print(Bean_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Bean_G)
print(Movie_networks)


# SO I MARRIED AN AXE MURDERER?
print("------Axe_Murderer------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Axe_Murderer.json", "r", encoding='utf-8') as data:
    Axe_Murderer = json.load(data)
print(Axe_Murderer)

# Create the movie graph
Axe_Murderer_node_names = []
Axe_Murderer_edges = []

for i in Axe_Murderer['network']['nodes']:
     id = (i['id'])
     Axe_Murderer_node_names.append(id)

for i in Axe_Murderer['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Axe_Murderer_edges.append(tuple)

Axe_Murderer_G = nx.Graph()
Axe_Murderer_G.add_nodes_from(Axe_Murderer_node_names)
Axe_Murderer_G.add_edges_from(Axe_Murderer_edges)
print(nx.info(Axe_Murderer_G))

# Create male and female groups
Axe_Murderer_female = ['HARRIET', 'ROSE', 'MAY', 'PENNY', 'LADY', 'GIRLS', 'STEWARDESS', 'SHERRI', 'KATHY', 'TOURIST', 'SUSAN']
Axe_Murderer_male = []

for m in Axe_Murderer_node_names:
    if m not in Axe_Murderer_female:
        Axe_Murderer_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Axe_Murderer_female:
    gender[n] = 'female'

for n in Axe_Murderer_male:
    gender[n] = 'male'

nx.set_node_attributes(Axe_Murderer_G, gender, 'gender')
print(Axe_Murderer_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Axe_Murderer_G)
print(Movie_networks)


# WONDER BOYS
print("------Wonder_Boys------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Wonder_Boys.json", "r", encoding='utf-8') as data:
    Wonder_Boys = json.load(data)
print(Wonder_Boys)

# Create the movie graph
Wonder_Boys_node_names = []
Wonder_Boys_edges = []

for i in Wonder_Boys['network']['nodes']:
     id = (i['id'])
     Wonder_Boys_node_names.append(id)

for i in Wonder_Boys['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Wonder_Boys_edges.append(tuple)

Wonder_Boys_G = nx.Graph()
Wonder_Boys_G.add_nodes_from(Wonder_Boys_node_names)
Wonder_Boys_G.add_edges_from(Wonder_Boys_edges)
print(nx.info(Wonder_Boys_G))

# Create male and female groups
Wonder_Boys_female = ['MARILYN', 'MISS SLOVIAK', 'WOMAN', 'OOLA', 'CARRIE MCWHIRTY', 'SARA', 'HANNAH GREEN', 'WAITRESS', 'TANYA', 'AMANDA LEER']
Wonder_Boys_male = []

for m in Wonder_Boys_node_names:
    if m not in Wonder_Boys_female:
        Wonder_Boys_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Wonder_Boys_female:
    gender[n] = 'female'

for n in Wonder_Boys_male:
    gender[n] = 'male'

nx.set_node_attributes(Wonder_Boys_G, gender, 'gender')
print(Wonder_Boys_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Wonder_Boys_G)
print(Movie_networks)


# MUMFORD
print("------Mumford------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Mumford.json", "r", encoding='utf-8') as data:
    Mumford = json.load(data)
print(Mumford)

# Create the movie graph
Mumford_node_names = []
Mumford_edges = []

for i in Mumford['network']['nodes']:
     id = (i['id'])
     Mumford_node_names.append(id)

for i in Mumford['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Mumford_edges.append(tuple)

Mumford_G = nx.Graph()
Mumford_G.add_nodes_from(Mumford_node_names)
Mumford_G.add_edges_from(Mumford_edges)
print(nx.info(Mumford_G))

# Create male and female groups
Mumford_female = ['NESSA', 'LANDLADY', 'LILY', 'ALTHEA', 'SHEELER', 'MRS COOK', 'KATIE', 'SOFIE']
Mumford_male = []

for m in Mumford_node_names:
    if m not in Mumford_female:
        Mumford_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Mumford_female:
    gender[n] = 'female'

for n in Mumford_male:
    gender[n] = 'male'

nx.set_node_attributes(Mumford_G, gender, 'gender')
print(Mumford_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Mumford_G)
print(Movie_networks)


# NICK OF TIME
print("------Nick_Of_Time------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Nick_Of_Time.json", "r", encoding='utf-8') as data:
    Nick_Of_Time = json.load(data)
print(Nick_Of_Time)

# Create the movie graph
Nick_Of_Time_node_names = []
Nick_Of_Time_edges = []

for i in Nick_Of_Time['network']['nodes']:
     id = (i['id'])
     Nick_Of_Time_node_names.append(id)

for i in Nick_Of_Time['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Nick_Of_Time_edges.append(tuple)

Nick_Of_Time_G = nx.Graph()
Nick_Of_Time_G.add_nodes_from(Nick_Of_Time_node_names)
Nick_Of_Time_G.add_edges_from(Nick_Of_Time_edges)
print(nx.info(Nick_Of_Time_G))

# Create male and female groups
Nick_Of_Time_female = ['MR JONES', 'KRISTA', 'WAITRESS', 'ELEANOR GRANT', 'WOMAN', 'LYNN', 'LITTLE GIRL', 'MS JONES', 'IRENE']
Nick_Of_Time_male = []

for m in Nick_Of_Time_node_names:
    if m not in Nick_Of_Time_female:
        Nick_Of_Time_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Nick_Of_Time_female:
    gender[n] = 'female'

for n in Nick_Of_Time_male:
    gender[n] = 'male'

nx.set_node_attributes(Nick_Of_Time_G, gender, 'gender')
print(Nick_Of_Time_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Nick_Of_Time_G)
print(Movie_networks)


# LIFE
print("------Life------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Life.json", "r", encoding='utf-8') as data:
    Life = json.load(data)
print(Life)

# Create the movie graph
Life_node_names = []
Life_edges = []

for i in Life['network']['nodes']:
     id = (i['id'])
     Life_node_names.append(id)

for i in Life['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Life_edges.append(tuple)

Life_G = nx.Graph()
Life_G.add_nodes_from(Life_node_names)
Life_G.add_edges_from(Life_edges)
print(nx.info(Life_G))

# Create male and female groups
Life_female = ['MAMA', 'COCKTAIL WAITRESS', 'SYLVIA', 'WAITRESS', 'MRS ABERNATHY', 'MAMA GIBSON', 'DAISY', 'NURSE HUMPHRIES', 'YVETTE']
Life_male = []

for m in Life_node_names:
    if m not in Life_female:
        Life_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Life_female:
    gender[n] = 'female'

for n in Life_male:
    gender[n] = 'male'

nx.set_node_attributes(Life_G, gender, 'gender')
print(Life_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Life_G)
print(Movie_networks)


# MY BEST FRIEND's WEDDING
print("------Best_Friend_Wedding------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Best_Friend_Wedding.json", "r", encoding='utf-8') as data:
    Best_Friend_Wedding = json.load(data)
print(Best_Friend_Wedding)

# Create the movie graph
Best_Friend_Wedding_node_names = []
Best_Friend_Wedding_edges = []

for i in Best_Friend_Wedding['network']['nodes']:
     id = (i['id'])
     Best_Friend_Wedding_node_names.append(id)

for i in Best_Friend_Wedding['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Best_Friend_Wedding_edges.append(tuple)

Best_Friend_Wedding_G = nx.Graph()
Best_Friend_Wedding_G.add_nodes_from(Best_Friend_Wedding_node_names)
Best_Friend_Wedding_G.add_edges_from(Best_Friend_Wedding_edges)
print(nx.info(Best_Friend_Wedding_G))

# Create male and female groups
Best_Friend_Wedding_female = ['SAMMY', 'WOMAN', 'KIMMY', 'ISABELLE', 'MANDY', 'FLOWER GIRL', 'JULIANNE']
Best_Friend_Wedding_male = []

for m in Best_Friend_Wedding_node_names:
    if m not in Best_Friend_Wedding_female:
        Best_Friend_Wedding_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Best_Friend_Wedding_female:
    gender[n] = 'female'

for n in Best_Friend_Wedding_male:
    gender[n] = 'male'

nx.set_node_attributes(Best_Friend_Wedding_G, gender, 'gender')
print(Best_Friend_Wedding_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Best_Friend_Wedding_G)
print(Movie_networks)


# THE DEVIL's ADVOCATE
print("------Devil_Advocate------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Devil_Advocate.json", "r", encoding='utf-8') as data:
    Devil_Advocate = json.load(data)
print(Devil_Advocate)

# Create the movie graph
Devil_Advocate_node_names = []
Devil_Advocate_edges = []

for i in Devil_Advocate['network']['nodes']:
     id = (i['id'])
     Devil_Advocate_node_names.append(id)

for i in Devil_Advocate['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Devil_Advocate_edges.append(tuple)

Devil_Advocate_G = nx.Graph()
Devil_Advocate_G.add_nodes_from(Devil_Advocate_node_names)
Devil_Advocate_G.add_edges_from(Devil_Advocate_edges)
print(nx.info(Devil_Advocate_G))

# Create male and female groups
Devil_Advocate_female = ['BARBARA', 'REPORTER', 'PAM', 'JACKIE', 'CHRISTABELLA', 'THERAPIST', 'DIANA', 'MRS LOMAX', 'WOMAN JUDGE', 'WOMAN', 'MELISSA', 'DANCER', 'MARY ANN', 'GISELLE']
Devil_Advocate_male = []

for m in Devil_Advocate_node_names:
    if m not in Devil_Advocate_female:
        Devil_Advocate_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Devil_Advocate_female:
    gender[n] = 'female'

for n in Devil_Advocate_male:
    gender[n] = 'male'

nx.set_node_attributes(Devil_Advocate_G, gender, 'gender')
print(Devil_Advocate_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Devil_Advocate_G)
print(Movie_networks)


# BEING JOHN MALKOVICH
print("------John_Malkovich------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/John_Malkovich.json", "r", encoding='utf-8') as data:
    John_Malkovich = json.load(data)
print(John_Malkovich)

# Create the movie graph
John_Malkovich_node_names = []
John_Malkovich_edges = []

for i in John_Malkovich['network']['nodes']:
     id = (i['id'])
     John_Malkovich_node_names.append(id)

for i in John_Malkovich['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        John_Malkovich_edges.append(tuple)

John_Malkovich_G = nx.Graph()
John_Malkovich_G.add_nodes_from(John_Malkovich_node_names)
John_Malkovich_G.add_edges_from(John_Malkovich_edges)
print(nx.info(John_Malkovich_G))

# Create male and female groups
John_Malkovich_female = ['GIRL MALKOVICH', 'FLORIS', 'GLORIA', 'MAXINE', 'LOTTE', 'WOMAN #1']
John_Malkovich_male = []

for m in John_Malkovich_node_names:
    if m not in John_Malkovich_female:
        John_Malkovich_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in John_Malkovich_female:
    gender[n] = 'female'

for n in John_Malkovich_male:
    gender[n] = 'male'

nx.set_node_attributes(John_Malkovich_G, gender, 'gender')
print(John_Malkovich_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(John_Malkovich_G)
print(Movie_networks)


# BODY OF EVIDENCE
print("------Body_Of_Evidence------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Body_Of_Evidence.json", "r", encoding='utf-8') as data:
    Body_Of_Evidence = json.load(data)
print(Body_Of_Evidence)

# Create the movie graph
Body_Of_Evidence_node_names = []
Body_Of_Evidence_edges = []

for i in Body_Of_Evidence['network']['nodes']:
     id = (i['id'])
     Body_Of_Evidence_node_names.append(id)

for i in Body_Of_Evidence['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Body_Of_Evidence_edges.append(tuple)

Body_Of_Evidence_G = nx.Graph()
Body_Of_Evidence_G.add_nodes_from(Body_Of_Evidence_node_names)
Body_Of_Evidence_G.add_edges_from(Body_Of_Evidence_edges)
print(nx.info(Body_Of_Evidence_G))

# Create male and female groups
Body_Of_Evidence_female = ['ESTER', 'MISS SELLERS', 'REBECCA', 'SHARON', 'SECRETARY', 'JOANNE']
Body_Of_Evidence_male = []

for m in Body_Of_Evidence_node_names:
    if m not in Body_Of_Evidence_female:
        Body_Of_Evidence_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Body_Of_Evidence_female:
    gender[n] = 'female'

for n in Body_Of_Evidence_male:
    gender[n] = 'male'

nx.set_node_attributes(Body_Of_Evidence_G, gender, 'gender')
print(Body_Of_Evidence_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Body_Of_Evidence_G)
print(Movie_networks)


# RACHEL GETTING MARRIED
print("------Rachel_Getting_Married------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Rachel_Getting_Married.json", "r", encoding='utf-8') as data:
    Rachel_Getting_Married = json.load(data)
print(Rachel_Getting_Married)

# Create the movie graph
Rachel_Getting_Married_node_names = []
Rachel_Getting_Married_edges = []

for i in Rachel_Getting_Married['network']['nodes']:
     id = (i['id'])
     Rachel_Getting_Married_node_names.append(id)

for i in Rachel_Getting_Married['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Rachel_Getting_Married_edges.append(tuple)

Rachel_Getting_Married_G = nx.Graph()
Rachel_Getting_Married_G.add_nodes_from(Rachel_Getting_Married_node_names)
Rachel_Getting_Married_G.add_edges_from(Rachel_Getting_Married_edges)
print(nx.info(Rachel_Getting_Married_G))

# Create male and female groups
Rachel_Getting_Married_female = ['RACHEL', 'SUSANNA', 'ABBY', 'EMMA', 'KYM', 'NURSE', 'MRS WILLIAMS', 'INTERESTING YOUNG WOMAN', 'CAROL', 'ROSA', 'STYLIST']
Rachel_Getting_Married_male = []

for m in Rachel_Getting_Married_node_names:
    if m not in Rachel_Getting_Married_female:
        Rachel_Getting_Married_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Rachel_Getting_Married_female:
    gender[n] = 'female'

for n in Rachel_Getting_Married_male:
    gender[n] = 'male'

nx.set_node_attributes(Rachel_Getting_Married_G, gender, 'gender')
print(Rachel_Getting_Married_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Rachel_Getting_Married_G)
print(Movie_networks)


# ROCKNROLLA
print("------RocknRolla------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/RocknRolla.json", "r", encoding='utf-8') as data:
    RocknRolla = json.load(data)
print(RocknRolla)

# Create the movie graph
RocknRolla_node_names = []
RocknRolla_edges = []

for i in RocknRolla['network']['nodes']:
     id = (i['id'])
     RocknRolla_node_names.append(id)

for i in RocknRolla['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        RocknRolla_edges.append(tuple)

RocknRolla_G = nx.Graph()
RocknRolla_G.add_nodes_from(RocknRolla_node_names)
RocknRolla_G.add_edges_from(RocknRolla_edges)
print(nx.info(RocknRolla_G))

# Create male and female groups
RocknRolla_female = ['NURSE', 'STELLA', 'DOLLY', 'JACKIE', 'SECRETARY']
RocknRolla_male = []

for m in RocknRolla_node_names:
    if m not in RocknRolla_female:
        RocknRolla_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in RocknRolla_female:
    gender[n] = 'female'

for n in RocknRolla_male:
    gender[n] = 'male'

nx.set_node_attributes(RocknRolla_G, gender, 'gender')
print(RocknRolla_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(RocknRolla_G)
print(Movie_networks)


# ALI
print("------Ali------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Ali.json", "r", encoding='utf-8') as data:
    Ali = json.load(data)
print(Ali)

# Create the movie graph
Ali_node_names = []
Ali_edges = []

for i in Ali['network']['nodes']:
     id = (i['id'])
     Ali_node_names.append(id)

for i in Ali['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Ali_edges.append(tuple)

Ali_G = nx.Graph()
Ali_G.add_nodes_from(Ali_node_names)
Ali_G.add_edges_from(Ali_edges)
print(nx.info(Ali_G))

# Create male and female groups
Ali_female = ['ORTF INTERVIEWER', 'IRENE', 'BETTY SHABAZZ', 'SONJI', 'ODESSA CLAY', 'GIRL', 'BELINDA', 'VERONICA', 'LANDLADY']
Ali_male = []

for m in Ali_node_names:
    if m not in Ali_female:
        Ali_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Ali_female:
    gender[n] = 'female'

for n in Ali_male:
    gender[n] = 'male'

nx.set_node_attributes(Ali_G, gender, 'gender')
print(Ali_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Ali_G)
print(Movie_networks)


# NINJA ASSASSIN
print("------Ninja_Assassin------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Ninja_Assassin.json", "r", encoding='utf-8') as data:
    Ninja_Assassin = json.load(data)
print(Ninja_Assassin)

# Create the movie graph
Ninja_Assassin_node_names = []
Ninja_Assassin_edges = []

for i in Ninja_Assassin['network']['nodes']:
     id = (i['id'])
     Ninja_Assassin_node_names.append(id)

for i in Ninja_Assassin['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Ninja_Assassin_edges.append(tuple)

Ninja_Assassin_G = nx.Graph()
Ninja_Assassin_G.add_nodes_from(Ninja_Assassin_node_names)
Ninja_Assassin_G.add_edges_from(Ninja_Assassin_edges)
print(nx.info(Ninja_Assassin_G))

# Create male and female groups
Ninja_Assassin_female = ['LANDLADY', 'MIKA', 'KIRIKO', 'PRETTY WOMAN', 'MRS SABATIN']
Ninja_Assassin_male = []

for m in Ninja_Assassin_node_names:
    if m not in Ninja_Assassin_female:
        Ninja_Assassin_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Ninja_Assassin_female:
    gender[n] = 'female'

for n in Ninja_Assassin_male:
    gender[n] = 'male'

nx.set_node_attributes(Ninja_Assassin_G, gender, 'gender')
print(Ninja_Assassin_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Ninja_Assassin_G)
print(Movie_networks)


# MIRRORS
print("------Mirrors------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Mirrors.json", "r", encoding='utf-8') as data:
    Mirrors = json.load(data)
print(Mirrors)

# Create the movie graph
Mirrors_node_names = []
Mirrors_edges = []

for i in Mirrors['network']['nodes']:
     id = (i['id'])
     Mirrors_node_names.append(id)

for i in Mirrors['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Mirrors_edges.append(tuple)

Mirrors_G = nx.Graph()
Mirrors_G.add_nodes_from(Mirrors_node_names)
Mirrors_G.add_edges_from(Mirrors_edges)
print(nx.info(Mirrors_G))

# Create male and female groups
Mirrors_female = ['DAISY', "AMY'S REFLECTION", 'SISTER ANNA', 'SISTER', 'ANNA', 'ROSA', 'AMY OS', "JIMMY'S MOTHER", 'AMY', 'WOMAN', 'MRS LEWIS', 'ANGELA']
Mirrors_male = []

for m in Mirrors_node_names:
    if m not in Mirrors_female:
        Mirrors_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Mirrors_female:
    gender[n] = 'female'

for n in Mirrors_male:
    gender[n] = 'male'

nx.set_node_attributes(Mirrors_G, gender, 'gender')
print(Mirrors_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Mirrors_G)
print(Movie_networks)



# JASON X
print("------Jason_X------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Jason_X.json", "r", encoding='utf-8') as data:
    Jason_X = json.load(data)
print(Jason_X)

# Create the movie graph
Jason_X_node_names = []
Jason_X_edges = []

for i in Jason_X['network']['nodes']:
     id = (i['id'])
     Jason_X_node_names.append(id)

for i in Jason_X['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Jason_X_edges.append(tuple)

Jason_X_G = nx.Graph()
Jason_X_G.add_nodes_from(Jason_X_node_names)
Jason_X_G.add_edges_from(Jason_X_edges)
print(nx.info(Jason_X_G))

# Create male and female groups
Jason_X_female = ['ADRIENNE', 'KAY-EM 14', 'BRIGGS', 'GIRL', 'JANESSA', 'AZRAEL']
Jason_X_male = []

for m in Jason_X_node_names:
    if m not in Jason_X_female:
        Jason_X_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Jason_X_female:
    gender[n] = 'female'

for n in Jason_X_male:
    gender[n] = 'male'

nx.set_node_attributes(Jason_X_G, gender, 'gender')
print(Jason_X_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Jason_X_G)
print(Movie_networks)


# THE BATTLE OF THE SHAKER HEIGHTS
print("------Battle_Of_Shaker_Heights------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Battle_Of_Shaker_Heights.json", "r", encoding='utf-8') as data:
    Battle_Of_Shaker_Heights = json.load(data)
print(Battle_Of_Shaker_Heights)

# Create the movie graph
Battle_Of_Shaker_Heights_node_names = []
Battle_Of_Shaker_Heights_edges = []

for i in Battle_Of_Shaker_Heights['network']['nodes']:
     id = (i['id'])
     Battle_Of_Shaker_Heights_node_names.append(id)

for i in Battle_Of_Shaker_Heights['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Battle_Of_Shaker_Heights_edges.append(tuple)

Battle_Of_Shaker_Heights_G = nx.Graph()
Battle_Of_Shaker_Heights_G.add_nodes_from(Battle_Of_Shaker_Heights_node_names)
Battle_Of_Shaker_Heights_G.add_edges_from(Battle_Of_Shaker_Heights_edges)
print(nx.info(Battle_Of_Shaker_Heights_G))

# Create male and female groups
Battle_Of_Shaker_Heights_female = ['HOLMSTEAD', 'TABBY', 'GIRL', 'STUDENT 2', 'EVE', 'MATHILDA', 'PRINCIPAL', "LANCE'S MOM", 'CHARLIE', 'XIOU-XIOU', 'WOMAN', 'SECRETARY', 'KELLY', 'MINNIE', 'SARAH']
Battle_Of_Shaker_Heights_male = []

for m in Battle_Of_Shaker_Heights_node_names:
    if m not in Battle_Of_Shaker_Heights_female:
        Battle_Of_Shaker_Heights_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Battle_Of_Shaker_Heights_female:
    gender[n] = 'female'

for n in Battle_Of_Shaker_Heights_male:
    gender[n] = 'male'

nx.set_node_attributes(Battle_Of_Shaker_Heights_G, gender, 'gender')
print(Battle_Of_Shaker_Heights_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Battle_Of_Shaker_Heights_G)
print(Movie_networks)



# AMERICAN GANGSTER
print("------American_Gangster------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/American_Gangster.json", "r", encoding='utf-8') as data:
    American_Gangster = json.load(data)
print(American_Gangster)

# Create the movie graph
American_Gangster_node_names = []
American_Gangster_edges = []

for i in American_Gangster['network']['nodes']:
     id = (i['id'])
     American_Gangster_node_names.append(id)

for i in American_Gangster['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        American_Gangster_edges.append(tuple)

American_Gangster_G = nx.Graph()
American_Gangster_G.add_nodes_from(American_Gangster_node_names)
American_Gangster_G.add_edges_from(American_Gangster_edges)
print(nx.info(American_Gangster_G))

# Create male and female groups
American_Gangster_female = ['CHARLENE', 'LAURIE', 'SHEILA', 'ANA', 'JACKIE']
American_Gangster_male = []

for m in American_Gangster_node_names:
    if m not in American_Gangster_female:
        American_Gangster_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in American_Gangster_female:
    gender[n] = 'female'

for n in American_Gangster_male:
    gender[n] = 'male'

nx.set_node_attributes(American_Gangster_G, gender, 'gender')
print(American_Gangster_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(American_Gangster_G)
print(Movie_networks)


# PIRATES OF CARIBBEAN - The Curse of the Black Pearl
print("------Pirates_Of_The Caribbean------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Pirates_Of_The Caribbean.json", "r", encoding='utf-8') as data:
    Pirates_Of_The_Caribbean = json.load(data)
print(Pirates_Of_The_Caribbean)

# Create the movie graph
Pirates_Of_The_Caribbean_node_names = []
Pirates_Of_The_Caribbean_edges = []

for i in Pirates_Of_The_Caribbean['network']['nodes']:
     id = (i['id'])
     Pirates_Of_The_Caribbean_node_names.append(id)

for i in Pirates_Of_The_Caribbean['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Pirates_Of_The_Caribbean_edges.append(tuple)

Pirates_Of_The_Caribbean_G = nx.Graph()
Pirates_Of_The_Caribbean_G.add_nodes_from(Pirates_Of_The_Caribbean_node_names)
Pirates_Of_The_Caribbean_G.add_edges_from(Pirates_Of_The_Caribbean_edges)
print(nx.info(Pirates_Of_The_Caribbean_G))

# Create male and female groups
Pirates_Of_The_Caribbean_female = ['ELIZABETH', 'ANAMARIA', 'ESTRELLA']
Pirates_Of_The_Caribbean_male = []

for m in Pirates_Of_The_Caribbean_node_names:
    if m not in Pirates_Of_The_Caribbean_female:
        Pirates_Of_The_Caribbean_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Pirates_Of_The_Caribbean_female:
    gender[n] = 'female'

for n in Pirates_Of_The_Caribbean_male:
    gender[n] = 'male'

nx.set_node_attributes(Pirates_Of_The_Caribbean_G, gender, 'gender')
print(Pirates_Of_The_Caribbean_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Pirates_Of_The_Caribbean_G)
print(Movie_networks)


# TWELVE AND HOLDING
print("------Twelve_And_Holding------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Twelve_And_Holding.json", "r", encoding='utf-8') as data:
    Twelve_And_Holding = json.load(data)
print(Twelve_And_Holding)

# Create the movie graph
Twelve_And_Holding_node_names = []
Twelve_And_Holding_edges = []

for i in Twelve_And_Holding['network']['nodes']:
     id = (i['id'])
     Twelve_And_Holding_node_names.append(id)

for i in Twelve_And_Holding['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Twelve_And_Holding_edges.append(tuple)

Twelve_And_Holding_G = nx.Graph()
Twelve_And_Holding_G.add_nodes_from(Twelve_And_Holding_node_names)
Twelve_And_Holding_G.add_edges_from(Twelve_And_Holding_edges)
print(nx.info(Twelve_And_Holding_G))

# Create male and female groups
Twelve_And_Holding_female = ['TEACHER', 'NURSE', 'MALEE', 'MOTHER # 1', 'HALEY', 'DEBBIE', 'ASHLEY', 'SARA', 'GRACE']
Twelve_And_Holding_male = []

for m in Twelve_And_Holding_node_names:
    if m not in Twelve_And_Holding_female:
        Twelve_And_Holding_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Twelve_And_Holding_female:
    gender[n] = 'female'

for n in Twelve_And_Holding_male:
    gender[n] = 'male'

nx.set_node_attributes(Twelve_And_Holding_G, gender, 'gender')
print(Twelve_And_Holding_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Twelve_And_Holding_G)
print(Movie_networks)



# REVOLUTIONARY ROAD
print("------Revolutionary_Road------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Revolutionary_Road.json", "r", encoding='utf-8') as data:
    Revolutionary_Road = json.load(data)
print(Revolutionary_Road)

# Create the movie graph
Revolutionary_Road_node_names = []
Revolutionary_Road_edges = []

for i in Revolutionary_Road['network']['nodes']:
     id = (i['id'])
     Revolutionary_Road_node_names.append(id)

for i in Revolutionary_Road['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Revolutionary_Road_edges.append(tuple)

Revolutionary_Road_G = nx.Graph()
Revolutionary_Road_G.add_nodes_from(Revolutionary_Road_node_names)
Revolutionary_Road_G.add_edges_from(Revolutionary_Road_edges)
print(nx.info(Revolutionary_Road_G))

# Create male and female groups
Revolutionary_Road_female = ['RECEPTIONIST', 'MAUREEN', 'MILLY', 'JENNIFER', 'APRIL', 'MRS GIVINGS']
Revolutionary_Road_male = []

for m in Revolutionary_Road_node_names:
    if m not in Revolutionary_Road_female:
        Revolutionary_Road_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Revolutionary_Road_female:
    gender[n] = 'female'

for n in Revolutionary_Road_male:
    gender[n] = 'male'

nx.set_node_attributes(Revolutionary_Road_G, gender, 'gender')
print(Revolutionary_Road_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Revolutionary_Road_G)
print(Movie_networks)


# THE BELIVER
print("------The_Believer------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/The_Believer.json", "r", encoding='utf-8') as data:
    The_Believer = json.load(data)
print(The_Believer)

# Create the movie graph
The_Believer_node_names = []
The_Believer_edges = []

for i in The_Believer['network']['nodes']:
     id = (i['id'])
     The_Believer_node_names.append(id)

for i in The_Believer['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        The_Believer_edges.append(tuple)

The_Believer_G = nx.Graph()
The_Believer_G.add_nodes_from(The_Believer_node_names)
The_Believer_G.add_edges_from(The_Believer_edges)
print(nx.info(The_Believer_G))

# Create male and female groups
The_Believer_female = ['RUMANIAN WOMAN', 'WOMAN', 'LINDA', 'MRS MOEBIUS', 'CARLA', 'LINA MOEBIUS', 'ENRAGED WIFE', 'MIRIAM', 'LARGE WOMAN', 'LINA', 'CINDY']
The_Believer_male = []

for m in The_Believer_node_names:
    if m not in The_Believer_female:
        The_Believer_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in The_Believer_female:
    gender[n] = 'female'

for n in The_Believer_male:
    gender[n] = 'male'

nx.set_node_attributes(The_Believer_G, gender, 'gender')
print(The_Believer_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(The_Believer_G)
print(Movie_networks)



# UP
print("------Up------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Up.json", "r", encoding='utf-8') as data:
    Up = json.load(data)
print(Up)

# Create the movie graph
Up_node_names = []
Up_edges = []

for i in Up['network']['nodes']:
     id = (i['id'])
     Up_node_names.append(id)

for i in Up['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Up_edges.append(tuple)

Up_G = nx.Graph()
Up_G.add_nodes_from(Up_node_names)
Up_G.add_edges_from(Up_edges)
print(nx.info(Up_G))

# Create male and female groups
Up_female = ['YOUNG ELLIE', 'GIRL']
Up_male = []

for m in Up_node_names:
    if m not in Up_female:
        Up_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Up_female:
    gender[n] = 'female'

for n in Up_male:
    gender[n] = 'male'

nx.set_node_attributes(Up_G, gender, 'gender')
print(Up_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Up_G)
print(Movie_networks)


# ORPHAN
print("------Orphan------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Orphan.json", "r", encoding='utf-8') as data:
    Orphan = json.load(data)
print(Orphan)

# Create the movie graph
Orphan_node_names = []
Orphan_edges = []

for i in Orphan['network']['nodes']:
     id = (i['id'])
     Orphan_node_names.append(id)

for i in Orphan['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Orphan_edges.append(tuple)

Orphan_G = nx.Graph()
Orphan_G.add_nodes_from(Orphan_node_names)
Orphan_G.add_edges_from(Orphan_edges)
print(nx.info(Orphan_G))

# Create male and female groOrphans
Orphan_female = ['ESTEER', 'KATE -', 'BRENDA', 'ESTHER -', 'SISTER ABIGAIL -', 'DORIS', 'NURSE', 'ESTBER', 'KATE-', 'SISTER JUDITH', 'RECEPTIONIST #2', 'ESTSER', 'YOLANDA', 'SISTER ABIGAIL', 'ESTHER', 'ESTHER-', 'KATE', 'RECEPTIONIST #1', 'JOYCE']
Orphan_male = []

for m in Orphan_node_names:
    if m not in Orphan_female:
        Orphan_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Orphan_female:
    gender[n] = 'female'

for n in Orphan_male:
    gender[n] = 'male'

nx.set_node_attributes(Orphan_G, gender, 'gender')
print(Orphan_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Orphan_G)
print(Movie_networks)


# VANILLA SKY
print("------Vanilla_Sky------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Vanilla_Sky.json", "r", encoding='utf-8') as data:
    Vanilla_Sky = json.load(data)
print(Vanilla_Sky)

# Create the movie graph
Vanilla_Sky_node_names = []
Vanilla_Sky_edges = []

for i in Vanilla_Sky['network']['nodes']:
     id = (i['id'])
     Vanilla_Sky_node_names.append(id)

for i in Vanilla_Sky['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Vanilla_Sky_edges.append(tuple)

Vanilla_Sky_G = nx.Graph()
Vanilla_Sky_G.add_nodes_from(Vanilla_Sky_node_names)
Vanilla_Sky_G.add_edges_from(Vanilla_Sky_edges)
print(nx.info(Vanilla_Sky_G))

# Create male and female groVanilla_Skys
Vanilla_Sky_female = ['LIBBY', 'WOMAN', 'EMMA THE CATERER', 'JULIANNA', 'DEARBORN', 'BEATRICE', 'JUL IANNA', 'RACHEL', 'SOFIA']
Vanilla_Sky_male = []

for m in Vanilla_Sky_node_names:
    if m not in Vanilla_Sky_female:
        Vanilla_Sky_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Vanilla_Sky_female:
    gender[n] = 'female'

for n in Vanilla_Sky_male:
    gender[n] = 'male'

nx.set_node_attributes(Vanilla_Sky_G, gender, 'gender')
print(Vanilla_Sky_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Vanilla_Sky_G)
print(Movie_networks)



# JIMMY AND JUDY
print("------Jimmy_And_Judy------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Jimmy_And_Judy.json", "r", encoding='utf-8') as data:
    Jimmy_And_Judy = json.load(data)
print(Jimmy_And_Judy)

# Create the movie graph
Jimmy_And_Judy_node_names = []
Jimmy_And_Judy_edges = []

for i in Jimmy_And_Judy['network']['nodes']:
     id = (i['id'])
     Jimmy_And_Judy_node_names.append(id)

for i in Jimmy_And_Judy['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Jimmy_And_Judy_edges.append(tuple)

Jimmy_And_Judy_G = nx.Graph()
Jimmy_And_Judy_G.add_nodes_from(Jimmy_And_Judy_node_names)
Jimmy_And_Judy_G.add_edges_from(Jimmy_And_Judy_edges)
print(nx.info(Jimmy_And_Judy_G))

# Create male and female groJimmy_And_Judys
Jimmy_And_Judy_female = ['HAZEL', 'JUDY', "JIMMY'S MOM", 'PROSTITUTE']
Jimmy_And_Judy_male = []

for m in Jimmy_And_Judy_node_names:
    if m not in Jimmy_And_Judy_female:
        Jimmy_And_Judy_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Jimmy_And_Judy_female:
    gender[n] = 'female'

for n in Jimmy_And_Judy_male:
    gender[n] = 'male'

nx.set_node_attributes(Jimmy_And_Judy_G, gender, 'gender')
print(Jimmy_And_Judy_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Jimmy_And_Judy_G)
print(Movie_networks)


# BLACK SNAKE MOAN
print("------Black_Snake_Moan------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/Black_Snake_Moan.json", "r", encoding='utf-8') as data:
    Black_Snake_Moan = json.load(data)
print(Black_Snake_Moan)

# Create the movie graph
Black_Snake_Moan_node_names = []
Black_Snake_Moan_edges = []

for i in Black_Snake_Moan['network']['nodes']:
     id = (i['id'])
     Black_Snake_Moan_node_names.append(id)

for i in Black_Snake_Moan['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        Black_Snake_Moan_edges.append(tuple)

Black_Snake_Moan_G = nx.Graph()
Black_Snake_Moan_G.add_nodes_from(Black_Snake_Moan_node_names)
Black_Snake_Moan_G.add_edges_from(Black_Snake_Moan_edges)
print(nx.info(Black_Snake_Moan_G))

# Create male and female groBlack_Snake_Moans
Black_Snake_Moan_female = ['KELL', 'MAYELLA', 'ROSE', 'ANGELA', 'GIRL', 'WAITRESS', 'JESSE', 'RAE', 'SANDY', 'ELLA MAE']
Black_Snake_Moan_male = []

for m in Black_Snake_Moan_node_names:
    if m not in Black_Snake_Moan_female:
        Black_Snake_Moan_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in Black_Snake_Moan_female:
    gender[n] = 'female'

for n in Black_Snake_Moan_male:
    gender[n] = 'male'

nx.set_node_attributes(Black_Snake_Moan_G, gender, 'gender')
print(Black_Snake_Moan_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(Black_Snake_Moan_G)
print(Movie_networks)


# HOUSE OF 1000 CORPSES
print("------House_Of_Corpses------")

# Read the json data in Python - processed in a dictionary structure
with open("data/movies/House_Of_Corpses.json", "r", encoding='utf-8') as data:
    House_Of_Corpses = json.load(data)
print(House_Of_Corpses)

# Create the movie graph
House_Of_Corpses_node_names = []
House_Of_Corpses_edges = []

for i in House_Of_Corpses['network']['nodes']:
     id = (i['id'])
     House_Of_Corpses_node_names.append(id)

for i in House_Of_Corpses['network']['edges']:
        s = (i['source'])
        t = (i['target'])
        w = (i['weight'])
        tuple = (s, t, {'w':w})
        House_Of_Corpses_edges.append(tuple)

House_Of_Corpses_G = nx.Graph()
House_Of_Corpses_G.add_nodes_from(House_Of_Corpses_node_names)
House_Of_Corpses_G.add_edges_from(House_Of_Corpses_edges)
print(nx.info(House_Of_Corpses_G))

# Create male and female groHouse_Of_Corpsess
House_Of_Corpses_female = ['DENISE', 'BABY', 'MOTHER', 'MARY', 'GLORIA STUART', 'WIFE']
House_Of_Corpses_male = []

for m in House_Of_Corpses_node_names:
    if m not in House_Of_Corpses_female:
        House_Of_Corpses_male.append(m)

# Assign gender property to each nodes
gender = {}
for n in House_Of_Corpses_female:
    gender[n] = 'female'

for n in House_Of_Corpses_male:
    gender[n] = 'male'

nx.set_node_attributes(House_Of_Corpses_G, gender, 'gender')
print(House_Of_Corpses_G.nodes(data=True))

# Add the graph to movie network list
Movie_networks.append(House_Of_Corpses_G)
print(Movie_networks)

print(len(Movie_networks))