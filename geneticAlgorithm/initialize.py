import random
def inizialize_gene(available_moves: [int], gene_length: int) -> [int]:
    gene = []
    for _ in range(gene_length):
        move = random.randint(0, len(available_moves) - 1)
        gene.append(available_moves[move])
    return gene

def initialize_population(n_genes: int, available_moves: [int], gene_length: int) -> [[int]]:
    population = []
    for _ in range(n_genes):
        gene = inizialize_gene(available_moves, gene_length)
        population.append(gene)
    return population