class Fishing(MiniGame):
    def play(self):
        print(f"You have {self.length} tries to catch fish.\nThe more fish you catch, the more oppertunities you get.")
        clock = self.length
        fish = 0
        
        
        while clock > 0:
            req = random.randint(1,self.difficulty)
            print(f"The fish will come up in {req} seconds")
            x = time.time()
            input("PRESS ENTER TO FISH")
            # Clear Screen
            x = time.time() - x
            
            if int(x) == req:
                fish += 1
                print("Fish caught!")
                if fish % 2 == 0:
                    clock += 1
            
            clock -= 1
        
        # Will update with biomes and such. 
        # Fish types, as well as dud fish, to be added.
        print(f"You got {fish} fish!")
        return fish
            