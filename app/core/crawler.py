import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def safe_request(url, retries=3):
    for _ in range(retries):
        try:
            return requests.get(url, timeout=10)
        except:
            pass
    return None


def extract_links(url, allowed_extensions):


    if any(url.endswith(ext) for ext in allowed_extensions):
        return [url]

    res = safe_request(url)
    if not res:
        return []

    soup = BeautifulSoup(res.text, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):
        full_url = urljoin(url, a["href"])

        if any(full_url.endswith(ext) for ext in allowed_extensions):
            links.append(full_url)

    return links



def crawl_site(site):
    return extract_links(
        site["start_url"],
        site["allowed_extensions"]
    )