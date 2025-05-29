import random

TABLE_SIZE = 8
POP_SIZE = 100
MUTATION_RATE = 0.03
MAX_GENERATIONS = 1000

def fitness(individual):
    conflicts = 0

    for i in range(TABLE_SIZE):
        for j in range(i+1, TABLE_SIZE):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                conflicts += 1

    return conflicts

def create_individual():
    individual = list(range(TABLE_SIZE))
    random.shuffle(individual)
    return individual

def crossover(parent1, parent2):
    point = random.randint(0, TABLE_SIZE - 1)
    child = parent1[:point] + [gene for gene in parent2 if gene not in parent1[:point]]
    return child

def mutate(individual):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(TABLE_SIZE), 2)
        individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm():
    population = [create_individual() for _ in range(POP_SIZE)]

    for generation in range(MAX_GENERATIONS):
        population.sort(key=fitness)
        if fitness(population[0]) == 0:
            return population[0], generation

        new_population = population[:10]

        while len(new_population) < POP_SIZE:
            parent1, parent2 = random.sample(population[:50], 2)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        population = new_population

    return None, MAX_GENERATIONS

