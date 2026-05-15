# Learning Python NumPy — Documentation

## Overview

This is a **7-day structured learning repository** designed to teach NumPy fundamentals through progressive, hands-on Python scripts. Each day covers a specific topic with tutorial files and practice tasks/questions. The repository culminates in a mini project that applies all learned concepts to a real-world dataset analysis scenario.

**Repository:** [github.com/Marwan-Alii/Learning-Python-Numpy](https://github.com/Marwan-Alii/Learning-Python-Numpy)

---

## Repository Structure

```
Learning-Python-Numpy/
├── Day1 - NumPy Arrays/
│   ├── 1. Lists vs Arrays.py
│   ├── 2. n-dimensional array.py
│   ├── 3. slicing.py
│   ├── Task1.py – Task9.py
│   └── Task10.txt
├── Day2 - Vectorized Operations and Broadcasting/
│   ├── Element_Wise_Operations.py
│   ├── Operations_With_Scalars.py
│   ├── Vectorization.txt
│   ├── question1.py – question9.py
│   └── question10.txt
├── Day3 - Reshaping and Dimensions/
│   ├── Array Reshaping.py
│   ├── Dimensions and Shapes.py
│   ├── matrix.py
│   ├── question1.py – question9.py
│   └── question10.txt
├── Day4 - Aggregation, Statistics & Axis Operations/
│   ├── 1. aggregation.py
│   ├── 2. Advanced_Aggregation.py
│   ├── file.py
│   ├── question1.py – question8.py
│   └── quesiton10.txt
├── Day5 - Random Module and Simulations/
│   ├── RandomIntegers.py
│   ├── Simulation.py
│   ├── question1.py – question9.py
│   └── question10.py
├── Day6 - Linear Algebra Basics/
│   ├── Linear_Algebra_Basics.py
│   ├── Matrix_Multiplication.py
│   ├── question1.py – question9.py
│   └── question10.py
└── Day7 - Mini Project/
    ├── dataset.py
    └── project.py
```

---

## Day-by-Day Curriculum

### Day 1 — NumPy Arrays
**Goal:** Understand the basics of NumPy arrays and how they differ from Python lists.

**Topics Covered:**
- Creating arrays with `np.array()`
- Differences between list concatenation (`+`) vs. element-wise array addition
- N-dimensional arrays (1D, 2D, 3D)
- Array properties: `.shape`, `.ndim`, `.dtype`, `.size`
- Element access using positive and negative indexing
- Array slicing syntax: `[start:end:step]`
- Multi-dimensional slicing and submatrix extraction

**Key Files:**
- `1. Lists vs Arrays.py` — Demonstrates list concatenation vs. array addition
- `2. n-dimensional array.py` — Creating and inspecting 1D/2D/3D arrays
- `3. slicing.py` — Slicing patterns including reverse arrays and submatrices

---

### Day 2 — Vectorized Operations and Broadcasting
**Goal:** Learn to perform operations on entire arrays without explicit loops.

**Topics Covered:**
- Element-wise arithmetic (`+`, `-`, `*`, `/`, `**`)
- Scalar operations and broadcasting rules
- Comparison operations and boolean masking
- Universal functions: `np.sqrt()`, `np.exp()`, `np.sin()`, `np.abs()`
- Broadcasting with 2D arrays

**Key Files:**
- `Element_Wise_Operations.py` — Basic arithmetic between two arrays
- `Operations_With_Scalars.py` — Scalar ops, comparison masks, broadcasting, and ufuncs

---

### Day 3 — Reshaping and Dimensions
**Goal:** Manipulate array shapes and understand dimensionality.

**Topics Covered:**
- `reshape()` and the `-1` auto-calculation feature
- Flattening multi-dimensional arrays with `.flatten()`
- Transposing arrays with `.T`
- Understanding 0D (scalar), 1D, 2D, and 3D shapes
- Matrix creation patterns

**Key Files:**
- `Array Reshaping.py` — `reshape()`, `flatten()`, `transpose`
- `Dimensions and Shapes.py` — Exploring `.ndim` and `.shape` across dimensions

---

### Day 4 — Aggregation, Statistics & Axis Operations
**Goal:** Summarize and analyze array data statistically.

**Topics Covered:**
- Aggregation: `np.sum()`, `np.mean()`, `np.median()`, `np.min()`, `np.max()`
- Index-based extrema: `np.argmin()`, `np.argmax()`
- Advanced stats: `np.std()`, `np.var()`, `np.cumsum()`, `np.cumprod()`, `np.prod()`
- Axis-based operations (`axis=0` for vertical, `axis=1` for horizontal)
- Keeping dimensions with `keepdims=True`

**Key Files:**
- `1. aggregation.py` — Core aggregation functions
- `2. Advanced_Aggregation.py` — Standard deviation, variance, cumulative ops, axis operations

---

### Day 5 — Random Module and Simulations
**Goal:** Generate random data and run simple simulations.

**Topics Covered:**
- `np.random.randint()` — random integers in ranges
- `np.random.rand()` — random floats in [0, 1)
- `np.random.choice()` — random selection with optional probabilities
- `np.random.shuffle()` — in-place shuffling
- `np.random.seed()` — reproducible randomness
- Simulations: coin flips, dice rolls, random image generation, noise

**Key Files:**
- `RandomIntegers.py` — Random integers, floats, choices, seeds
- `Simulation.py` — Practical simulations (coin, dice, images, noise)

---

### Day 6 — Linear Algebra Basics
**Goal:** Apply fundamental linear algebra operations using NumPy.

**Topics Covered:**
- Vector operations: addition, subtraction, scalar multiplication
- Dot product with `np.dot()`
- Matrix multiplication with `@` and `np.matmul()`
- Transpose, identity matrix (`np.eye()`), determinant (`np.linalg.det()`)
- Matrix inverse (`np.linalg.inv()`) and verification
- Solving linear equations with `np.linalg.solve()`
- Vector magnitude with `np.linalg.norm()`

**Key Files:**
- `Linear_Algebra_Basics.py` — Vector ops and dot product
- `Matrix_Multiplication.py` — Matrix multiplication, inverse, determinant, solving equations

---

### Day 7 — Mini Project
**Goal:** Apply all learned concepts to analyze a student marks dataset.

**Dataset (`dataset.py`):**
- 5 students × 4 subjects
- Marks range from 67 to 95
- Includes a helper function `assign_grade(arr, low, high)` for grade binning

**Analysis Performed (`project.py`):**
- Dataset inspection (shape, dimensions, size)
- Student-wise total and average marks
- Subject-wise average, highest, and lowest marks
- Identifying the best student using `argmax()`
- Normalization (scaling to 0–1 range)
- Standard deviation analysis to find most/least consistent subjects
- Pass/fail boolean masking (`marks > 50`)
- Grade assignment (A: 85–100, B: 70–85, C: below 70)

---

## How to Use This Repository

1. **Clone or download** the repository
2. **Work day by day** — start with the tutorial `.py` files, then attempt the tasks/questions
3. **Run scripts** in any Python environment with NumPy installed:
   ```bash
   pip install numpy
   python "Day1 - NumPy Arrays/1. Lists vs Arrays.py"
   ```
4. **Check your understanding** with the `Task10.txt` / `question10.txt` (or `.py`) explanation prompts
5. **Complete the Mini Project** on Day 7 to consolidate all skills

---

## Prerequisites

- Python 3.x
- NumPy (`pip install numpy`)

---

## Summary of Concepts Covered

| Category | Concepts |
|----------|----------|
| **Array Basics** | Creation, indexing, slicing, dimensions, shapes, dtypes |
| **Operations** | Element-wise arithmetic, scalar ops, broadcasting, comparison masks |
| **Reshaping** | `reshape`, `flatten`, `transpose`, `-1` inference |
| **Aggregation** | Sum, mean, median, min, max, std, var, cumsum, cumprod, axis ops |
| **Randomness** | `randint`, `rand`, `choice`, `shuffle`, `seed`, simulations |
| **Linear Algebra** | Dot product, matrix multiplication, inverse, determinant, solving equations |
| **Project Skills** | Dataset analysis, normalization, grading, statistical interpretation |

---

This repository serves as a **self-contained NumPy bootcamp** — ideal for beginners transitioning from basic Python to numerical computing.
