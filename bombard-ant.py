import random
import math

POPULATION_SIZE = 50
MAX_GENERATIONS = 100
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.02
BOMB_RADIUS = 10.0

class Point:
    def __init__(self, x, y, amount_of_ants):
        self.x = x
        self.y = y
        self.amount_of_ants = amount_of_ants

class Chromosome:
    def __init__(self, bombs):
        self.bombs = bombs
        self.fitness = self.calculateFitness()

    def calculateDistance(self, p1, p2):
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        return math.sqrt(dx * dx + dy * dy)

    def calculateKills(self, ants, distance):
        dmax = self.calculateDistance(nests[0], nests[1])
        for i in range(num_nests):
            for j in range(i + 1, num_nests):
                d = self.calculateDistance(nests[i], nests[j])
                if d > dmax:
                    dmax = d
        return ants * dmax / 20.0 * distance + 0.00001

    def calculateFitness(self):
        total_kills = 0.0
        remaining_ants = [nest.amount_of_ants for nest in nests]
        for bomb in self.bombs:
            for i, nest in enumerate(nests):
                distance = self.calculateDistance(nest, bomb)
                if distance <= BOMB_RADIUS:
                    kills = self.calculateKills(nest.amount_of_ants, distance)
                    if kills >= remaining_ants[i]:
                        total_kills += remaining_ants[i]
                        remaining_ants[i] = 0
                    else:
                        total_kills += kills
                        remaining_ants[i] -= kills
        return total_kills

def initializePopulation():
    population = []
    for i in range(POPULATION_SIZE):
        bombs = [Point(random.randint(0, 100), random.randint(0, 100), 0) for _ in range(3)]
        population.append(Chromosome(bombs))
    return population

def mutate(chromosome):
    for i in range(3):
        if random.random() < MUTATION_RATE:
            chromosome.bombs[i].x = random.randint(0, 100)
            chromosome.bombs[i].y = random.randint(0, 100)
    chromosome.fitness = chromosome.calculateFitness()

def crossover(parent1, parent2):
    child1_bombs = []
    child2_bombs = []
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(0, 2)
        for i in range(3):
            if i <= crossover_point:
                child1_bombs.append(parent1.bombs[i])
                child2_bombs.append(parent2.bombs[i])
            else:
                child1_bombs.append(parent2.bombs[i])
                child2_bombs.append(parent1.bombs[i])
    else:
        child1_bombs = [Point(bomb.x, bomb.y, bomb.amount_of_ants) for bomb in parent1.bombs]
        child2_bombs = [Point(bomb.x, bomb.y, bomb.amount_of_ants) for bomb in parent2.bombs]
    child1 = Chromosome(child1_bombs)
    child2 = Chromosome(child2_bombs)
    mutate(child1)
    mutate(child2)
    return child1, child2

def evolve(population):
    total_fitness = sum(chromosome.fitness for chromosome in population)
    new_population = []
    for i in range(0, POPULATION_SIZE, 2):
        parent1 = rouletteWheelSelection(population, total_fitness)
        parent2 = rouletteWheelSelection(population, total_fitness)
        child1, child2 = crossover(population[parent1], population[parent2])
        new_population.append(child1)
        new_population.append(child2)
    for i in range(POPULATION_SIZE):
        population[i] = new_population[i]

def rouletteWheelSelection(population, total_fitness):
    slice = random.random() * total_fitness
    fitness_so_far = 0.0
    for i in range(POPULATION_SIZE):
        fitness_so_far += population[i].fitness
        if fitness_so_far >= slice:
            return i
    return POPULATION_SIZE - 1

def findBestSolution(population):
    best_solution = population[0]
    for i in range(1, POPULATION_SIZE):
        if population[i].fitness > best_solution.fitness:
            best_solution = population[i]
    return best_solution

nests = [
    Point(25, 65, 100),
    Point(23, 8, 200),
    Point(7, 13, 327),
    Point(95, 53, 440),
    Point(3, 3, 450),
    Point(54, 56, 639),
    Point(67, 78, 650),
    Point(32, 4, 678),
    Point(24, 76, 750),
    Point(66, 89, 801),
    Point(84, 4, 945),
    Point(34, 23, 967)
]
num_nests = len(nests)

population = initializePopulation()

best_fitness_list = []  # List to store the best fitness value from each generation
max_kills_list = []  # List to store the maximum kills from each generation

for generation in range(MAX_GENERATIONS):
    best_solution = findBestSolution(population)
    best_fitness_list.append(best_solution.fitness)
    max_kills_list.append(max([chromosome.fitness for chromosome in population]))  # Append maximum kills from the current generation
    print(f"Generation: {generation}, Best fitness solution: {best_solution.fitness:.3f}, Max kills: {max(max_kills_list):.3f}")
    evolve(population)

best_solution = findBestSolution(population)
print("\nBest solution:")
for i, bomb in enumerate(best_solution.bombs):
    print(f"Bomb {i+1}: ({bomb.x:.3f}, {bomb.y:.3f})")

print("\nAnts extermination successful.\n")
