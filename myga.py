import random
import numpy as np

prob_crossover = 0.9
prob_mutation = 0.025
iterations_limit = 1500
population_size = 100
individual_size = 10

def random_individual() :
    return [random.randint(0,1) for i in range(individual_size)]

def initial_population():
    population = np.zeros((population_size,individual_size))
    for i in range(population_size):
        population[i,:] = random_individual()
    return population

def fitness(c):
    fitness_population = []
    for i in range(population_size):
        fitness_population.append(sum(c[i,:]))
    return fitness_population

def selection(population,fitness_population,population_size):
    fitness_sum = sum(fitness_population)
    fitness_pro = []
    for i in range(len(fitness_population)):
        fitness_pro.append(fitness_population[i]/fitness_sum)
    fitness_pro = np.cumsum(fitness_pro)
    roulette = []
    for i in range(population_size):
        roulette.append(random.random())
    roulette.sort()
    fitin = 0
    rouin = 0
    population_new = population
    while rouin < population_size:
        if roulette[rouin] < fitness_pro[fitin]:
            population_new[rouin] = population[fitin]
            rouin += 1
        else:
            fitin += 1
    return population_new

def crossover(population, prob_crossover,individual_size,population_size):
    parents = range(population_size)
    random.shuffle(parents)
    father = parents[0:(population_size/2)]
    mother = parents[(population_size/2):population_size]
    for i in range(population_size/2):
        if(random.random() < prob_crossover):
            cpoint = random.randint(0,individual_size)
            temp1 = []
            temp2 = []
            temp1.extend(population[father[i]][0 : cpoint])
            temp1.extend(population[mother[i]][cpoint :individual_size])
            temp2.extend(population[mother[i]][0 : cpoint])
            temp2.extend(population[father[i]][cpoint : individual_size])
            population[father[i]] = temp1
            population[mother[i]] = temp2
    return population

def mutation(population,individual_size,prob_mutation):
    for i in range(len(population)):
        if(random.random() < prob_mutation):
            mpoint = random.randint(0,individual_size-1)
            population[i][mpoint] = 1 - population[i][mpoint]
    return population

#def survival(fitness_initial,fitness_new,init_population,population,population_size):

#    return population
def check_stop(fitness,population_size):
    return 1 if (sum(fitness)/population_size) == individual_size else 0

def run():
    population = initial_population()
    for i in range(iterations_limit):
        fitness_initial = fitness(population)
        best = max(fitness_initial)
        worst = min(fitness_initial)
        ave = sum(fitness_initial)/population_size
        print i, best, ave, worst
        if check_stop(fitness_initial,population_size) :break 
        population = selection(population,fitness_initial,population_size)
        population = crossover(population,prob_crossover,individual_size,population_size)
        population = mutation(population,individual_size,prob_mutation)
    return population
run()
#print run()
#population = initial_population()
#fitness = fitness(population)
