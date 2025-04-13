# 🎲 Battle of the Dice – Which One Wins Most?

## 🧩 Scenario

Imagine you are testing three different dice in a game lab. Each die has a different range of numbers:

- 🎲 **Die A** is a regular 6-sided die with values from **1 to 6**
- 🎲 **Die B** is a smaller die with values from **2 to 5**
- 🎲 **Die C** is an extended die with values from **1 to 8**

You want to understand:  
**Which die is more likely to win if all three are rolled at the same time and the highest number is considered the winner?**

To find out, we simulate this experiment **1,000 times**, recording which die wins in each round.  
If two or more dice tie for the highest number, the result is counted as a **tie**.

---

## 📊 Simulation Purpose

This simulation helps us explore:

- 📐 The effect of **different number ranges** on outcome probabilities
- 🔀 The use of Python’s `random` module for basic simulations
- 📈 Basic data visualization using `matplotlib`

---

## 🧪 What You’ll Learn

- ✅ How to use `random.randint()` to simulate dice rolls
- ✅ How to use `for` loops and dictionary counters to track results
- ✅ How to determine the maximum rolled value and detect ties
- ✅ How to visualize results using:
  - 📊 **Bar charts**
  - 🥧 **Pie charts**
  - 📉 **Horizontal bar charts**

---

## 📦 Requirements

- Python 3.x
- `matplotlib` for plotting results

You can install matplotlib with:
```bash
pip install matplotlib
