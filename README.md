# tennis-twit
 Tennis Twitter Bot

## requirements

```
pip install -r requirements.txt
```

## tourn.py
 Given the url of a tournament page from atpworldtour.com will create this object:

```python
{
    "url": "https://www.atptour.com/en/tournaments/paris/352/overview",
    "name": "Rolex Paris Masters",
    "loc": "Paris, France",
    "time": "October 31 - November 06",
    "surface": "Hard",
    "prize": "5,415,410",
    "commit": "6,008,725",
    "top_players": [
        "Carlos Alcaraz",
        "Rafael Nadal",
        "Casper Ruud",
        "Daniil Medvedev",
        "Alexander Zverev",
        "Stefanos Tsitsipas",
        "Novak Djokovic",
        "Cameron Norrie"
    ]
}
```

## match.py
 Given a tournament gets all the matches for the current day. It distinguishes matches between singles and doubles with the ["type"] attribute.

```json
{
    "url": "/en/scores/current/vienna/337/daily-schedule",
    "matches": [
        {
            "round": "QF",
            "player_one": {
                "seed": "NS",
                "name": "Grigor Dimitrov"
            },
            "player_two": {
                "seed": "NS",
                "name": "Marcos Giron"
            },
            "type": "singles"
        },
        {
            "round": "QF",
            "player_one": {
                "seed": "1",
                "name": "Daniil Medvedev"
            },
            "player_two": {
                "seed": "6",
                "name": "Jannik Sinner"
            },
            "type": "singles"
        },
        {
            "round": "QF",
            "player_one": {
                "seed": "5",
                "name": "Hubert Hurkacz"
            },
            "player_two": {
                "seed": "NS",
                "name": "Borna Coric"
            },
            "type": "singles"
        },
        {
            "round": "QF",
            "player_one": {
                "seed": "NS",
                "name": "Daniel Evans"
            },
            "player_two": {
                "seed": "NS",
                "name": "Denis Shapovalov"
            },
            "type": "singles"
        },
        {
            "round": "QF",
            "player_one": {
                "seed": "NS",
                "name": [
                    "Francisco Cerundolo",
                    "Maximo Gonzalez"
                ]
            },
            "player_two": {
                "seed": "WC",
                "name": [
                    "Robin Haase",
                    "Philipp Oswald"
                ]
            },
            "type": "doubles"
        },
        {
            "round": "SF",
            "player_one": {
                "seed": "Q",
                "name": [
                    "Sander Gille",
                    "Joran Vliegen"
                ]
            },
            "player_two": {
                "seed": "WC",
                "name": [
                    "Alexander Erler",
                    "Lucas Miedler"
                ]
            },
            "type": "doubles"
        }
    ]
}
```

## main.py
 Currently goes and creates a tournament object for every tournament in this month (not updated to current release of the object above):

```python
{
    "url": "https://www.atptour.com/en/tournaments/tokyo/329/overview",
    "name": "Rakuten Japan Open Tennis Championships",
    "loc": "Tokyo, Japan",
    "time": "October 03 - 09"
}
{
    "url": "https://www.atptour.com/en/tournaments/astana/9410/overview",
    "name": "Astana Open",
    "loc": "Astana, Kazakhstan",
    "time": "October 03 - 09"
}
{
    "url": "https://www.atptour.com/en/tournaments/gijon/2807/overview",
    "name": "Gijon Open",
    "loc": "Gijon, Spain",
    "time": "October 10 - 16"
}
{
    "url": "https://www.atptour.com/en/tournaments/florence/2805/overview",
    "name": "UniCredit Firenze Open",
    "loc": "Florence, Italy",
    "time": "October 10 - 16"
}
{
    "url": "https://www.atptour.com/en/tournaments/antwerp/7485/overview",
    "name": "European Open",
    "loc": "Antwerp, Belgium",
    "time": "October 17 - 23"
}
{
    "url": "https://www.atptour.com/en/tournaments/stockholm/429/overview",
    "name": "Stockholm Open",
    "loc": "Stockholm, Sweden",
    "time": "October 17 - 23"
}
{
    "url": "https://www.atptour.com/en/tournaments/naples/2809/overview",
    "name": "Tennis Napoli Cup",
    "loc": "Naples, Italy",
    "time": "October 17 - 23"
}
{
    "url": "https://www.atptour.com/en/tournaments/vienna/337/overview",
    "name": "Erste Bank Open",
    "loc": "Vienna, Austria",
    "time": "October 24 - 30"
}
{
    "url": "https://www.atptour.com/en/tournaments/basel/328/overview",
    "name": "Swiss Indoors Basel",
    "loc": "Basel, Switzerland",
    "time": "October 24 - 30"
}
{
    "url": "https://www.atptour.com/en/tournaments/paris/352/overview",
    "name": "Rolex Paris Masters",
    "loc": "Paris, France",
    "time": "October 31 - November 06"
}
```

 In the future hopefully can cull out tournaments that are not currently in play.