from bs4 import BeautifulSoup
import requests

URL = "https://www.nfl.com/teams/las-vegas-raiders/roster"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="main-content")

player_elements = results.find_all("tr")
i=0
j=0
for player_element in player_elements:
    player = player_element.find("a", class_="nfl-o-roster__player-name nfl-o-cta--link")
    print(player, end="\n"*2)
    i +=1
print(i)
print(j)

