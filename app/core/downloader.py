import os
import requests


def download_file(url, output_folder="output"):

    os.makedirs(output_folder, exist_ok=True)

    filename = url.split("/")[-1]
    filepath = os.path.join(output_folder, filename)


    if os.path.exists(filepath):
        return filepath, True   # True = skipped

    response = requests.get(url, stream=True, timeout=15)

    with open(filepath, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    return filepath, False  # False = newly downloaded