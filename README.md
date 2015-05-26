# Genetics
Python framework for running a genetic algorithm. Can pass in custom problems that can be represented as a binary string and with a fitness function specified.

##Usage

`genetics_lab.py` contains the main code for the genetic algorithm. You can run this by calling `run_genetic_algorithm` with the following arguments:

`pop_size`: the size of each population

`encoding_length`: how long each binary encoding is in bits

`mutation_rate`: probability of mutation on each bit

`crossover_rate`: probability of a crossover on each mating

`max_generations` the maximum number of generations the algorithm should run for

fitness_func: a **function** that accepts one argument, a binary string, and returns the fitness value of the member associated with that string.
It is often useful to define an encoding_to_member function, which converts a binary representation of an encoding to whatever the fitness function needs to calculate fitness.

`create_random_gene`: a no-argument function that returns a random gene, represented as a binary string

`output`: a one-argument function that takes a gene and returns whatever output is desired for that gene, which can be printed each generation. Defaults to a function that just returns the binary of that gene and its fitness.

`fitness_threshold`: The target fitness value. When the average fitness of the generation's members become greater than this value, the algorithm will terminate.

`verbose`: whether to print output for each member on each generation. Defaults to false.

`use_alpha`: Uses the alpha member from one generation (i.e., the one with highest fitness) as the first pair for the next generation. While this method may or may not be better, it will guarantee that the peak of the generation does not decrease over generations.


Several examples are provided, one involving an optimization of operations, and one involving optimizing a team of Pokemon based on certain characteristics.

More info can be found at http://www.ai-junkie.com/ga/intro/gat1.html
