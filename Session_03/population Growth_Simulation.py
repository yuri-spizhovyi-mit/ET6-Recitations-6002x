import matplotlib.pyplot as plt
import random

def simulate_population_growth(initial_population, num_generations, reproduction_probability):
    """
    Simulates population growth over multiple generations with a stochastic process.

    Parameters:
    - initial_population (int): The initial size of the population.
    - num_generations (int): The number of generations to simulate.
    - reproduction_probability (float): The probability of an individual reproducing in each generation.

    Returns:
    - list: List containing the population size for each generation.
    """
