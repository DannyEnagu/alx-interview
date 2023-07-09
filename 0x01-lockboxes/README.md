# 0x01. Lockboxes
`Algorithm` `Python`

To check if all the boxes can be opened in the given list of arrays, you can use a depth-first search (DFS) algorithm or a breadth-first search (BFS) algorithm. Here's an approach using a depth-first search:

1. Initialize a visited array or set to keep track of the boxes that have been visited.
2. Create a helper function, let's call it dfs, which takes a box number as input.
3. Inside the dfs function:
   - Mark the current box as visited.
   - Iterate through each key in the current box's list of keys:
      - If the key is already visited, continue to the next key.
      - Otherwise, recursively call the dfs function with the key as the input.
4. Call the dfs function starting from the first box (box 0).
5. After the dfs function returns, check if all boxes have been visited. If they have, return True; otherwise, return False.

In the solution located in the `0-lockboxes.py`, the `canUnlockAll` function takes the list of boxes as input and returns True if all boxes can be opened and False otherwise. The algorithm starts from box 0 and performs a depth-first search to visit all the connected boxes. It uses the visited array to keep track of visited boxes. Finally, it checks if all boxes have been visited using the all function and returns the result.

