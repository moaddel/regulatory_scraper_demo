import logging

from crawler import crawl_site
from config import load_sources
from downloader import download_file
from manifest import save_manifest


logging.basicConfig(level=logging.INFO)


def main():

    sources = load_sources()

    manifest_rows = []

    for source in sources:

        print(f"Crawling: {source['name']}")

        results = crawl_site(source)

        for file_url in results:

            saved_path, skipped = download_file(file_url)

            if skipped:
                print(f"Skipped (already exists): {saved_path}")
            else:
                print(f"Downloaded: {saved_path}")
                logging.info(f"Downloaded: {saved_path}")

            manifest_rows.append([
                source["name"],
                file_url,
                saved_path
            ])

    save_manifest(manifest_rows)

    print("Done ✔")


if __name__ == "__main__":
    main()