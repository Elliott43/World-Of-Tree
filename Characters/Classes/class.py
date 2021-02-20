class Class:
    starting_equipment = []
    def __init__(self, name, description, stat_order):
        self.stats = dict(zip(stat_order, get_stats()))
        self.inventory = []
		
        self.inventory += starting_equipment