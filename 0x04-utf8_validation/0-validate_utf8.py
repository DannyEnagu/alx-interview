#!/usr/bin/python3
"""
Defines the module `0-validate_utf8`
"""


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.

    Args:
        data(list): data set that contain multiple characters.

    Return:
        True: if data is a valid UTF-8 encoding, else return False
    """
    number_bytes = 0

    step_1 = 1 << 7
    step_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & step_1 and not (i & step_2)):
                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
