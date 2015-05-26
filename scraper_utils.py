# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2

def openURL(url):
	response = urllib2.urlopen(url)
	html = response.read()
	return BeautifulSoup(html)

#available generation, games
def getAvailable(name):
	name_upper = name[0].upper() + name[1:]
	page = "http://bulbapedia.bulbagarden.net/wiki/" + name_upper +"_(Pokémon)"
	page_tree = openURL(page)

	table = page_tree.find(id="Game_locations").parent.next_sibling.next_sibling
	games = [unicode(el.string) for el in table.find_all("span")]

	first_available = unicode(table.find("small").string)

	return (first_available, games)
	# table.find("span")

def generateTypeStrengths(row, types):
	typeCor = {}
	typeCor["strongEffect"] = []
	typeCor["weakEffect"] = []
	typeCor["noEffect"] = []
	typeCor["normalEffect"] = []

	index = 0
	for el in row.find_all("td"):
		strength = unicode(el.string[1:2])
		if strength == u"1":
			typeCor["normalEffect"].append(types[index])
		elif strength == "2":
			typeCor["strongEffect"].append(types[index])
		elif strength == "0":
			typeCor["noEffect"].append(types[index])
		else:
			typeCor["weakEffect"].append(types[index])
		index += 1
	return typeCor

def getTypeMatrix(generation):
	url = "http://bulbapedia.bulbagarden.net/wiki/Type"
	if (generation < 6):
		url += "/Type_chart"
	page_tree = openURL(url)
	type_table = page_tree.find(id="mw-content-text").find_all("table")[1 + (generation == 1)]
	type_matrix = {}
	rows = type_table.find_all("tr")
	types = [str(el["title"]) for el in rows[1].find_all("a")]
	index = 0
	for row in rows[2:-1]:
		#print(row)
		type_matrix[types[index]] = generateTypeStrengths(row, types) 
		index += 1
	return (types, type_matrix)

