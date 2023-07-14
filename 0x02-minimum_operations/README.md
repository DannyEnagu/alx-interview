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

To calculate the fewest number of operations needed to result in exactly `n(H)` characters in the file:

1. Define and initalize two a variables,
   - `operations = 0` # store the numbers of operations 
   - `prime = 2`      # store the prime factores of n
2. In a while loop, iterate untile `n <= 1`.
3. On each iteration check `n` divide by `prime` is equal to zero `(n % prime == 0)`.
4. If `prime` is a factor of `n` increase the number of operations by `prime` `(operations += prime).`
5. Else, increase prime by 1 `(prime += 1)` and repeat step 2 to 5.
6. Return `operations`.
