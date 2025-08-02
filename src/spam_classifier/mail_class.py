import re

from bs4 import BeautifulSoup
from nltk.stem.snowball import SnowballStemmer
from urlextract import URLExtract


class Mail:
    def __init__(self, body: str, type: str):
        self.body: str = body
        self.type: str = type

    def transform_mail(self):
        match self.type:
            case "text/html":
                soup = BeautifulSoup(self.body, "html.parser")
                body = soup.get_text()
                for link in soup.find_all("a"):
                    body += f' {link.get("href")}'

            case _:
                body = self.body

        body = re.sub(r"(\s*\n)+", " ", body, flags=re.M | re.S)

        extractor = URLExtract()
        urls = extractor.find_urls(body)
        for url in urls:
            body = body.replace(url, "URL ")

        body = re.sub(r"\b[\w.-]+@[\w.-]+\.\w+\b", "EMAIL ", body, flags=re.M | re.S)
        body = re.sub(r"[^\w\s]|_", "", body, flags=re.M | re.S)
        body = body.lower().split()

        stemmer = SnowballStemmer("english")
        word_dict = {}
        for word in body:
            word = stemmer.stem(word)
            word_dict[word] = word_dict.get(word, 0) + 1

        return word_dict
