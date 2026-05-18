import csv
import os
from datetime import datetime


def save_manifest(rows, filename="output/manifest.csv"):

    os.makedirs("output", exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "source",
            "url",
            "local_path",
            "download_date"
        ])

        for row in rows:
            writer.writerow(row)