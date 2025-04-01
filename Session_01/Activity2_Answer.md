# 💡 Sample Answers – Activity 2: Exploring Brute Force Algorithm via Recursion

---

### 1. Describe the operation of the recursive search tree approach as implemented in the `maxVal()` function. How does it explore possible combinations of items to find a solution?

The `maxVal()` function explores every possible subset of items using **recursion**, which implicitly builds a **binary decision tree**.

At each step:
- It chooses whether to **include** the current item (left branch) or **exclude** it (right branch).
- It then **recursively solves the remaining problem** with the reduced list and updated capacity.
- This continues until there are no items left or no capacity remaining (base case).

Each **path through the tree** represents a **different combination of items**, and the function **compares the total values** of these combinations to find the best one.

---

### 2. How do the results obtained from the greedy algorithm and the brute force (recursive search tree) approach differ when solving the knapsack problem with the same items and constraints?

- The **greedy algorithm** selects items based on a single heuristic (e.g., highest value, lowest cost, best value-per-calorie), one step at a time.  
  → It is **fast**, but it doesn’t always return the **optimal** solution.

- The **brute-force recursive approach** (via `maxVal`) examines **all valid combinations** and always returns the **optimal** set of items.  
  → However, it is **much slower**, especially as the number of items increases.

> ✅ Summary:  
> Greedy = fast but sometimes suboptimal  
> Brute force = slow but guaranteed optimal

---

### 3. Compare the complexity of the two approaches (greedy and recursive). What trade-offs do they involve?

| Algorithm       | Time Complexity         | Trade-offs |
|----------------|--------------------------|------------|
| Greedy         | `O(n log n)` (due to sorting)| Fast, simple, but not always optimal |
| Brute Force    | `O(2^n)`                 | Guarantees optimal solution, but exponential time |

- **Greedy** is useful when you need a quick approximation.  
- **Brute force** is better when **accuracy matters** and the problem size is small.

---

### 4. Can you identify repeated subproblems? How could memoization or dynamic programming improve this?

Yes — the `maxVal()` function solves the same subproblems **multiple times**, especially when:
- The same list of remaining items
- The same remaining capacity

This results in **redundant computations**.

> **Memoization** or **dynamic programming** can be used to **store solutions** to these subproblems, so they aren’t recalculated.

This transforms the time complexity from `O(2^n)` to `O(n * W)`, where:
- `n` = number of items  
- `W` = total capacity

This is the foundation of the **Dynamic Programming solution** to the knapsack problem.
