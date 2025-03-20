import chardet
import csv

def detect_file_encoding(file_path: str) -> str:
    """
    Detect the encoding of a file.

    :param file_path: The path to the file whose encoding is to be detected.
    :type file_path: str
    :return: The detected encoding of the file.
    :rtype: str
    """
    with open(file_path, 'rb') as f:
        raw_data = f.read(2048)  # Read a portion of the file for encoding detection
        detected_encoding = chardet.detect(raw_data)
    return detected_encoding['encoding']

def detect_csv_separator_and_load(file_path: str) -> tuple:
    """
    Detect the CSV separator and load the file content.

    :param file_path: The path to the CSV file to be loaded.
    :type file_path: str
    :return: A tuple containing:
        - list: The content of the CSV file as a list of rows.
        - str: The detected delimiter used in the CSV file.
        - str: The detected encoding of the CSV file.
    :rtype: tuple
    """
    encoding = detect_file_encoding(file_path)
    with open(file_path, 'r', encoding=encoding, errors="ignore") as file:
        dialect = csv.Sniffer().sniff(file.read(1024))
        file.seek(0)  # Reset file pointer to the start
        reader = csv.reader(file, delimiter=dialect.delimiter)
        data = list(reader)  # Load the entire CSV content
    result_data = []
    for row in data:
        if row:
            result_data.append(row)
    return result_data, dialect.delimiter, encoding

if __name__ == "__main__":
    file_path = 'dqi_user2.csv'
    data, delimiter, encoding = detect_csv_separator_and_load(file_path)
    print(data)
    print(delimiter)
    print(encoding)