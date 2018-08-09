class Enemy:


    def __init__(self, attackh, attackl):
        self.attackh = attackh
        self.attackl = attackl

    def getattack(self):
        print(self.attackl)

enamy1 = Enemy(60,70)
enamy1.getattack()

enamy1 = Enemy(40,50)
enamy1.getattack()