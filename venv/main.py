from bs4 import BeautifulSoup
import requests

URL = "https://www.raiders.com/team/players-roster/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="main-content")

player_elements = results.find_all("tr")
i=0
j=0
for player_element in player_elements:
    player = player_element.find("td", class_="sorter-custom-height")
    if player == None:
        j += 1
    print(player, end="\n"*2)
    i +=1
print(i)
print(j)

