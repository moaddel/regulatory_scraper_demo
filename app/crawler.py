import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def extract_links(url, allowed_extensions):


    if any(url.endswith(ext) for ext in allowed_extensions):
        return [url]


    res = requests.get(url, timeout=10)

    soup = BeautifulSoup(res.text, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):
        full_url = urljoin(url, a["href"])

        if any(full_url.endswith(ext) for ext in allowed_extensions):
            links.append(full_url)

    return links


def crawl_site(site):
    links = extract_links(
        site["start_url"],
        site["allowed_extensions"]
    )

    return links