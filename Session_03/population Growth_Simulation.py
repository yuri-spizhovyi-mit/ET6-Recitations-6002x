import matplotlib.pyplot as plt
import random


def simulate_population_growth(
    initial_population, num_generations, reproduction_probability
):
    """
    Simulates population growth over multiple generations with a stochastic process.

    Parameters:
    - initial_population (int): The initial size of the population.
    - num_generations (int): The number of generations to simulate.
    - reproduction_probability (float): The probability of an individual reproducing in each generation.

    Returns:
    - list: List containing the population size for each generation.
    """
    generations_list = [initial_population]
    current_population = initial_population
    while num_generations > 0:
        new_population = 0
        for i in range(current_population):
            if random.random() < reproduction_probability:
                new_population += 1
        current_population += new_population
        generations_list.append(current_population)
        num_generations -= 1
    return generations_list


def plot_result(result, num_generations):
    plt.bar(range(len(result)), result)
    plt.xlabel("Generations")
    plt.ylabel("Number of population")
    plt.title(f"Histogram of population growth over {num_generations} generations")
    for i, value in enumerate(result):
        plt.text(i, value + 0.5, f"{value}", ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    plt.show()


def main():
    initial_population = 5
    num_generations = 10
    reproduction_probability = 0.8
    result = simulate_population_growth(
        initial_population, num_generations, reproduction_probability
    )
    plot_result(result, num_generations)


if __name__ == "__main__":
    main()
