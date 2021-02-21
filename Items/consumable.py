class Consumable(Item):
    def get_effect(self):
        return self.amount, self.stat
