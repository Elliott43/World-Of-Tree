class Class:
    starting_equipment = []
    def __init__(self, name, description, stat_order):
        self.stats = dict(zip(stat_order, get_stats()))
        self.inventory = []
		
        self.inventory += starting_equipment

def get_stats():
	stats = []
	for i in range(6):
		stats.append([])
		for j in range(4):
			stats[i].append(random.randint(1, 6))
		
		stats[i].sort()
		stats[i].pop(0)
	
	return stats