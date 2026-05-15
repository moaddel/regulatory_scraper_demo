from crawler import crawl_site
from config import load_sources
from downloader import download_file
from manifest import save_manifest


def main():

    sources = load_sources()

    all_results = []

    manifest_rows = []

    for source in sources:

        print(f"Crawling: {source['name']}")

        results = crawl_site(source)

        for file_url in results:

            saved_path = download_file(file_url)

            print(f"Downloaded: {saved_path}")

            manifest_rows.append([
                source["name"],
                file_url,
                saved_path
            ])

        all_results.extend(results)

    save_manifest(manifest_rows)

    print("Done ✔")


if __name__ == "__main__":
    main()