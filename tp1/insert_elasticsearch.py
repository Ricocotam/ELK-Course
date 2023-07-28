import re
from bs4 import BeautifulSoup
from glob import glob
from tqdm import tqdm

from elasticsearch import Elasticsearch

es = Elasticsearch("http://elastic:changeme@localhost:9200")
# Crée un index
#es.indices.create(index="elk-course-0001")

def format_chapter(book_name, chapt, chapt_cont):
    return {
        "book_title": book_name,
        "chap_title": chapt.get_text(strip=True),
        "chapt_content": "\n".join(chapt_cont)
    }


for fn in glob("*.html"):
    with open(fn, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    print("File", fn)
    books = soup.find_all("h2", {"id": {re.compile(r"^chap_\d+")}})
    formatted_chapters = []
    for book in books:
        book_name = book.get_text(strip=True)
        print("Book", book_name)
        chapters = [book]
        for sib in book.next_siblings:
            if sib.name == "h2":
                break
            if sib.name == "h3":
                chapters.append(sib)
        formatted_chapters = []
        for chapt in tqdm(chapters):
            chapt_head = chapt
            chapt_cont = []
            for sib in chapt_head.next_siblings:
                chapt_cont.append(sib.get_text(strip=True))
                if sib.name == "h3" or sib.name == "h2":
                    break
            chapt = format_chapter(book_name, chapt, chapt_cont)
            es.index(index="elk-course-0001", document=chapt)
