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

  The Goal is to find the total perimeter of the Island (i.e connected 1 cells) that is surrounded by
water (i.e 0 cells).

I used two nested for loops. The outer loop, go over the grid rows, the inner the grid columns.

Finding the perimeter of an Island is simply calcutating the total of all the sides of a square land
`(1 cell)` that are next to water `(0 cells)`. The perimeter represents the total length of the boundary
that surrounds the land cells (the island).

Where, each side of the given square `(1 cell)` has a length of `1`. A single land cell `(1 cell)`
surrounded by water cells `(0 cells)`, has a total length of 4. Therefore, if it's closest neighbour
`(top or botom or right or even left cell)` is a land cell, we then need to subtract those side(s) from 4,
and add up the remaining remaining lengths from all the land cells that makes up the Island to get the
final perimeter of the Island area.

### Algorithm

1. Set `perimeter = 0`
2. Start loop
3. `IF` current cell value is `1` `THEN` `perimeter += 4` MOVE to step 4 `ELSE` `JUMP TO STEP` 5
4. Check adjacent cells (up, down, left, and right)
   - `IF` top cell value `1` `THEN` `perimeter -= 2`
   - `IF` left cell value `1` `THEN` `perimeter -= 2`
   - `ELSE` `JUMP TO STEP` 5
5. `Else` continue to next cell

