from codecs import ignore_errors

import chardet
import csv


# Function to detect the encoding of a file
def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read(2048)  # Read a portion of the file for encoding detection
        detected_encoding = chardet.detect(raw_data)
    return detected_encoding['encoding']


# Function to detect the CSV separator and load the file
def detect_csv_separator_and_load(file_path):
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