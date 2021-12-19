from bs4 import BeautifulSoup
import requests

URL = "https://www.nfl.com/teams/las-vegas-raiders/roster"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="main-content")

player_list = results.find_all("tr")
i=0
for players in player_list:
    print(players)
    playerAttributes = players.find_all("td")
    try:
        status = str(playerAttributes[3])[4:-5]
        if status != "RSR" and status != "RES" and status != "ACT":
            # Only counting players on the active roster or that are in the reserves
            # All other players are skipped
            continue
        i += 1
    except:
        # Any player that we want to use would have a status, so anything lacking status is not useful.
        continue
    player = str(players.find("a", class_="nfl-o-roster__player-name nfl-o-cta--link"))
    player = player[player.index(">")+1:player.index("</a>")]
    print("LOOK HERE {} {}\n\n".format(status, player))