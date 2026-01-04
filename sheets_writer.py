import csv
from pathlib import Path

def write_to_sheet(data, path="data/google_sheet.csv"):
    file_exists = Path(path).exists()

    with open(path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)
