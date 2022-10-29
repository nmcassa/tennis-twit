from tourn import *

class Results:
	def __init__(self, tourn: Tournament):
		page = self.build_page(tourn)
		self.dates = self.get_dates(page)

		self.results = {}

		for date in self.dates:
			page = get_parsed_page("https://www.atptour.com" + self.url + "?matchdate=" + date)
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
		matches = page.find("div", {"id": "scoresResultsContent"}).find("tbody")
		matches = matches.findAll("tr")

		ret = []

		#get info
		for match in matches:
			single = {}

			#creates a dict to hold each player
			single["winner"] = {}
			single["loser"] = {}

			##if it finds none it's a header row
			seeds = match.findAll("td", {"day-table-seed"})
			if seeds == None:
				continue
			else:
				try:
					single["winner"]["seed"] = seeds[0].find("span").text.replace("\r\n", "").replace(" ", "")
					single["winner"]["seed"] = single["winner"]["seed"].replace(" ", "")
				except:
					pass
				try:
					single["loser"]["seed"] = seeds[1].find("span").text.replace("\r\n", "").replace(" ", "")
					single["loser"]["seed"] = single["loser"]["seed"].replace(" ", "")
				except:
					pass

			names = match.findAll("td", {"day-table-name"})

			#winner
			name_one = names[0].findAll("a")
			name_two = names[1].findAll("a") #loser
			if len(name_one) == 1:
				single["type"] = "singles"
				single["winner"]["name"] = name_one[0].text
				single["loser"]["name"] = name_two[0].text
			else:
				single["type"] = "doubles"
				single["winner"]["name"] = [name_one[0].text, name_one[1].text]
				single["loser"]["name"] = [name_two[0].text, name_two[1].text]

			score = match.find("td", {"day-table-score"}).find("a").text.replace("\r\n", "").replace("\n", "").split(" ")
			score = [i for i in score if i != '']

			n_score = []

			for item in score:
				if len(item) == 2 or len(item) == 3:
					n_score.append(item)
				elif len(item) == 5 or len(item) == 6:
					n_score.append(item[:3])
					n_score.append(item[3:])
				elif len(item) == 8:
					n_score.append(item[:3])
					n_score.append(item[3:6])
					n_score.append(item[6:])

			single["score"] = n_score
			
			ret.append(single)

		return ret

if __name__ == "__main__":
	to = Tournament("/en/tournaments/vienna/337/overview")
	re = Results(to)
	print(re)
