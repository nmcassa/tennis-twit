#import datetime
from tourn import *

##KEEGAN dont forget ----- 
##when crossing over to another month there will be 
##more items after a tournment.time.split(' ')
##so watch out!!

#list of tournaments that are currently on
def get_curr_tourns(tourns: list[Tournament]) -> list[Tournament]:
	#TODO
	return 1

#list of tournaments that are occuring in the next week
def get_next_tourns(tourns: list[Tournament]) -> list[Tournament]:
	#TODO
	return 1

#return day number of tourn
def get_curr_day(tourn: Tournament) -> int:
	#TODO
	return -1

def get_curr_month_tourns() -> list[Tournament]:
	tourny_page = get_parsed_page("https://www.atptour.com/en/tournaments")
	tourny_page = tourny_page.findAll("div", {"class": "expand"})
	curr_month = tourny_page[0].findAll("td", {"class": "title-content"})

	ret = []

	for item in curr_month:
		ret.append(Tournament(item.findChildren()[0]["href"]))

	return ret

if __name__ == "__main__":
	print(get_curr_month_tourns())