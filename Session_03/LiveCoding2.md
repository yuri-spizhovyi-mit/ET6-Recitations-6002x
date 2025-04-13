# 🪣 Probability Simulation – Drawing Balls with Replacement

## 🎯 Scenario: Understanding Probabilities Through Repeated Random Draws

You are given a bucket containing an equal number of red and green balls:

- 🎈 3 **Red (R)** balls
- 🎈 3 **Green (G)** balls

You draw **3 balls in succession**, **with replacement** — meaning the ball is placed back into the bucket after each draw, so probabilities remain constant.

The goal of this simulation is to estimate the **empirical probability** of specific outcomes by repeating the experiment **1,000 times**.

---

## 🧪 What Are We Tracking?

In each set of 3 draws, the code keeps track of the number of times we observe:

- 🎯 `RRR`: All three balls drawn are red
- 🎯 `RGR`: The exact sequence Red → Green → Red
- 🎯 `2R1G`: Any combination that includes exactly two red and one green ball
- 🎯 `R ≥ G`: Any draw in which the number of red balls is **greater than or equal to** the number of green balls

---

## 🛠 How It Works

- A list `['R', 'G', 'R', 'G', 'R', 'G']` simulates the bucket.
- On each trial, the simulation:
  1. Randomly selects 3 balls with replacement
  2. Checks if the result matches any of the tracked conditions
  3. Updates the corresponding counter
- After 1,000 trials, the results are plotted using:
  - 📊 A **bar chart** to show frequency of each outcome
  - 🥧 A **pie chart** to visualize outcome proportions (optional)

---

## 📚 What You’ll Learn

- How to use `random.choice()` for simulations with replacement
- How to count specific outcome patterns from multiple trials
- How to track multiple logical conditions in one experiment
- How to visualize outcomes using:
  - Bar charts (`matplotlib.pyplot.bar`)
  - Pie charts (`matplotlib.pyplot.pie`)

---

## 🚀 Try It Yourself

To run the simulation and see the plots:

```bash
python draw_simulation.py
