import random
import math
from deap import base
from deap import creator
from deap import tools
import matplotlib.pyplot as plt

random.seed()
def randouble(minimum, maximum):
    return random.randrange(minimum, maximum)+random.random()

def evalFunction(individual):
    x = individual[0]
    y = individual[1]
    return (math.pow(x, 2)+math.pow(y, 2))/4000.0-math.cos(x)*math.cos(y/math.sqrt(2))+1,

def transFitness(population):
    fits = [ind.fitness.values[0] for ind in population]
    mx = 2.5
    for i in range(0,len(fits),1) :
        fits[i] = -fits[i]+mx+1
    for ind, fit in zip(population, fits):
        ind.fitness.values = [fit,]
    return population

def delta(genindex, y, rand, maxgen, decspeed):
    return y*(1-rand**((1-genindex/float(maxgen))**decspeed))

def mutNonuniform(individual, genindex, low, up, indpb, maxgen, decspeed):
    for i in range(0, len(individual), 1):
        if random.random() >= indpb:
            rand = random.random()
            if rand >= 0.5 :
                individual[i] += delta(genindex, up-individual[i], rand, maxgen, decspeed)
            else :
                individual[i] -= delta(genindex, individual[i]-low, rand, maxgen, decspeed)
    return individual,

#GA parameter
IND_SIZE = 2
POP_SIZE = 20
NGEN = 500

#crossover parameter
CXPB = 1
CXETA = 1
CXLOW = -30.0
CXUP = 30.0
#mutation parameter
MUTPB = 0.01
MUTETA = 100
MUTLOW = -30
MUTUP = 30
INDPB = 1


creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
# Attribute generator
toolbox.register("attribute", randouble, -30.0, 30.0)
# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalFunction)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", mutNonuniform, low = MUTLOW, up = MUTUP, indpb = INDPB, maxgen = NGEN, decspeed = 1)
toolbox.register("select", tools.selRoulette)

pop = toolbox.population(n=POP_SIZE)
# Evaluate the entire population
fitnesses = list(map(toolbox.evaluate, pop))
for ind, fit in zip(pop, fitnesses):
    ind.fitness.values = fit


avr = []
mn = []
# Begin the evolution
for g in range(NGEN):
    print("-- Generation %i --" % g)
    # Select the next generation individuals
    new_pop = []
    pop = transFitness(pop)
    while len(new_pop) < len(pop):
        offspring = toolbox.select(pop, 2)
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))
        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant, g)
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        new_pop = new_pop + offspring

    pop[:] = new_pop
    pop = list(map(toolbox.clone, pop))
    # Gather all the fitnesses in one list and print the stats
    fits = [ind.fitness.values[0] for ind in pop]

    length = len(pop)
    mean = sum(fits) / length
    sum2 = sum(x * x for x in fits)
    std = abs(sum2 / length - mean ** 2) ** 0.5
    avr.append(mean)
    mn.append(min(fits))
    print("  Min %s" % min(fits))
    print("  Max %s" % max(fits))
    print("  Avg %s" % mean)
    print("  Std %s" % std)

