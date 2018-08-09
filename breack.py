import random


playerhelthh = 260
enemyatkh = 70
enemayatkl = 60


while playerhelthh > 0:
    dmg = random.randrange(enemayatkl, enemyatkh)
    playerhelthh = playerhelthh - dmg

    if playerhelthh <= 30:
        playerhelthh = 30


    print("enamy strick for", dmg, "point of damage. current hp", playerhelthh)

    if playerhelthh == 30:
        print("player is getting hospital to restore health")
        break
