from tourn import *

if __name__ == "__main__":
	tourny_page = get_parsed_page("https://www.atptour.com/en/tournaments")
	tourny_page = tourny_page.findAll("div", {"class": "expand"})
	curr_month = tourny_page[0].findAll("td", {"class": "title-content"})
	for item in curr_month:
		curr = Tournament(item.findChildren()[0]["href"])
		print(curr)