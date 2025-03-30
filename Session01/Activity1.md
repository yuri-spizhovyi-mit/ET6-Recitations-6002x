# 🧩 Activity 1: Exploring the Greedy Algorithm

## 🧠 Objective

Understand how the greedy algorithm works in the provided Python code and how different strategies affect the outcome of the 0/1 Knapsack problem.

---

## 🔍 Discussion Questions

1. **What is the role of the `greedy()` function in the code, and how does it operate?**  
   - Consider how it sorts the items and what logic determines inclusion in the knapsack.

2. **What is the purpose of the `testGreedys()` function in the code?**  
   - What are the benefits of calling `testGreedy()` multiple times with different key functions from a learning or testing perspective?

3. **Explain the significance of the `keyFunction` parameter in the `greedy()` function.**  
   - How does it influence item selection? What effect do different key functions have on the final result?

---
## 🧪 Provided Code

The core logic revolves around the following functions:

- `greedy(items, maxCost, keyFunction)`
- `testGreedy(items, constraint, keyFunction)`
- `testGreedys(foods, maxUnits)`

The program tries different greedy strategies using item value, cost (calories), and density (value/calorie).

```python
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue() / self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)

def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\\nUse greedy by cost to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, lambda x: 1 / Food.getCost(x))
    print('\\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)
```

---

## 🧩 Stretch Exercise (Optional)

Try modifying the item list or calorie constraint.  
Can you create an example where the greedy algorithm gives a suboptimal solution?  
What does that reveal about its limitations?

---

## 📌 Learning Goals

- Understand how greedy algorithms **approximate** optimal solutions
- Observe how **choice of heuristic** (key function) affects outcome
- Reflect on when greedy methods are useful vs when they fall short
