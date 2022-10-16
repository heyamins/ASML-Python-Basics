
class Person:

    __slots__ = '_name', '_residence', '_age', '_profession', '_education', '_cars'

    def __init__(self, name, residence, age = None, profession = 'Unknown'):
        self._name = name
        self._residence = residence
        self._age = age
        self._profession = profession
        self._cars = []
        self._education = 'TU'

    def tell(self):
        print(f'I am {self._name} and I live in {self._residence}.')
        if self._age is None:
            print(f'I am {self._age} years old.')

    def move(self, new_residence):
        self._residence = new_residence
        
    def buy_car(self, car):
        self._cars.append(car)

    def list_cars(self):
        print('I own the following cars:')
        for car in self._cars:
            print(car)

    @property
    def profession(self):
        return self._profession.title()

    @profession.setter
    def profession(self, profession):
        if profession:
            self._profession = profession


#-----------------------------------

# Instantiation / Instance

p1 = Person('Peter', 'Lhee', 65)
p2 = Person('Joost', 'Veldhoven', 38, 'Project manager')

# call methods

p1.tell()
p2.tell()

p1.move('Eindhoven')
p1.tell()

p2.move('Nuenen')
p2.tell()

p1.buy_car('Ferrari')
p1.buy_car('Lotus')

print(p2.profession)
p2.profession = 'Project manager'
print(p2.profession)

p1.list_cars()

