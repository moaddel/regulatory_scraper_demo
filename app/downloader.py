import os
import requests


def download_file(url, output_folder="output"):
    os.makedirs(output_folder, exist_ok=True)

    filename = url.split("/")[-1]

    filepath = os.path.join(output_folder, filename)

    response = requests.get(url, stream=True)

    with open(filepath, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    return filepath