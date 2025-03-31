# Завдання 1:
# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте 
# на наявність дублікатів і приберіть їх. 
# Результат запишіть у файл result_<your_second_name>.csv

"""
Combines two CSV files, removes duplicates, and saves the result.
Reads data from 'random.csv' and 'rmc.csv' in 'work_with_csv' folder,
removes duplicate rows, and writes the result to 'result_benedek.csv'.
"""

import csv
from pathlib import Path

def read_csv(filepath: Path) -> list:
    """Reads a CSV file and returns its content as a list of rows."""
    with open(filepath, "r", encoding="utf-8") as my_file:
        reader = csv.reader(my_file)
        return list(reader)

def write_csv(filepath: Path, content: list):
    """Writes a list of rows to a CSV file."""
    with open(filepath, "w", encoding="utf-8", newline="") as my_file:
        writer = csv.writer(my_file, delimiter=";")
        writer.writerows(content)

if __name__ == "__main__":
    input_folder = Path(__file__).parent.parent / "work_with_csv"
    file1 = read_csv(input_folder / "random.csv")
    file2 = read_csv(input_folder / "rmc.csv")

    combined = file1 + file2
    unique_rows = set()
    for row in combined:
        unique_rows.add(tuple(row))

    result = [list(row) for row in unique_rows]

    output_file = Path(__file__).parent.parent / "result_benedek.csv"
    write_csv(output_file, result)

    print(f"Finished! Result saved to: {output_file}")
