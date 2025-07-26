
def format_indian_currency(number):
    num_str = f"{number:.4f}".rstrip('0').rstrip('.')
    if '.' in num_str:
        integer, decimal = num_str.split('.')
    else:
        integer, decimal = num_str, ''

    n = len(integer)
    if n <= 3:
        formatted = integer
    else:
        start = integer[:-3]
        end = integer[-3:]
        parts = []
        while len(start) > 2:
            parts.insert(0, start[-2:])
            start = start[:-2]
        if start:
            parts.insert(0, start)
        formatted = ','.join(parts + [end])

    return formatted + ('.' + decimal if decimal else '')

# Example usage
if __name__ == "__main__":
    print(format_indian_currency(123456.7891))  # Output: 1,23,456.7891
