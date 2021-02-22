class User:
    def __init__(self, name, password):
        self.number = []
        for i in range(len(password)):
            self.number.append(random.randint(-500000, 500000))

        self.name = name
        self.put_password(password)
        self.characters = []

    def get_password(self):
        ret = ""
        for j, i in zip(self.number, self.password):
            ret += chr( converter( ord(i) - int(j) ) )

        return ret


    def put_password(self, password):
        self.password = ""
        for j, i in zip(self.number, password):
            self.password += chr( converter( ord(i) + int(j) ) )

    def __dict__(self):
        return {
            "name"            :   self.name,
            "number"          :   self.number,
            "password"        :   self.password,
            "characters"      :   [i.__dict__() for i in self.characters()]

        }

    def load(self, data):
        for i in data:
            setattr(self, i, data[i])

        self.characters = [Character(j) for j in self.characters]
        return self

def converter(num : int):
    if num < 0:
        return converter(1114111 + num)
    elif num > 1114111:

        return converter( num - 1114111)
    else:
        return num