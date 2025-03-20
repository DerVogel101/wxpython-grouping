def number_to_column(n: int) -> str:
    """
    Convert a given positive integer to its corresponding Excel-style column name.

    :param n: The column number to convert. Must be 1 or greater.
    :type n: int
    :return: The corresponding column name in Excel-style (e.g., 1 -> 'A', 27 -> 'AA').
    :rtype: str
    :raises ValueError: If the input number is less than 1.
    """
    if n < 1:
        raise ValueError("Number must be 1 or greater")

    result = ""
    while n > 0:
        n -= 1  # Zero-based indexing
        result = chr(n % 26 + ord('A')) + result
        n //= 26

    return result

if __name__ == '__main__':
    # Test cases
    for i in range(1, 30):
        print(i, "->", number_to_column(i))