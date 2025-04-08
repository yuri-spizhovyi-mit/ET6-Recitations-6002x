# 🎓 Recitation #2 – MITx 6.00.2x

## 🧭 Topic: Graph Problem

## 🌌 1. What Is a Graph?

A **graph** is a collection of:

- **Nodes (Vertices)**: Represent entities like cities, users, atoms.
- **Edges (Links)**: Represent relationships between nodes (e.g., roads, friendships).

### Types of Graphs

- **Directed** vs. **Undirected**
- **Weighted** vs. **Unweighted**

Graphs are used in:
- Social networks
- Transportation systems
- Computer and financial networks

---

## 🌲 2. Special Case: Trees

- A **tree** is a directed graph with one unique path between any two nodes.
- Useful for hierarchical data (e.g., file systems, family trees).

---

## 🧰 3. Representing Graphs in Python

### `Node` Class

```python
class Node:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
```

### `Edge` Class

```python
class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return f"{self.src.getName()}->{self.dest.getName()}"
```

### `Digraph` and `Graph`

- `Digraph` uses an adjacency list for directed graphs.
- `Graph` (subclass) adds reverse edges automatically to simulate an undirected graph.

---

## 📘 What is an Adjacency List?

An adjacency list is a way to represent a graph in code (or on paper) that shows which nodes are connected to which.

### 📌 Definition:
For each node in the graph, the adjacency list shows a list of neighboring nodes it connects to directly (i.e., its outgoing edges in a digraph).

---

### 🧭 Where Is the Adjacency List in the Code?

The adjacency list is implemented in the `Digraph` class, specifically in this line:

```python
self.edges = {}
```

This `self.edges` dictionary **is** the adjacency list.

---

### 🔍 Let’s break it down:

When you run:
```python
self.edges[node] = []
```
You create a key for each node in the graph, and associate it with a list of children (i.e., nodes it connects to).

Then when you do:
```python
self.edges[src].append(dest)
```
You’re saying:  
**“There is a directed edge from `src` to `dest`.”**

For example:
```python
g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
```
Results in:
```python
edges[Boston] = [Providence]
```

---

### 🧠 Internally, the adjacency list looks like:

```python
{
  Boston: [Providence, New York],
  Providence: [Boston, New York],
  New York: [Chicago],
  Chicago: [Denver],
  Denver: [Phoenix, New York],
  Phoenix: [],
  Los Angeles: [Boston]
}
```

---

### 🖨️ To print the adjacency list explicitly:

You can modify your script like this:

```python
g = buildCityGraph(Graph)
for node in g.edges:
    print(f"{node.getName()}: {[child.getName() for child in g.edges[node]]}")
```

This will output a clean adjacency list in text format.

---

## 🔁 5. Graph Search Overview

### Breadth-First Search (BFS)
- Explores neighbors level by level.
- Great for finding **shortest path** in unweighted graphs.

### Depth-First Search (DFS)
- Explores as far as possible before backtracking.
- Good for detecting **cycles**, traversing deeply.

🔗 Try both interactively:  
[algorithm-visualizer.org](https://algorithm-visualizer.org/brute-force/depth-first-search)

---

## 🔍 6. DFS vs BFS Comparison

| Feature            | DFS                            | BFS                            |
|--------------------|----------------------------------|--------------------------------|
| Strategy           | Depth first                     | Level by level                 |
| Data Structure     | Stack or recursion              | Queue                          |
| Best Use Case      | Exploring deeply, cycle detection | Finding shortest path          |
| Might Get Stuck?   | Yes (if cycles aren't handled)  | No                             |
| Memory             | Lower                           | Higher                         |



| Aspect                | DFS                              | BFS                              |
|-----------------------|-----------------------------------|----------------------------------|
| May find target faster? | Depends — faster in deep graphs | Better for closer targets        |
| Finds shortest path?  | ❌ No                             | ✅ Yes (if unweighted)           |
| Asymptotic speed?     | O(V + E)                          | O(V + E)                         |


---


