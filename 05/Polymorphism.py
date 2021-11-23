from abc import abstractmethod
from typing import Optional


class Animal(object):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplemented

    @abstractmethod
    def voice(self):
        raise NotImplemented


class Cat(Animal):
    @property
    def name(self) -> str:
        return 'cat'

    def voice(self):
        print('Meow!')


class Dog(Animal):
    @property
    def name(self) -> str:
        return 'dog'

    def voice(self):
        print('Woof!')


class Cow(Animal):
    @property
    def name(self) -> str:
        return 'cow'

    def voice(self):
        print('Moo!')


class AnimalFactory(object):
    def __init__(self):
        self._animals = [Cat(), Dog(), Cow()]

    def get_animal(self, name: str) -> Optional[Animal]:
        for animal in self._animals:
            if animal.name is name:
                return animal
        else:
            return None


if __name__ == '__main__':
    factory = AnimalFactory()

    animal: Animal = factory.get_animal('cow')
    print(animal.name)
    animal.voice()
