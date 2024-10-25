#!/usr/bin/python3

""" this module contains a script that parses log """


import sys
import re

# Define the regex pattern
substring_a = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] '
substring_b = r'(\"\w+ \S+ HTTP/1.1\") (\d{3}) (\d+)$'
log_pattern = re.compile(
    r'(\d{1,3}\.){3}\d{1,3} - ' + substring_a + substring_b
)

total_size = 0
status_code_counts = {}
line_count = 0


def print_stats():
    """Print the total file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")


try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if match:
            ip_address, date, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            total_size += file_size

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
