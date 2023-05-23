import copy
import random
from Cube import Kocka
from GrafickiPrikaz import PrikazKocke

# Definirajte predefinirani set permutacija poteza kocke
potezi = [
    "F'L'B'R'U'RU'BLFRUR'U",
    "FRBLUL'UB'R'F'L'U'LU'",
    "BLFRUR'UF'L'B'R'U'RU'",
    "B'R'F'L'U'LU'FRBLUL'U",
    "UUBUUB'RRFR'F'UUF'UUFR'",
    "U'U'B'U'U'BL'L'F'LFU'U'FU'U'F'L",
    "UUFUUF'LLBL'B'UUB'UUBL'",
    "U'U'F'U'U'FR'R'B'RBU'U'BU'U'B'R",
    "UURUUR'FFLF'L'UUL'UULF'",
    "U'U'L'U'U'LF'F'R'FRU'U'RU'U'R'F",
    "UULUUL'BBRB'R'UUR'UURB'",
    "U'U'R'U'U'RB'B'L'BLU'U'LU'U'L'B",
    "U'BBDDL'FFDDBBR'U'",
    "UB'B'D'D'RF'F'D'D'B'B'LU",
    "U'FFDDR'BBDDFFL'U'",
    "UF'F'D'D'LB'B'D'D'F'F'RU",
    "UBBDDRFFDDBBLU",
    "U'B'B'D'D'L'F'F'D'D'B'B'R'U'",
    "UFFDDLBBDDFFRU",
    "U'F'F'D'D'R'B'B'D'D'F'F'L'U'",
    "D'R'DRRU'RBBLU'L'BBURR",
    "DLD'L'L'UL'B'B'R'URB'B'U'L'L'",
    "D'L'DLLU'LFFRU'R'FFULL",
    "DRD'R'R'UR'F'F'L'ULF'F'U'R'R'",
    "DLD'LLUL'BBR'URBBU'LL",
    "D'R'DR'R'U'RB'B'LU'L'B'B'UR'R'",
    "DRD'RRUR'FFL'ULFFU'RR",
    "D'L'DL'L'U'LF'F'RU'R'F'F'UL'L'",
    "R'UL'UURU'LR'UL'UURU'LU'",
    "LU'RU'U'L'UR'LU'RU'U'L'UR'U",
    "L'UR'UULU'RL'UR'UULU'RU'",
    "RU'LU'U'R'UL'RU'LU'U'R'UL'U",
    "LU'RUUL'UR'LU'RUUL'UR'U",
    "R'UL'U'U'RU'LR'UL'U'U'RU'LU'",
    "RU'LUUR'UL'RU'LUUR'UL'U",
    "L'UR'U'U'LU'RL'UR'U'U'LU'RU'",
    "F'UBU'FUB'U'",
    "FU'B'UF'U'BU",
    "B'UFU'BUF'U'",
    "BU'F'UB'U'FU",
    "FU'B'UF'U'BU",
    "F'UBU'FUB'U'",
    "BU'F'UB'U'FU",
    "B'UFU'BUF'U'",
    "L'UULRRFFR",
    "RU'U'R'L'L'F'F'L'",
    "LU'U'L'R'R'B'B'R'",
    "R'UURLLBBL",
    "U' L' U R U' L U R'",
    "R'U'RRURUR'U'RURU'RU'R'UU",
    "x",
    "y'"
]

kocka = Kocka()
kocka.scramble()
kocka.printaj_kocku()
# Definirajte klasu za jedinku (rješenje)
class Individual:
    def __init__(self, moves=None):
        if moves is None:
            self.moves = []
        else:
            self.moves = moves

    def add_move(self, move):
        self.moves.append(move)

    def copy(self):
        return Individual(self.moves.copy())

    def __str__(self):
        return "".join(self.moves)


# Definirajte funkciju za evaluaciju fitnessa
def evaluate_fitness(individual):
    kocka_copy = copy.deepcopy(kocka)
    for move in individual.moves:
        kocka_copy.unos_poteza(move)
    # Count the number of correctly placed stickers
    fitness = 0
    faces = [('U', kocka_copy.U), ('L', kocka_copy.L), ('F', kocka_copy.F), ('R', kocka_copy.R), ('D', kocka_copy.D), ('B', kocka_copy.B)]
    for face_name, face in faces:
        for row in face:
            for sticker in row:
                if sticker == face[1][1]:
                    fitness += 1
    return fitness


# Definirajte funkciju za odabir roditelja na temelju fitnessa
def select_parents(population):
    fitness_values = [evaluate_fitness(individual) for individual in population]
    sorted_indices = sorted(range(len(population)), key=lambda k: fitness_values[k], reverse=True)
    best_indices = sorted_indices[:int(len(population) * 0.2)]  # Select top 20% individuals
    parents = [population[index] for index in best_indices]
    return parents


# Definirajte funkciju za križanje roditelja
def crossover_parents(parent1, parent2):
    child1 = parent1
    child2 = parent2
    index = random.randint(0, min(len(child1.moves), len(child2.moves)) - 1)
    child1.moves[index] = parent2.moves[index]
    child2.moves[index] = parent1.moves[index]
    return child1, child2


# Definirajte funkciju za mutaciju jedinke
def mutate_individual(individual):
    new_individual = individual.copy()
    if random.random() < 0.15:
        new_individual.add_move("x")
    if random.random() < 0.15:
        new_individual.add_move("y'")
    if random.random() < 0.5:
        # Add a random move
        new_individual.add_move(random.choice(potezi))
    if random.random() < 0.25:
        # Add a random move
        new_individual.add_move(random.choice(potezi))
    else:
        index = random.randint(0, len(new_individual.moves) - 1)
        # Replace a move with a random different move
        new_individual.moves[index] = random.choice(potezi)
    return new_individual


# Glavna funkcija za evolucijski algoritam
def evolutionary_algorithm(population_size, generations, min_moves, max_moves):
    # Inicijalizacija populacije
    population = initialize_population(population_size, min_moves, max_moves)

    for generation in range(generations):
        new_population = []

        # Evaluacija fitnessa
        fitness_values = [evaluate_fitness(individual) for individual in population]

        # Odabir roditelja
        parents = select_parents(population)

        # Križanje roditelja
        for _ in range(population_size):
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child1, child2 = crossover_parents(parent1, parent2)
            new_population.append(child1)
            new_population.append(child2)

        # Mutacija
        new_population = [mutate_individual(individual) for individual in new_population]

        # Zamjena stare populacije s novom populacijom
        population = new_population
        max_fitness = max(fitness_values)
        best_solution = population[fitness_values.index(max_fitness)]
        print(f"Generation {_ + 1}: Best Fitness = {max_fitness}, Solution = {best_solution}")
#        solucija = str({best_solution})
#        kocka_temp = copy.deepcopy(kocka)
#        prikaz_kocke = PrikazKocke(kocka_temp)
#        kocka_temp.unos_poteza(solucija)
#        prikaz_kocke.prikazi_kocku()
        if max_fitness == 54:  # Rubik's Cube is solved
            break
    # Pronađite najbolju jedinku nakon završetka generacija
    best_individual = max(population, key=evaluate_fitness)
    return best_individual


# Inicijalizacija populacije
def initialize_population(population_size, min_moves, max_moves):
    population = []
    for _ in range(population_size):
        moves = random.choices(potezi, k=random.randint(min_moves, max_moves))
        individual = Individual(moves)
        population.append(individual)
    return population


# Parametri evolucijskog algoritma
population_size = 500
generations = 300
min_moves = 3
max_moves = 12
# Pokretanje evolucijskog algoritma
best_individual = evolutionary_algorithm(population_size, generations, min_moves, max_moves)
# Ispis rezultata
print("Najbolja jedinka:", best_individual)
print("Fitness:", evaluate_fitness(best_individual))
