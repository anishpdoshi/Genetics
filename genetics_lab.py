"""
Framework for genetic algorithms. Useful for optimization of solutions
for which fitness evaluation relies on constraints that are not easily
or direcely modifiable. Uses binary literals of of any length.
"""

from random import randint, uniform

#Params (w/ default values):
POP_SIZE = 100
ENCODING_LENGTH = 6 #(10 bytes)
MUTATION_RATE = 0.001
CROSSOVER_RATE = 0.7
NUM_GENERATIONS = 15
# fitness

def gene_string(encoding):
	return format(encoding, "#0" + str(ENCODING_LENGTH) + "b")

def roulette_select(population):
	pie_size = sum([fitness(member) for member in population])
	spin = uniform(0, pie_size)
	curr = 0
	for member in population: 
		curr += fitness(member)
		if curr > spin:
			return member

def crossover(memberA, memberB):
	flip_index = ENCODING_LENGTH - randint(0, ENCODING_LENGTH - 1)
	remainingA = (memberA >> flip_index) << flip_index
	crossA = remainingA ^ memberA
	remainingB = (memberB >> flip_index) << flip_index
	crossB = remainingB ^ memberB
	return (remainingA + crossB, remainingB + crossA)

def mutate(member):
	mask = 0b1
	for i in range(ENCODING_LENGTH):
		if (uniform(0, 1) <= MUTATION_RATE):
			member = member ^ mask
		mask = mask << 1
	return member

def mate_pair(population):
	(memberA, memberB) = \
	(roulette_select(population), roulette_select(population))

	if uniform(0, 1) <= CROSSOVER_RATE:
		memberA, memberB = crossover(memberA, memberB)
	
	memberA = mutate(memberA)
	memberB = mutate(memberB)

	return (memberA, memberB)

def average_fitness(population):
	total = sum([fitness(member) for member in population])
	# print(total)
	return total / float(len(population))

def max_member(population):
	max_fitness = fitness(population[0])
	alpha = population[0]
	for member in population:
		mem_fit = fitness(member)
		if mem_fit > max_fitness:
			alpha = member
			max_fitness = mem_fit
	return alpha

def run_genetic_algorithm(pop_size, encoding_length, mutation_rate, crossover_rate, max_generations, fitness_func, create_random_gene, output, fitness_threshold, verbose=False):

	global POP_SIZE, ENCODING_LENGTH, MUTATION_RATE, CROSSOVER_RATE, NUM_GENERATIONS, fitness

	POP_SIZE = pop_size #the size of each population
	ENCODING_LENGTH = encoding_length #how long each binary encoding is in bits
	MUTATION_RATE = mutation_rate #probability of mutation on each bit
	CROSSOVER_RATE = crossover_rate #probability of a crossover on each mating
	NUM_GENERATIONS = max_generations #the maximum number of generations the algorithm should run
	fitness = fitness_func 
	population = [create_random_gene() for i in range(pop_size)]
	
	gen = 0
	while gen < NUM_GENERATIONS and average_fitness(population) < fitness_threshold:
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("GENERATION: " + str(gen + 1) + ",  AVERAGE FITNESS: " + str(average_fitness(population)))
		alpha = max_member(population)
		print("ALPHA: " + output(alpha) + "\n")
		if verbose:
			for el in population:
				print(output(el))

		newpop = []
		num_mates = pop_size / 2
		if use_alpha:
			newpop = [alpha, alpha]
			num_mates -= 2

		for i in range(num_mates):
			childA, childB = mate_pair(population)
			newpop += [childA, childB]

		population = newpop
		gen += 1

	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("FINAL GENERATION: " + str(gen + 1) + ",  AVERAGE FITNESS: " + str(average_fitness(population)))
	print("ALPHA: " + output(max_member(population)))
	for el in population:
		print(output(el))

	return population

