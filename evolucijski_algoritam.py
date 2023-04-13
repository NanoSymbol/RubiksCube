import random
from Cube import Kocka




def initialize_population(pop_size, min_moves, max_moves):
    population = []
    for _ in range(pop_size):
        moves = ''.join(random.choices("ULFRBD", k=random.randint(min_moves, max_moves)))
        population.append(moves)
    return population


def evaluate_fitness(individual):
    cube = Kocka()
    for move in individual:
        if move == 'U':
            cube.rotacijaU()
        elif move == 'L':
            cube.rotacijaL()
        elif move == 'F':
            cube.rotacijaF()
        elif move == 'R':
            cube.rotacijaR()
        elif move == 'B':
            cube.rotacijaB()
        elif move == 'D':
            cube.rotacijaD()

    # Count the number of correctly placed stickers
    fitness = 0
    faces = [('U', cube.U), ('L', cube.L), ('F', cube.F), ('R', cube.R), ('D', cube.D), ('B', cube.B)]
    for face_name, face in faces:
        for row in face:
            for sticker in row:
                if sticker == face[1][1]:
                    fitness += 1

    return fitness

def select_parents(population, fitnesses):
    # Tournament selection
    parents = []
    k = 3  # Tournament size
    for _ in range(len(population)):
        candidates = random.sample(list(zip(population, fitnesses)), k)
        winner = max(candidates, key=lambda x: x[1])
        parents.append(winner[0])
    return parents

def crossover(parents):
    offspring = []
    for i in range(0, len(parents), 2):
        parent1 = parents[i]
        parent2 = parents[i + 1]
        # One-point crossover
        crossover_point = random.randint(1, len(parent1) - 1)
        offspring.append(parent1[:crossover_point] + parent2[crossover_point:])
        offspring.append(parent2[:crossover_point] + parent1[crossover_point:])
    return offspring

def mutate(offspring, mutation_rate):
    mutated_offspring = []
    for child in offspring:
        mutated_child = ''
        for move in child:
            if random.random() < mutation_rate:
                mutated_child += random.choice("ULFRBD")
            else:
                mutated_child += move
        mutated_offspring.append(mutated_child)
    return mutated_offspring

def evolutionary_algorithm():
    pop_size = 200
    min_moves = 15
    max_moves = 400
    mutation_rate = 0.07
    max_generations = 10000

    population = initialize_population(pop_size, min_moves, max_moves)
    fitnesses = [evaluate_fitness(individual) for individual in population]

    for gen in range(max_generations):
        parents = select_parents(population, fitnesses)
        offspring = crossover(parents)
        offspring = mutate(offspring, mutation_rate)
        population = offspring
        fitnesses = [evaluate_fitness(individual) for individual in population]

        max_fitness = max(fitnesses)
        best_solution = population[fitnesses.index(max_fitness)]
        print(f"Generation {gen + 1}: Best Fitness = {max_fitness}, Solution = {best_solution}")
        if max_fitness == 9:  # Rubik's Cube is solved
            break

evolutionary_algorithm()
