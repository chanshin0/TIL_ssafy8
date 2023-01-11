class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
    def bark(self):
        print('왈왈!')
    @classmethod
    def get_status(cls):
        print(f'Birth : {cls.num_of_dogs}, Current : {cls.birth_of_dogs}')
    def __del__(self):
        Doggy.birth_of_dogs -= 1

d1 = Doggy('초코', '푸들')
d2 = Doggy('꽁이', '말티즈')
d3 = Doggy('별이', '시츄')

d1.bark() 
d2.bark() 
d3.bark()

Doggy.get_status()