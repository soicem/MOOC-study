import random
import math
from deap import base
from deap import creator
from deap import tools
import matplotlib.pyplot as plt

random.seed()
def randouble(minimum, maximum):
    return random.randrange(minimum, maximum)+random.random()

def decoding(individual):
    sum = 0
    print individual
    for i in range(0, len(individual), 1):
        individual[i] * (2 ** i)
        sum += individual[i]*(2**i)
    return sum/float(2**12)*(2-(-1))+(-1)

def evalFunction(individual):
    x = decoding(individual)
    return x*math.sin(10*math.pi*x)+2.0,

#GA parameter
IND_SIZE = 12
POP_SIZE = 20
NGEN = 1000

#crossover parameter
CXPB = 0.3
CXETA = 1
CXLOW = -1.0
CXUP = 2.0

#mutation parameter
MUTPB = 0.01
MUTETA = 0
MUTLOW = -1
MUTUP = 2
INDPB = 1


creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
# Attribute generator
toolbox.register("attribute", random.randint, 0, 1)
# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalFunction)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb = INDPB)
toolbox.register("select", tools.selRoulette)

pop = toolbox.population(n=POP_SIZE)

# Evaluate the entire population
fitnesses = list(map(toolbox.evaluate, pop))
for ind, fit in zip(pop, fitnesses):
    ind.fitness.values = fit

avr = []
mx = []
mn = []
# Begin the evolution
for g in range(NGEN):
    print("-- Generation %i --" % g)
    # Select the next generation individuals
    new_pop = []
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
                toolbox.mutate(mutant)
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        new_pop = new_pop + offspring
        print len(new_pop)

    pop[:] = new_pop
    pop = list(map(toolbox.clone, pop))
    # Gather all the fitnesses in one list and print the stats
    fits = [ind.fitness.values[0] for ind in pop]

    length = len(pop)
    mean = sum(fits) / length
    sum2 = sum(x * x for x in fits)
    std = abs(sum2 / length - mean ** 2) ** 0.5
    avr.append(mean)
    mx.append(max(fits))
    mn.append(min(fits))
    print("  Min %s" % min(fits))
    print("  Max %s" % max(fits))
    print("  Avg %s" % mean)
    print("  Std %s" % std)



