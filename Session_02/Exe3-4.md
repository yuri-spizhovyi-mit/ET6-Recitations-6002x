# Understanding Maximum Number of Adjacent Swaps (Question 4)

## ❓ What does the question ask?

Given two different arrangements (permutations) of `n` students in a line, what is the **maximum number of adjacent swaps** it could take to turn one arrangement into the other?

---

## ⛓️ What is an adjacent swap?

An **adjacent swap** is when you only switch the positions of **two students standing next to each other**. You can't jump or swap people who are far apart.

---

## 🧠 Example with 4 Students

Let’s say the students are originally lined up like this:

```
A   B   C   D
```

And we want to reverse the line to:

```
D   C   B   A
```

We can only swap **neighboring** students. Here are the steps:

1. Swap C and D → `A B D C`  
2. Swap B and D → `A D B C`  
3. Swap A and D → `D A B C`  
4. Swap B and C → `D A C B`  
5. Swap A and C → `D C A B`  
6. Swap A and B → `D C B A`

✅ Total swaps = **6**

---

## 🧮 Why is the Maximum Swaps Formula `n(n - 1)/2`?

To reverse `n` elements using adjacent swaps:
- The last person moves `n - 1` steps to the front  
- The second-last person moves `n - 2` steps  
- ...
- The second person moves 1 step

So total swaps:
```
(n - 1) + (n - 2) + ... + 1 = n(n - 1)/2
```

---

## ✅ Final Answer

> The **maximum number of adjacent swaps** to go from one permutation to another is:
```
n(n - 1)/2
```

---

## 🎞️ Animation

You can use the following animation to visualize how `"ABCD"` becomes `"DCBA"` using 6 adjacent swaps:

👉 ![Animation of adjacent swaps](adjacent_swaps.gif)


---

## 🔁 Let’s Count the Swaps Needed (Step-by-Step)

### Step-by-step moves:

- **Move D** from position 4 → position 1:  
  → D passes over C (1), B (2), A (3) → **3 swaps**

- **Move C** from position 3 → position 2:  
  → C passes over B (1), A (2) → **2 swaps**

- **Move B** from position 2 → position 3:  
  → B passes over A (1) → **1 swap**

- **A** is already in the final position

✅ **Total swaps**: `3 + 2 + 1 = 6`
