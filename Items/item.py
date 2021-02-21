class Item:
    # If the item does not break/run out of uses, reusable = -1
    # If the item does break/run out of uses, reusable = amount of uses left.
    # If the item is broken/has run out of uses, reusable = 0
    def __init__(self, name, desc, stat, weight, amount=0, reusable=-1):
        self.name = name
        self.desc = desc
        self.stat = stat
        self.amount = amount
        self.reusable = reusable