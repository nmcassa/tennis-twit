from tourn import *

class Matches:
	def __init__(self, tourn: Tournament):
		self.build(tourn)

	def __str__(self):
		return jsonify(self)

	def build(self, tourn: Tournament):
		#get the daily schedule page
		page = get_parsed_page(tourn.url)
		page = page.find("li", {"data-title": "Daily Schedule"}).find("a")

		#add attribute to dict and get page
		self.url = page['href']
		page = get_parsed_page("https://www.atptour.com" + self.url)

		#get rows in page
		matches = page.find("div", {"id": "scoresDailyScheduleContent"})
		matches = matches.findAll("tr")

		self.matches = []

		#get info
		for match in matches:
			single = {}

			##if it finds none it's a header row
			row_filter = match.find("td", {"day-table-round"})
			if row_filter == None:
				continue
			else:
				single["round"] = row_filter.text.replace("\r\n", "")
				single["round"] = single["round"][:len(single["round"])-8]

			#creates a dict to hold each player
			single["player_one"] = {}
			single["player_two"] = {}

			##gets seeds of players and filters out dumb stuff
			seeds = match.findAll("td", {"day-table-seed"})
			try:
				single["player_one"]["seed"] = seeds[0].find("span").text.replace("\r\n", "")[21:]
				single["player_one"]["seed"] = single["player_one"]["seed"][:len(single["player_one"]["seed"])-17]
			except:
				single["player_one"]["seed"] = "NS"
			try:
				single["player_two"]["seed"] = seeds[1].find("span").text.replace("\r\n", "")[21:]
				single["player_two"]["seed"] = single["player_two"]["seed"][:len(single["player_two"]["seed"])-17]
			except:
				single["player_two"]["seed"] = "NS"

			names = match.findAll("td", {"day-table-name"})

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
			
			self.matches.append(single)

if __name__ == "__main__":
	to = Tournament("/en/tournaments/vienna/337/overview")
	ma = Matches(to)
	print(ma)

