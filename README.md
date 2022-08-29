# RMS Technology Consulting Test

# Introduction

In the below 10x10 grid, three numbers along a horizontal line have been highlighted.

```
8 2 22 97 38 15 0 40 0 75

49 49 99 40 17 81 18 57 60 87

81 49 31 73 55 79 14 29 93 71

52 70 95 23 4 60 11 42 69 24

22 31 16 71 51 67 63 89 41 92

24 47 32 60 99 3 45 2 44 75

32 98 81 28 64 23 67 10 26 38

67 26 20 68 2 62 12 20 95 63

24 55 58 5 66 73 99 26 97 17

21 36 23 9 75 0 76 44 20 45
```

The product of these numbers is 4 x 60 x 11 = 2640.

# Questions

1. How many different combinations are there of three adjacent numbers in the same
direction (up, down, left, right or diagonally) in the 10 x 10 grid?
2. What is the greatest product of three adjacent num

# Requirements

Submit your answers to each of the above questions along with a link to your source code. The
solution should be submitted in Python.

Your source code will be held in GitHub and should contain a function which accepts a grid of
size n x m and finds the greatest product of x adjacent numbers in the same direction. We will
be running a large grid (much larger than the above example) through your method. In Python,
the function signature could look like the following:

```python
def find_greatest_product_of_contiguous_integers(grid: NumberGrid, contiguous_integers: int) -> int:
```

Please also attach any relevant notes/comments along with your submission. Clean, readable,
testable code is preferred.

# Solution

## Quick Start

```python
$ ./rms_tech_test.py TechConsultingTestGrid.csv --contiguous-integers 3
```

### Output

```python
========== QUESTION 1 ==========
How many different combinations are there of 3 adjacent numbers in the same direction (up, down, left, right or diagonally) in the 10 x 10 grid?
Answer: 288
========== QUESTION 2 ==========
What is the greatest product of 3 adjacent numbers in the same direction (up, down, left, right or diagonally) in the 10 x 10 grid?
Answer: 667,755
```

## Validation

The `validate_grid()` function carries out some high-level checks of the input grid and the contiguous integers argument:

- Contiguous integers value must be greater than 0
- Contiguous integers value must be an integer
- Grid must not contain null values
- Grid must not contain non-numeric values
- Grid must be at least 1x1
- Grid must be wider and taller than contiguous integers value

Further assumptions are described in the next section.

## Assumptions

### Cells are non-directional

As stated in the instructional PDF, there is the following clarification:

- Contiguous cells are considered the same whether read left-to-right or right-to-left

The assumption is that this also applies to:

- up-to-down and down-to-up
- top-left-to-bottom-right and bottom-right-to-top-left
- top-right-to-bottom-left and bottom-left-to-top-right

In short, the assumption is that contiguous cells are non-directional.

### Grids are uniform

Grid of size *n x m* are assumed to be uniform in that rows and columns are assumed to be of the same size i.e., grids are rectangular.

### Cells are squares

It is assumed cells are squares (and not other tessellating shapes such as hexagons).