class Character:
    def __init__(self, name, race, klass, inventory=[]):
        self.name = name
        self.race = race
        self.klass = klass
        self.inventory = inventory
	
        def get_init(self):
            return ((self.klass.stats["dexterity"]-10) / 2) + random.randint(1,20)
	
        def __dict__(self):
            full = dir(self)
			save = {}
			for i in save:
				if not "__" in i:
					saved_value = getattr(self, i)
					
					if "__main__" in type(saved_value):
						saved_value = saved_value.__dict__()
					
					save[i] = saved_value
			
			return save
			
		def __str__(self):
			return cstring(self.__dict__())
		
		