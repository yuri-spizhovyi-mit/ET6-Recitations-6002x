# 💡 Sample Answers – Activity 1: Greedy Algorithm

---

### 1. What is the role of the `greedy()` function in the code, and how does it operate?

The `greedy()` function (used via `testGreedy()` and `testGreedys()`) implements a greedy strategy to select items based on a **key function**.

- It sorts the items in descending order of the key function.
- Iteratively adds items to the result until the total cost exceeds the constraint.
- Returns the **selected items and their total value**.

---

### 2. What is the purpose of the `testGreedys()` function?

The `testGreedys()` function serves as a **testing framework** to evaluate how the `greedy()` function behaves with different heuristics.

- It calls `testGreedy()` with multiple key functions.
- Helps compare strategies:
  - `Food.getValue` – highest value
  - `1/Food.getCost` – lowest cost
  - `Food.density` – best value per calorie

> **2.b.** This allows students to observe how item selection varies with different key functions and identify which is best for their specific problem context.

---

### 3. What is the role of the `keyFunction` parameter?

The `keyFunction` defines how items are prioritized during selection.

- `Food.getValue`: Prioritizes high-value items  
- `1/Food.getCost`: Prioritizes low-cost items  
- `Food.density`: Prioritizes best value-per-cost  

It allows customization of the greedy strategy based on the optimization objective. Understanding it is crucial for adapting the algorithm effectively.
