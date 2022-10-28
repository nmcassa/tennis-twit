import json
import re
import requests
from bs4 import BeautifulSoup
from json import JSONEncoder

class Tournament:
    def __init__(self, url: str) -> None:
        self.url = "https://www.atptour.com" + url
        page = get_parsed_page(self.url)

        #does all the work to create the thing
        self.build(page)

    def __str__(self) -> None:
        return jsonify(self)

    def build(self, page: str) -> None:
        #basic info contains oddly formatted tournament title, location, and time
        basic_info = page.find("div", {"class": "inner-wrap"})
        self.name = basic_info.find("div", {"class": "last-name"}).text

        basic_info = basic_info.findAll("div", {"class": "hero-date-range"})

        self.loc = basic_info[0].text
        self.time = basic_info[1].text.replace("\r\n", "")[20:]
        self.time = self.time[:len(self.time) - 21]

        #tourn_info is #sgls players, #dbls teams, surface, finacials
        tourn_info = page.find("div", {"class": "player-profile-hero-table"})
        tourn_info = tourn_info.findAll("div", {"class": "item-value"})

        self.surface = tourn_info[0].text
        self.prize = tourn_info[1].text.replace("\u20ac", "")
        self.commit = tourn_info[2].text.replace("\u20ac", "")

        #gives the players in the scrollable WHO IS PLAYING thing
        players = page.findAll("div", {"class": "action-info"})
        self.top_players = []

        #These players are in order from top seed to 8th seed
        for player in players:
            player = player.find("a")
            self.top_players.append(player['ga-label'])


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
    to = Tournament("/en/tournaments/vienna/337/overview")
    print(to)
