from tqdm import tqdm
import requests
from bs4 import BeautifulSoup

comediehumaine_url = "https://www.gutenberg.org/ebooks/search/?query=la+com%C3%A9die+humaine&submit_search=Go%21"
link_format = "https://www.gutenberg.org{text_id}.txt.utf-8"

urls = [
    "https://www.gutenberg.org/ebooks/41211.txt.utf-8",
    "https://www.gutenberg.org/files/43851/43851-0.txt",
    "https://www.gutenberg.org/files/45060/45060-0.txt",
    "https://www.gutenberg.org/files/48082/48082-0.txt",
    "https://www.gutenberg.org/files/49482/49482-0.txt",
    "https://www.gutenberg.org/files/51381/51381-0.txt",
    "https://www.gutenberg.org/files/52831/52831-0.txt",
    "https://www.gutenberg.org/files/54723/54723-0.txt",
    "https://www.gutenberg.org/files/55860/55860-0.txt",
    "https://www.gutenberg.org/files/58244/58244-0.txt",
    "https://www.gutenberg.org/files/60551/60551-0.txt",
    "https://www.gutenberg.org/ebooks/67264.txt.utf-8",
    "https://www.gutenberg.org/ebooks/71022.txt.utf-8"
]


html = requests.get(comediehumaine_url).content
soup = BeautifulSoup(html, "html.parser")

for url in tqdm(urls):
    title = url.split("/")[-1]
    title = title.replace(".utf-8", "")
    resp = requests.get(url)
    with open(f"data/{title}", "w") as f:
        f.write(resp.content.decode("utf-8"))


