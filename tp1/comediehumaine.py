from tqdm import tqdm
import requests
from bs4 import BeautifulSoup

comediehumaine_url = "https://www.gutenberg.org/ebooks/search/?query=la+com%C3%A9die+humaine&submit_search=Go%21"
link_format = "https://www.gutenberg.org/{text_id}.html.images"

html = requests.get(comediehumaine_url).content
soup = BeautifulSoup(html, "html.parser")

for book in tqdm(soup.find_all("li", {"class": "booklink"})):
    text_id = book.a["href"]
    title = book.find("span", {"class": "title"}).text
    url = link_format.format(text_id=text_id)
    resp = requests.get(url)
    with open(title + ".html", "w") as f:
        f.write(resp.content.decode("utf-8"))


