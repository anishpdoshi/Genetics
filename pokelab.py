from __future__ import print_function
import requests
import pprint
from random import randint, uniform
from pokemon import Pokemon
from genetics_lab import run_genetic_algorithm, gene_string
from scraper_utils import getTypeMatrix

"""trickies (for scraping):
Nidoran-f
Nidoran-m
Mr-mime
Ho-oh
Deoxys-normal
Wormadam-plant
Mime-jr
Porygon-z
Giratina-altered
Shaymin-land
Basculin-red-striped
Darmanitan-standard
Tornadus-incarnate
Thundurus-incarnate
Landorus-incarnate
Keldeo-ordinary
Meloetta-aria
Meowstic-male
Pumpkaboo-average
Gourgeist-average
"""

GENERATION = 4

def scrape_data():
	x = open("inst2.txt", "w+")
	try:
		for i in range(1, 730):
			data =requests.get("http://pokeapi.co/api/v1/pokemon/" + str(i)).json()
			p = Pokemon(data)
			p.id = i
			print(str(p.__dict__), file=x)
			print(str(data["name"]).upper() +" has been successfully created! Id: " + str(i) + ", Generation: " + str(p.generation))

	finally:
		x.close()

def query(section, num):
	response = requests.get("http://pokeapi.co/api/v1/" + section + "/" + str(num))
	pprint.pprint(response.json())


def initialize_pokedex():
	x = open("inst2.txt", "r")
	pokedex = {}
	for line in x:
		pk = Pokemon(eval(line.rstrip()))
		pokedex[pk.id] = pk
	x.close()
	return pokedex


FITNESS_TABLE = {}
typematrix = {}
# scrape_data()
pokedex = initialize_pokedex()
print("Pokedex initialized.")
types, typematrix = getTypeMatrix(GENERATION)
print("Types initialized.")

def encoding_to_team(encoding):
	team = set()
	shifting = encoding
	mask = 1023 # 0b1111111111
	for i in range(6):
		leftmost = shifting & mask
		if leftmost <= 700 and leftmost in pokedex:
			team.add(pokedex[leftmost])
		shifting = shifting >> 10
	return team

#Performs team fitness analysis on a given pokemon team, represented as an encoding
def fitness(encoding):
	if encoding in FITNESS_TABLE:
		return FITNESS_TABLE[encoding]

	team = encoding_to_team(encoding) 
	
	fitness_val = 12
	typeset = set()
	for pk in team:
		for t in pk.types:
			typeset.add(t)
		fitness_val += pk.statsum()
	fitness_val *= len(typeset)

	FITNESS_TABLE[encoding] = fitness_val
	return fitness_val

def output(gene):
	team_list = [str(x.name) for x in encoding_to_team(gene)]
	return str(team_list) +  " -> " + str(fitness(gene))

def optimized_team():
	random_gene = lambda : randint(0, pow(2, 60) - 1)
	run_genetic_algorithm(100, 60, 0.01, 0.7, 3000, fitness, random_gene, output, 400000)

optimized_team()