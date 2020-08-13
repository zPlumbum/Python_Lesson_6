class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed_animal(self):
        print(f'Вы покормили животное по имени "{self.name}"!')
        return


class Cow(Animal):
    animal_type = 'Корова'

    def milk(self):
        print(f'{self.animal_type} "{self.name}" подоена!')
        return

    def voice(self):
        print('Mooooo!')


class Goose(Animal):
    animal_type = 'Гусь'

    def collect_eggs(self):
        print('Яйца собраны!')
        return

    def voice(self):
        print('Ga-ga-ga!')


class Sheep(Animal):
    animal_type = 'Овца'

    def cut(self):
        print('Овца подстрижена!')
        return

    def voice(self):
        print('Beeeeee!')


class Chicken(Animal):
    animal_type = 'Курица'

    def collect_eggs(self):
        print('Яйца собраны!')
        return

    def voice(self):
        print('Pok-pok-pok!')


class Goat(Animal):
    animal_type = 'Коза'

    def milk(self):
        print(f'{self.animal_type} "{self.name}" подоена!')
        return

    def voice(self):
        print('Meeeeeee!')


class Duck(Animal):
    animal_type = 'Утка'

    def collect_eggs(self):
        print('Яйца собраны!')
        return

    def voice(self):
        print('Quack-quack!')


goose_0 = Goose('Серый', 10)
goose_1 = Goose('Белый', 11)
cow = Cow('Манька', 160)
sheep_0 = Sheep('Барашек', 45)
sheep_1 = Sheep('Кудрявый', 54)
chicken_0 = Chicken('Ко-Ко', 9)
chicken_1 = Chicken('Кукареку', 10)
goat_0 = Goat('Рога', 38)
goat_1 = Goat('Копыта', 44)
duck = Duck('Кряква', 15)

animals = [goose_0, goose_1, goat_0, goat_1, cow, sheep_0, sheep_1, chicken_0, chicken_1, duck]
max_weight = 0
heavy_animal = ''
total_weight = 0

for animal in animals:
    total_weight += animal.weight
    if animal.weight > max_weight:
        max_weight = animal.weight
        heavy_animal = animal

print(f'Общий вес всех животных - {total_weight}кг')
print(f'Самое тяжелое животное - {heavy_animal.animal_type} по кличке "{heavy_animal.name}" при весе {max_weight}кг')
