import csv
from datetime import datetime

def save_manifest(data):
    path = "../output/manifest.csv"

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "source", "title", "url", "download_date"
        ])

        writer.writeheader()

        for row in data:
            row["download_date"] = datetime.now().isoformat()
            writer.writerow(row)