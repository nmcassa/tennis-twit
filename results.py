from tourn import *

class Results:
	def __init__(self, tourn: Tournament):
		page = self.build_page(tourn)
		self.dates = self.get_dates(page)

		self.results = {}

		for date in self.dates:
			self.results[date] = self.get_results(page, date)

	def __str__(self):
		return jsonify(self)

	def build_page(self, tourn: Tournament) -> BeautifulSoup:
		page = get_parsed_page(tourn.url)
		page = page.find("li", {"data-title": "Results"}).find("a")

		#add attribute to dict and get page
		self.url = page['href']

		return get_parsed_page("https://www.atptour.com" + self.url)

	def get_dates(self, page: BeautifulSoup) -> list[str]:
		dates = page.find("ul", {"data-value": "matchdate"}).findAll("li")[1:]

		ret = []

		for date in dates:
			ret.append(date['data-value'])

		return ret

	def get_results(self, page: BeautifulSoup, date: str):
		matches = page.find("div", {"id": "scoresResultsContent"})
		matches = matches.findAll("tr")

		ret = []

		#get info
		for match in matches:
			single = {}

			#creates a dict to hold each player
			single["player_one"] = {}
			single["player_two"] = {}

			##if it finds none it's a header row
			seeds = match.findAll("td", {"day-table-seed"})
			if seeds == None:
				continue
			else:
				try:
					single["player_one"]["seed"] = seeds[0].find("span").text.replace("\r\n", "")[21:]
					single["player_one"]["seed"] = single["player_one"]["seed"][:len(single["player_one"]["seed"])-17]
				except:
					pass
				try:
					single["player_two"]["seed"] = seeds[1].find("span").text.replace("\r\n", "")[21:]
					single["player_two"]["seed"] = single["player_two"]["seed"][:len(single["player_two"]["seed"])-17]
				except:
					pass

			names = match.findAll("td", {"day-table-name"})
			print(names)

			#player_one
			name_one = names[0].findAll("a")
			name_two = names[1].findAll("a") #player_two
			if len(name_one) == 1:
				single["type"] = "singles"
				single["player_one"]["name"] = name_one[0].text
				single["player_two"]["name"] = name_two[0].text
			else:
				single["type"] = "doubles"
				single["player_one"]["name"] = [name_one[0].text, name_one[1].text]
				single["player_two"]["name"] = [name_two[0].text, name_two[1].text]
			
			ret.append(single)

		return ret

if __name__ == "__main__":
	to = Tournament("/en/tournaments/vienna/337/overview")
	re = Results(to)
	print(re)