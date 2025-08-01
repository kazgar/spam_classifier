from bs4 import BeautifulSoup


class Mail:
    def __init__(self, body: str, type: str):
        self.body: str = body
        self.type: str = type

    def transform_mail(self):
        match self.type:
            case "text/html":
                soup = BeautifulSoup(self.body, "html.parser")
                text = soup.get_text()
                for link in soup.find_all("a"):
                    text += f' {link.get("href")}'

            case _:
                text = self.body

        print(text)


class MailBox:
    def __init__(self):
        self.mailbox: list[Mail] = []
        self.vocab: set[str] = set()

    def add_mail(self, mail: Mail):
        self.mailbox.append(mail)
