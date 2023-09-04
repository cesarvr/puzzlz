class Character:
    def __init__(self):
        self.life = 0
        self.armor = 0
        self.mana = 0

    def hit(self, damage):
        self.life = self.life - damage

    def is_dead(self):
        return self.life <= 0

