import random


playerhp = 260
enamyatkh = 60
enamyathkl = 50


while playerhp > 0:
    dmg = random.randrange(enamyathkl, enamyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("enamy attack in ", dmg, "and now plyerhp", playerhp)

    if playerhp > 30:
        continue
    print("player is getting hospital to restore health")
    break
