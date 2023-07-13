# 0x02. Minimum Operations


## Tasks

## 0. Minimum Operations
In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

    - Prototype: def minOperations(n)
    - Returns an integer
    - If `n` is impossible to achieve, return `0`

**Example:**

`n = 9`

`H` => `Copy All `=> `Paste` => `HH` => `Paste` => `HHH` => `Copy All `=> `Paste` => `HHHHHH` => `Paste` => `HHHHHHHHH`

Number of operations: `6`

```
carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$
```

```
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
```

## Solution

Minimum Operations:

Noticed that Minimum Operations is just the sum of the prime factors of the number `n`

`2 x 2 = 4` `(ans: 2 + 2 = 4)`
`3 x 3 = 9` `( ans: 3 + 3 = 6)`
`2 x 2 x 3 = 12` `(ans: 2+2+3=7)`
`…`
`…`

To calculate the fewest number of operations needed to result in exactly n 'H' characters in the file, you can use a dynamic programming approach.

we use an array `dp (i.e dynamic programming)` to store the minimum number of operations needed for each index up to n. The base case `dp[1] = 0` indicates that no operations are needed when `n = 1`.

The outer loop iterates from 2 to `n`, considering each number and finding the minimum operations required to reach that number of `'H'` characters. The inner loop iterates from `1` to `i - 1`and checks if `i` is divisible by `j`. If it is, we consider the option of `copying` `j` characters and `pasting` them `(i // j) - 1` times to reach `i` characters. We update the minimum operations using `min(dp[i], dp[j] + i // j)`.

Finally, the method returns `dp[n]`, which represents the fewest number of operations needed to result in exactly `n` `'H'` characters in the file.
