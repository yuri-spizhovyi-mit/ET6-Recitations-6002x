# 🎓 Recitation #1 – MITx 6.00.2x

## 🧭 Topic: 0/1 Knapsack Problem

---

## 🎯 Definition

The **0/1 Knapsack Problem** is a classic optimization problem where you aim to select a combination of items that maximizes total value **without exceeding** a weight (or calorie) limit.

You are given:
- A list of items `I`, where each item has a `value` and a `weight`
- A binary vector `V` where `V[i]` = 1 means item `i` is included, 0 means excluded

The problem:

**Maximize**  
\[
\sum_{i=0}^{n-1} V[i] \cdot I[i].value
\]  
**Subject to**  
\[
\sum_{i=0}^{n-1} V[i] \cdot I[i].weight \leq w
\]

---

## 🎒 Visualization

<p align="center">
  <img src="https://raw.githubusercontent.com/MIT-Emerging-Talent/ET6-Recitations-6002x/main/Session01/knapsack2.png" alt="Diagram" width="500"/>
</p>

<p align="center"><em>Example: Maximize value under a 1500 calorie limit</em></p>

---

## 🧩 Problem Classification Diagram
<p align="center">
  <img src="https://raw.githubusercontent.com/MIT-Emerging-Talent/ET6-Recitations-6002x/main/Session01/knapsack.png" alt="Knapsack Problem Diagram" width="600"/>
</p>

<p align="center"><em>Flowchart: Knapsack problem and solution strategies</em></p>


---

## ⚙️ Algorithmic Approaches

### 🟢 Greedy Algorithm

> **"While knapsack not full, put the 'best' available item in."**

But what is "best"?

- Most valuable
- Least expensive
- Highest value per unit (value/weight)

✅ Fast  
❌ May not give the optimal solution

---

### 🔵 Brute Force Algorithm

> Try **all combinations**, then select the best valid one.

Steps:
1. Generate the **power set** of all items
2. Eliminate combinations that **exceed the weight limit**
3. From the rest, **pick the one with the highest total value**

✅ Finds the optimal solution  
❌ Extremely slow — exponential time

---

### ❓ Discussion Prompt

> 🧠 **How can we connect the idea of brute force to a decision tree?**  
> What do branches, nodes, and paths represent in the context of item selection?

(Hint: Each node is a partial solution. Each level represents including or skipping the next item.)

---

### 🟠 Dynamic Programming (DP)

DP improves over brute-force by **avoiding repeated work**.

From the lecture notes:
- DP saves **intermediate results** in a table
- Solves subproblems **bottom-up** or with **memoization**
- For knapsack: store the **best value** for each (item index, remaining capacity) pair

✅ Guarantees optimal solution  
✅ Much faster than brute force  
⛔ Slightly more complex to implement

---

## 📊 Algorithm Comparison Table

| Approach          | Optimal? | Speed       | Strategy                              | Best For                        |
|-------------------|----------|-------------|----------------------------------------|----------------------------------|
| **Greedy**        | ❌        | ⚡ Fast      | Heuristic, local best choice           | Quick approximations             |
| **Brute Force**   | ✅        | 🐢 Very Slow | All combinations                       | Small input sizes, teaching      |
| **Dynamic Programming** | ✅  | 🚀 Efficient | Reuse subproblem results (memoization) | Practical and scalable solutions |

---

## ✅ Summary

- The knapsack problem models **real decision-making under constraint**
- You explored **three strategies**: Greedy (fast), Brute Force (accurate but slow), and DP (efficient and optimal)
- You now understand the **bridge between recursion, decision trees, and optimization**

---
