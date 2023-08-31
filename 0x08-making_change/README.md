# 0x08. Making Change

`Algorithm` `Python`

## Tasks

### 0. Change comes from within

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

  - Prototype: `def makeChange(coins, total)`
  - Return: fewest number of coins needed to meet `total`
    - If `total` is `0` or less, return `0`
    - If `total` cannot be met by any number of coins you have, return `-1`
  - `coins` is a list of the values of the coins in your possession
  - The value of a coin will always be an integer greater than `0`
  - You can assume you have an infinite number of each denomination of coin in the list
  - Your solution’s runtime will be evaluated in this task

### Usage

```
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
```

### Expected Output

```
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
```
## Solution Algorithem

1. Sort the pile/list of coins in decending order.
2. Set `number_of_coin = 0`.
2. Loop through the list once. one item/coin at a time.
3. Count the number of times current coin amount can be gotten from total amount `(i.e count = total // coint)` and `(remender = total % coin)`.
4. check if after step 3, remainder is greater than zero(0):
  - total = remainder`, `number_of_coin += count`. continue to next item/coin.
  - Else, `number_of_coin  += count` return early `number_of_coin`.
5. if current item/coin is the last on the list of coins return `-1` (i.e could not make change).

