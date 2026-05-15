from crawler import crawl_site
from config import load_sources


def main():
    sources = load_sources()

    all_results = []

    for source in sources:
        print(f"Crawling: {source['name']}")
        results = crawl_site(source)
        all_results.extend(results)

    print("Done ✔")


if __name__ == "__main__":
    main()