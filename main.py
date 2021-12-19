import random
from tkinter import *
from bs4 import BeautifulSoup
import requests

bgColor = "#BEC2CB"

root = Tk()
root.geometry("1920x1080")
root.configure(bg=bgColor)

URL = "https://www.nfl.com/teams/las-vegas-raiders/roster"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="main-content")

all_players = results.find_all("tr")
playerList = []
hiddenStat = ""
for players in all_players:
    playerAttributes = players.find_all("td")
    try:
        status = str(playerAttributes[3])[4:-5]
        if status != "RSR" and status != "RES" and status != "ACT":
            # Only counting players on the active roster or that are in the reserves
            # All other players are skipped
            continue
    except:
        # Any player that we want to use would have a status, so anything lacking status is not useful.
        continue
    playerName = str(players.find("a", class_="nfl-o-roster__player-name nfl-o-cta--link"))
    playerName = playerName[playerName.index(">") + 1:playerName.index("</a>")]
    number = str(playerAttributes[1])
    number = number[number.index(">") + 1:number.index("</td")]
    position = str(playerAttributes[2])
    position = position[position.index(">") + 1:position.index("</td")]
    playerList.append([playerName, position, number, status])
previousPlayer = random.choice(playerList)


def set_screen():
    global gui, text_entry
    text_entry = StringVar()
    text_entry.set("")
    gui = [
        Label(root, text=previousPlayer[0]),
        Label(root, text=previousPlayer[1]),
        Label(root, text=previousPlayer[2]),
        Entry(root, textvariable=text_entry),
        Button(root, command=new_player, text="Check"),
        Button(root, command=reveal_answer, text="Reveal")
    ]

    grid = [
        gui[0].grid(row=0, column=0),
        gui[1].grid(row=0, column=1),
        gui[2].grid(row=0, column=2),
        gui[3].grid(row=1, column=1),
        gui[4].grid(row=2, column=0),
        gui[5].grid(row=2, column=1)
    ]
    new_player()
    for i in range(3):
        gui[i].configure(bg=bgColor)

def new_player():
    global previousPlayer, gui, hiddenStat
    if gui[3].get() == hiddenStat:
        text_entry.set("")
        random_player = random.choice(playerList)
        while random_player == previousPlayer:
            random.choice(playerList)
        previousPlayer = random_player
        hidden_num = random.randint(0, 2)
        hiddenStat = previousPlayer[hidden_num]
        gui[0].config(text=previousPlayer[0])
        gui[1].config(text=previousPlayer[1])
        gui[2].config(text=previousPlayer[2])
        gui[hidden_num].config(text="?")


def reveal_answer():
    text_entry.set(hiddenStat)

root.title("Raiders Roster")
set_screen()

root.mainloop()
