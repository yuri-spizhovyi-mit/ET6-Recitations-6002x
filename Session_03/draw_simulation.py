import random
import matplotlib.pyplot as plt


def trial():
    balls = ["R", "R", "R", "G", "G", "G"]
    result = ""
    for _ in range(3):
        draw = random.choice(balls)
        result += draw
    return result


def simulate_draws(num_trials=1000):
    """
    Simulates drawing 3 balls with replacement from a bucket containing
    3 red ('R') and 3 green ('G') balls, repeated over a number of trials.

    For each trial, tracks the frequency of specific outcomes:

    - "RRR": All three draws are red.
    - "RGR": The exact sequence Red → Green → Red.
    - "2R1G": Any sequence with exactly two red balls and one green.
    - "R>=G": Any sequence where the number of red balls is greater than
             or equal to the number of green balls.

    Parameters:
        num_trials (int): Number of simulation runs to perform (default is 1000).

    Returns:
        dict: A dictionary mapping each tracked outcome to its observed frequency.
              Keys: "RRR", "RGR", "2R1G", "R>=G"
              Values: Integer counts of how many times each condition occurred.
    """

    tracker = {}
    for i in range(num_trials):
        outcome = trial()
        red = outcome.count("R")
        green = outcome.count("G")
        if outcome == "RRR":
            tracker["RRR"] = tracker.get("RRR", 0) + 1
        if outcome == "RGR":
            tracker["RGR"] = tracker.get("RGR", 0) + 1
        if red == 2 and green == 1:
            tracker["2R1G"] = tracker.get("2R1G", 0) + 1
        if red > green:
            tracker["R>=G"] = tracker.get("R>=G", 0) + 1
    return tracker


def prepare_result_for_plot(result, num_trials):
    draws = []
    nums = []
    for key, value in result.items():
        draws.append(key)
        nums.append(value / num_trials * 100)
    sorted_data = sorted(zip(draws, nums), key=lambda x: x[1], reverse=True)
    key_sorted, value_sorted = zip(*sorted_data)
    return key_sorted, value_sorted


def plot_result(key_sorted, value_sorted, trials):
    plt.bar(key_sorted, value_sorted)
    plt.xlabel("Draws Distribution")
    plt.ylabel(f"Amount of time per {trials} trials, %")
    plt.title("Histogram of frequency of specific outcomes")
    for i, value in enumerate(value_sorted):
        plt.text(i, value + 0.5, f"{value}%", ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    plt.grid(True)
    plt.show()


def main():
    trials = 1000
    result = simulate_draws(trials)
    key_sorted, value_sorted = prepare_result_for_plot(result, trials)
    plot_result(key_sorted, value_sorted, trials)


if __name__ == "__main__":
    main()
