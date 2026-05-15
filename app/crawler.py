import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_site(source):
    url = source["start_url"]
    allowed = source["allowed_extensions"]

    results = []

    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        links = soup.find_all("a")

        for link in links:
            href = link.get("href")
            if not href:
                continue

            full_url = urljoin(url, href)

            if any(full_url.endswith(ext) for ext in allowed):
                results.append({
                    "source": source["name"],
                    "title": link.text.strip(),
                    "url": full_url
                })

    except Exception as e:
        print(f"Error crawling {url}: {e}")

    return results