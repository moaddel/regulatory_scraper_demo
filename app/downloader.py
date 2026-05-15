import os
import httpx
import hashlib

async def download_file(url, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.get(url)

    content = r.content

    with open(path, "wb") as f:
        f.write(content)

    return hashlib.md5(content).hexdigest()