#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

print(makeChange([1256, 54, 48, 16, 102], 0))

print(makeChange([1256, 54, 48, 16, 102], 15))
print(makeChange([15, 20, 24, 30, 40, 60], 120))
print(makeChange([15, 20, 24, 30, 40, 60], 200))
print(makeChange([8, 15, 20, 24, 30, 40, 60], 128))
print(makeChange([32, 2, 3, 4, 5, 6, 8, 10, 64], 130))
