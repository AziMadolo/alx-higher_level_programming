#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """Print accumulated metrics.

    Args:
        total_size (int): The accumulated file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(total_size))
    for key in sorted(status_codes):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))

def main():
    size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    valid_codes = set(status_codes.keys())

    try:
        for line in sys.stdin:
            parts = line.split()
            
            try:
                status_code = parts[-2]
                if status_code in valid_codes:
                    status_codes[status_code] += 1
            except IndexError:
                pass

            try:
                size += int(parts[-1])
            except (IndexError, ValueError):
                pass

    except KeyboardInterrupt:
        pass

    print_stats(size, status_codes)

if __name__ == "__main__":
    main()

