#!/usr/bin/python3
"""Defines the module `0-lockboxes` that
   contains a function `canUnlockAll`.
"""


def canUnlockAll(boxes):
    """The method that determines if all the boxes
       can be opened.

       Agrs:
         boxes(list): list of lists
    """
    num_boxes = len(boxes)
    # Keep track of visited boxes.
    visited = [False] * num_boxes

    # Useing a depth-first search (DFS) algorithm
    # Recursively mark the current box as visited.
    def dfs(box):
        visited[box] = True
        # Iterate through each key in the current box.
        for key in boxes[box]:
            # Call the `dfs` function unvisited boxes.
            if not visited[key]:
                dfs(key)

    dfs(0)  # Start the search
    return all(visited)
