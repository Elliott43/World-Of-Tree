class Party:
	def __init__(self, *characters):
		self.members = self.characters
	
	def add(self, *characters):
		self.members += self.characters
	
	def lose(self, name):
		x = 0
		for i in self.members:
			if name == i.name:
				pop = x
			
			x += 1
		
		self.members.pop(pop)
	
	def get_inits(self):
		inits = []
		for i in members:
			inits.append({i.get_init() : i})
		
		return inits