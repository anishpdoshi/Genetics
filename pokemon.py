# -*- coding: utf-8 -*-

#from scraper_utils import getAvailable

#Represents a pokemon
class Pokemon:

	def __init__(self, data):
		
		if (data):
			#Name and generations
			self.name = str(data["name"])
			#self.generation, self.games = getAvailable(str(self.name))

			#Stats
			self.attack = data["attack"]
			self.defense = data["defense"]
			self.hp = data["hp"]
			self.sp_atk = data["sp_atk"]
			self.sp_def = data["sp_def"]
			self.speed = data["speed"]

			self.weight = int(data["weight"])

			self.types = [el for el in data["types"]]
			self.id = data["id"]

			#To add trade support, just
			if self.id <= 151:
				self.generation = 1
			elif self.id <= 251:
				self.generation = 2
			elif self.id <= 386:
				self.generation = 3
			elif self.id <= 493:
				self.generation = 4
			elif self.id <= 649:
				self.generation = 5
			else:
				self.generation = 6

			#self.id WILL NOT BE REAL ID

			#THIS WOULD BE REAL ID
			
	def statsum(self):
		return self.attack + self.defense + self.speed + \
		self.sp_atk + self.sp_def + self.hp		

	def __str__(self):
		desc = "\n" + self.name.upper() + "  " + str(self.types) + "\n"
		desc += "\tAttack: " + str(self.attack) + "\n"
		desc += "\tSpecial Attack: " + str(self.sp_atk) + "\n"
		desc += "\tDefense: " + str(self.defense) + "\n"
		desc += "\tSpecial Defense: " + str(self.sp_def) + "\n"
		desc += "\tHP: " + str(self.hp) + "\n"
		desc += "\tSpeed: " + str(self.speed) + "\n"
		return desc


