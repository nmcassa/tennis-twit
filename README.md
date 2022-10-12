# tennis-twit
 Tennis Twitter Bot

## tourn.py
 Given the url of a tournament page from atpworldtour.com will create this object:

```python
 {
    "url": "https://www.atptour.com/en/tournaments/paris/352/overview",
    "name": "Rolex Paris Masters",
    "loc": "Paris, France",
    "time": "October 31 - November 06 "
}
```

## main.py
 Currently goes and creates a tournament object for every tournament in this month:

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