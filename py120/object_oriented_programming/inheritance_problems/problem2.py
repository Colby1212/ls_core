'''
Let's create a few more methods for out dog class

class Dog:
    def speak(self):
        pass

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

    def fetch(self):
        return 'fethcing!'

create a new class called Cat, which can do everything a dog can except fetch. Assume the methods do the exact same thing.


class Animal:
    def speak(self):
        pass

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'


class Dog(Animal):
    def speak(self):
        return 'barking!'

    def fetch(self):
        return 'fetching!'

class Cat(Animal):
    def speak(self):
        return 'meowing!'