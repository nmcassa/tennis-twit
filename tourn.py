import json
import re
import requests
from bs4 import BeautifulSoup
from json import JSONEncoder

class Tournament:
    def __init__(self, url: str) -> None:
        self.url = "https://www.atptour.com" + url
        page = get_parsed_page(self.url)

        self.build(page)

    def __str__(self) -> None:
        return jsonify(self)

    def build(self, page: str) -> None:
        basic_info = page.find("div", {"class": "inner-wrap"})
        self.name = basic_info.find("div", {"class": "last-name"}).text
        basic_info = basic_info.findAll("div", {"class": "hero-date-range"})
        self.loc = basic_info[0].text
        self.time = basic_info[1].text.replace("\r\n", "")[20:]
        self.time = self.time[:len(self.time) - 21]


def get_parsed_page(url: str) -> None:
    # This fixes a blocked by cloudflare error i've encountered
    headers = {
        "referer": "https://letterboxd.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    return BeautifulSoup(requests.get(url, headers=headers).text, "lxml")

def jsonify(info: str) -> str:
    return json.dumps(info, indent=4,cls=Encoder)

class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

if __name__ == "__main__":
    to = Tournament("/en/tournaments/tokyo/329/overview")
    print(to)
