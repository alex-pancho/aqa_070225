import csv
from pathlib import Path

def read_file(filepath: Path) -> list:
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_csv(filepath: Path, content: list, keys):
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, delimiter=",", fieldnames=keys)  # quoting=csv.QUOTE_ALL
        writer.writerows(content)


if __name__ == "__main__":
    first_csv = Path(__file__).parent / "random.csv"
    content_1 = read_file(first_csv)
    keys_1 = content_1[0].keys()

    second_csv = Path(__file__).parent / "random-michaels.csv"
    content_2 = read_file(second_csv)
    keys_2 = content_2[0].keys()

    content_union = content_1 + content_2
    keys_union = set().union(keys_1, keys_2)

    result = [x for x in content_union if x not in content_1 or x not in content_2]
    result_csv = Path(__file__).parent / "result_hello.csv"

    write_csv(result_csv, result, keys_union)
