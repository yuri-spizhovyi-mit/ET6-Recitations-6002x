# 🧩 Activity #2: Exploring Brute Force Algorithm via Recursion

## 🔍 Objective

Explore and describe how the recursive function `maxVal()` simulates a **decision tree** to solve the 0/1 Knapsack Problem.

---

## 🧠 Background: What Does `maxVal()` Do?

- At each step, the function decides **whether to include or exclude** the current item.
- This creates **two recursive branches**:
  - One that **includes the item** (reducing available weight)
  - One that **excludes the item** (leaving weight unchanged)
- These recursive calls form a **binary decision tree**.

---

## 🌳 How It Builds the Tree

| Code Step                            | Decision Tree Meaning             |
|-------------------------------------|-----------------------------------|
| `maxVal([A, B, C], avail)`          | Root node                         |
| Take A → `maxVal([B, C], avail-A)`  | Left child (include A)            |
| Skip A → `maxVal([B, C], avail)`    | Right child (exclude A)           |
| Repeats until no items or no weight | Leaf node (base case reached)     |

Each path = one **possible combination** of items.  
The function compares **left vs right** to return the **maximum value solution**.

---

## 🔄 Base Case and Termination

- The recursion **stops** when:
  - No items are left (`toConsider == []`)
  - No capacity remains (`avail == 0`)
- It then **backs up** and chooses the better result between:
  - Including the current item
  - Excluding the current item

---

## 💬 Group Discussion Questions (Activity 2)

1. Describe the operation of the recursive search tree approach as implemented in the `maxVal` function. How does it explore possible combinations of items to find a solution?
2. How do the results obtained from the greedy algorithm and the brute force (recursive search tree) approach differ when solving the knapsack problem with the same items and constraints?
3. Compare the complexity of the two approaches (greedy and recursive). What trade-offs do they involve?
4. Can you identify repeated subproblems? How could memoization or dynamic programming improve this?

---

## 🧩 Python Code for Reference

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
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                          calories[i]))
    return menu

def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key = keyFunction,
                       reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
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
    print('Use greedy by value to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.getValue)
    print('\nUse greedy by cost to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.density)

def maxVal(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)

testGreedys(foods, 750)
print('')
testMaxVal(foods, 750)
