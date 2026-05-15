import json
import os

def load_sources():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "..", "config", "sources.json")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)