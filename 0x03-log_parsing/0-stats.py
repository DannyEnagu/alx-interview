#!/usr/bin/python3
"""
The script reads `stdin` line by line and computes metrics:

    File size: <total size>
    <status code>: <number>
"""
import sys
import re


codes = [200, 301, 400, 401, 403, 404, 405, 500]
req_stats = {key: 0 for key in codes}
total_file_size = 0


def print_stat(req_dict):
    """Print request stats"""

    for key in req_dict.keys():
        if req_dict[key] > 0:
            print("{}: {}".format(key, req_dict[key]))


for i, line in enumerate(sys.stdin):
    try:
        line = line.strip()
        # Find all space followed by number in line => list
        nums = re.findall(r'\s\d+\b', line)
        status, size = nums[-2:]  # Get last two numbers from list

        # Check if status can be converted to integer
        if status.strip().isdigit():
            req_stats[int(status)] += 1
            total_file_size += int(size)

        if i % 10 == 0 and i > 0:
            print(f"File size: {total_file_size}")
            print_stat(req_stats)

    except KeyboardInterrupt:  # Handle KeyboardInterrupt
        print(f"File size: {total_file_size}")
        print_stat(req_stats)
