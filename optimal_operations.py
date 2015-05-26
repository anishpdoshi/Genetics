#Inspired by http://www.ai-junkie.com/ga/intro/gat1.html.
#Tries to create a sequence of numbers and operations that, if valid,
#evaluates to be as close to a target number as possible


import sys
from random import randint, uniform
import genetics_lab
import time

#REPRESENTATION: 
"""
1 - 9 (binary equivalents) (fuck zero)
+ : 1010
- : 1011
* : 1100
/ : 1101
"""
operators = "+-*/"

#The number we wish to get as close to as possible
TARGET_NUM = 22.3
FITNESS_TABLE = {}
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.001
SHORT_SCALING = 0.995

#Parses and sanitizes encoding into string of operations
def encoding_to_operations(encoding):
	operations = "" #build from right to left
	lastOneNum = False #numbers and operations must alternate
	for i in range(0, 9):
		LSN = encoding & 0b1111 #least significant nibble
		if LSN >= 1 and LSN <= 9 and not lastOneNum:
			operations = str(LSN) + operations
			lastOneNum = True
		elif (LSN >= 10 and LSN <= 13 and lastOneNum):
			operations = operators[LSN - 10] + operations
			lastOneNum = False
		encoding = encoding >> 4
	if (not lastOneNum):
		operations = operations[1:]
	if operations=="":
		operations = "0"
	return operations	

def fitness(encoding):
	if (encoding in FITNESS_TABLE):
		return FITNESS_TABLE[encoding]
	raw_ops = encoding_to_operations(encoding)
	encoded_val = eval(raw_ops)

	difference = abs(encoded_val - TARGET_NUM)
	if difference == 0:
		print("success! - member is " + encoding_to_operations(encoding))
		sys.exit(0)
	else:
		fitness_val = (1.0 / difference) * pow(SHORT_SCALING, len(raw_ops))
		FITNESS_TABLE[encoding] = 1.0 / difference
		return 1.0 / difference

def create_random_gene():
	return randint(0, pow(2, 36) - 1)

def output(gene):
	return genetics_lab.gene_string(gene) + " -> " + encoding_to_operations(gene) +  " -> " + str(fitness(gene))

genetics_lab.run_genetic_algorithm(100, 36, 0.01, 0.7, 10, fitness, create_random_gene, output, 100, verbose=False)







