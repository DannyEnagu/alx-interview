# 0x09. Island Perimeter

`Algorithm` `Python`

## Task

### 0. Island Perimeter

Create a function def `island_perimeter(grid):` that returns the perimeter of the island described in
`grid`:

  - `grid` is a list of list of integers:
    - 0 represents water
    - 1 represents land
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically (not diagonally).
    - `grid` is rectangular, with its width and height not exceeding 100
  - The `grid` is completely surrounded by water
  - There is only one island (or nothing).
  - The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island)

### Usage Example

```
guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

guillaume@ubuntu:~/0x09$ 
```

### Expected Output

```
guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$ 
```

## Solution

  The Goal is to find the perimiter of a rectangular `grid` (i.e Island) that is surrounded by water.
Note, the perimiter of a rectangle can be calculated as such:
  p = 2(l + w).
  where
    - 2 the two dimensions of a rectangle length and width. 
    - l is the length (Horizontal sides) and
    - w is the width (Vertical sides).

But in our case, the height of the island refers the vertical side and the width is the horizontal sides.
Therefore: p = 2(h + w).

We will attempt to solve the island problem using two loops an outer loop and an inner loop. The outer
loop will loop throught the grid rows and the inner loop, loops through a row columns once.

We start both our outer and inner loop at item 2, and stop just before the last item in the grid because
we were told that the grid is completely surrounded by water. So it will be a wast of time to start at the
first items.

### Algorithm

