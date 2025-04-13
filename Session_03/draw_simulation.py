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
