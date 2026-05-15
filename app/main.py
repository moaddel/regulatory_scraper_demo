import json
import logging
from crawler import crawl_site
from manifest import save_manifest

logging.basicConfig(
    filename="../logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_sources():
    with open("../config/sources.json", "r") as f:
        return json.load(f)

def main():
    sources = load_sources()
    all_results = []

    for source in sources:
        print(f"Crawling: {source['name']}")
        logging.info(f"Started crawling {source['name']}")

        results = crawl_site(source)
        all_results.extend(results)

    save_manifest(all_results)

    print("Done ✔")
    logging.info("Scraping completed")

if __name__ == "__main__":
    main()