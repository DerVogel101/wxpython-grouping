"""
    Number to Text Conversion Module
    ===============================

    This module provides utilities for converting numbers to text representations,
    particularly for Excel-style column naming.

    .. inheritance-diagram:: groupbuilder.utility.number_to_text
       :parts: 1

    .. autosummary::
       :toctree: generated/

       number_to_column
"""

def number_to_column(n: int) -> str:
    """
    Convert a given positive integer to its corresponding Excel-style column name.

    This function implements the algorithm to convert numerical column indices to
    alphabetical Excel-style column labels (e.g., A, B, ..., Z, AA, AB, etc.).

    The conversion follows these rules:
    - Column 1 maps to 'A'
    - Column 26 maps to 'Z'
    - Column 27 maps to 'AA'
    - Column 52 maps to 'AZ'
    - Column 53 maps to 'BA'
    - And so on...

    :param n: The column number to convert. Must be 1 or greater.
    :type n: int
    :return: The corresponding column name in Excel-style (e.g., 1 -> 'A', 27 -> 'AA').
    :rtype: str
    :raises ValueError: If the input number is less than 1.

    .. autosummary::
       :toctree: generated/
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