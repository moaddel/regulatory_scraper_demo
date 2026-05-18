# RegulatoryScraper

A modular Python-based regulatory document scraping framework designed for bulk downloading PDFs and Excel files from AU/NZ regulatory agencies.

---

## Features

- Modular scraping architecture
- Source adapter system
- PDF / Excel bulk downloading
- Playwright integration for JS-rendered sites
- Deduplication handling
- Structured output pipeline
- Manifest CSV generation
- Retry-safe downloads
- Production-oriented project structure

---

## Tech Stack

- Python 3.11+
- requests
- BeautifulSoup4
- Playwright
- CSV manifest pipeline

---

## Project Structure

```text
app/
│
├── core/
│   ├── crawler.py
│   ├── downloader.py
│   ├── manifest.py
│   └── playwright_adapter.py
│
├── sources/
│   └── w3c_test.py
│
├── main.py
└── config.py

---

## Supported Capabilities

- Static HTML crawling
- JS-rendered page extraction
- Direct PDF downloads
- Multi-source architecture
- Configurable source adapters
- Deduplication-safe execution

---

## Example Output

```text
Crawling: W3C_Test
Downloaded: output/dummy.pdf
Done ✔
```

---

## Output Structure

```text
output/
    manifest.csv
    dummy.pdf
```

---

## Run

```bash
pip install -r requirements.txt

python app/main.py
```

---

## Future Improvements

- Multi-agency crawling
- Pagination support
- Incremental crawling
- File hashing
- Metadata extraction
- Async downloads

---

## Author

Mahdi Moaddel
