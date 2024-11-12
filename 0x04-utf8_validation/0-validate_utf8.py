#!/usr/bin/env python3

""" utf-8 validation module """


def validUTF8(data):
    idx = 0
    while idx < len(data):
        byte = data[idx]

        # Check if it starts with '0' (1-byte character)
        if (byte & 0b10000000) == 0:
            # 1-byte character (valid)
            idx += 1
        # Check if it starts with '110' (2-byte character)
        elif (byte & 0b11100000) == 0b11000000:
            # Expect 1 continuation byte
            if idx + 1 >= len(data) or (data[idx + 1] &
                                        0b11000000) != 0b10000000:
                return False
            idx += 2
        # Check if it starts with '1110' (3-byte character)
        elif (byte & 0b11110000) == 0b11100000:
            # Expect 2 continuation bytes
            if idx + 2 >= len(data) or (data[idx + 1] & 0b11000000)\
                    != 0b10000000 or (data[idx + 2] & 0b11000000)\
                    != 0b10000000:
                return False
            idx += 3
        # Check if it starts with '11110' (4-byte character)
        elif (byte & 0b11111000) == 0b11110000:
            # Expect 3 continuation bytes
            if idx + 3 >= len(data) or (data[idx + 1] & 0b11000000)\
                    != 0b10000000 or (data[idx + 2] & 0b11000000)\
                    != 0b10000000 or (data[idx + 3] & 0b11000000)\
                    != 0b10000000:
                return False
            idx += 4
        else:
            return False  # Invalid leading byte

    return True
