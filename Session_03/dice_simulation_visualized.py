import random

# import pylab


import matplotlib.pyplot as plt


# -----------------------------------------
# Scenario:
# You have three dice:
# - Die A: values from 1 to 6
# - Die B: values from 2 to 5
# - Die C: values from 1 to 8
# In each round, all three dice are rolled.
# The die with the highest number wins.
# If there's a tie, it's counted as a "Tie".
# We simulate 1000 rounds and visualize the results.
# -----------------------------------------
def roll_die(min_val, max_val):
    return random.randint(min_val, max_val)


def simulate_dice_competition(rounds=1000):
    abc_tie = "ABC"
    ab_tie = "AB"
    ac_tie = "AC"
    bc_tie = "BC"
    a_winner = "A"
    b_winner = "B"
    c_winner = "C"
    data = {}
    for _ in range(rounds):
        a = roll_die(1, 6)
        b = roll_die(2, 5)
        c = roll_die(1, 8)
        if a == b == c:
            data[abc_tie] = data.get(abc_tie, 0) + 1
        elif a == b and a > c:
            data[ab_tie] = data.get(ab_tie, 0) + 1
        elif a == c and a > b:
            data[ac_tie] = data.get(ac_tie, 0) + 1
        elif b == c and b > a:
            data[bc_tie] = data.get(bc_tie, 0) + 1
        elif a > b and a > c:
            data[a_winner] = data.get(a_winner, 0) + 1
        elif b > a and b > c:
            data[b_winner] = data.get(b_winner, 0) + 1
        else:
            data[c_winner] = data.get(c_winner, 0) + 1

    return data


def prepare_result_for_plot(result, rounds):
    winner = []
    probability = []
    for dice, res in result.items():
        winner.append(dice)
        probability.append(round(res / rounds * 100, 2))
    sorted_data = sorted(zip(winner, probability), key=lambda x: x[1], reverse=True)
    winner_sorted, probability_sorted = zip(*sorted_data)
    return winner_sorted, probability_sorted


def plot_result(winner_sorted, probability_sorted):
    plt.bar(winner_sorted, probability_sorted)
    plt.xlabel("Dice Win Distribution")
    plt.ylabel("Probability, %")
    plt.title("Histogram of probability of rolling 3 dice")
    for i, value in enumerate(probability_sorted):
        plt.text(i, value + 0.5, f"{value}%", ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def main():
    rounds = 1000
    result = simulate_dice_competition(rounds)
    winner_sorted, probability_sorted = prepare_result_for_plot(result, rounds)
    plot_result(winner_sorted, probability_sorted)


if __name__ == "__main__":
    main()
