# Object-Oriented Programming (OOP) in Python

## What is OOP?

OOP is a way of organising code around **objects**: bundles of **data** (attributes) and **behaviour** (methods).

- A **class** is a blueprint.
- An **object** (instance) is something built from that blueprint.

```python
class Dog:
    def __init__(self, name):
        self.name = name          # attribute

    def bark(self):               # method
        return f"{self.name} says woof!"

rex = Dog("Rex")                  # object
print(rex.bark())                 # Rex says woof!
```

OOP has **four pillars**: Encapsulation, Abstraction, Inheritance and Polymorphism.

---

## 1. Encapsulation

**Idea:** Keep data and the methods that work on it together, and protect the data from being changed directly or incorrectly.

In Python, a leading underscore (`_`) or double underscore (`__`) signals that an attribute is private.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance      # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        return self.__balance


account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
print(account.get_balance())   # 120

# account.__balance = 1000000  # doesn't change the real balance
```

**Why it matters:** The balance can only be changed through `deposit()` and `withdraw()`, which check the rules first.

---

## 2. Abstraction

**Idea:** Hide the complicated details and expose only what the user needs. You use *what* something does without needing to know *how*.

Python uses abstract base classes (`abc` module) to define a template that child classes must follow.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass                          # no details, just a rule


class Car(Vehicle):
    def start(self):
        return "Car engine started"


my_car = Car()
print(my_car.start())                 # Car engine started

# v = Vehicle()  # Error: can't create an object from an abstract class
```

**Why it matters:** `Vehicle` says every vehicle must have a `start()` method, but leaves the details to each subclass. When you drive a car, you press "start" and don't need to know how the engine works.

---

## 3. Inheritance

**Idea:** A **child class** can reuse the attributes and methods of a **parent class**, and add or change its own. This avoids repeating code.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"


class Dog(Animal):                    # Dog inherits from Animal
    def bark(self):
        return f"{self.name} says woof!"


rex = Dog("Rex")
print(rex.eat())                      # Rex is eating   (inherited)
print(rex.bark())                     # Rex says woof!  (its own)
```

**Why it matters:** `Dog` gets `name` and `eat()` from `Animal` for free, and adds only what's unique to dogs.

---

## 4. Polymorphism

**Idea:** "Many forms". Different classes can have a method with the **same name** but **different behaviour**. You can call it without caring which type of object you have.

```python
class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class Cow:
    def speak(self):
        return "Moo!"


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())

# Woof!
# Meow!
# Moo!
```

**Why it matters:** The same call, `animal.speak()`, does something different depending on the object. You can add new animals later without changing the loop.

---

## Quick Summary

| Pillar | One-line meaning | Key Python feature |
|---|---|---|
| **Encapsulation** | Bundle data with methods and protect it | `__private` attributes, getters/methods |
| **Abstraction** | Hide the details, show only what's needed | `ABC` and `@abstractmethod` |
| **Inheritance** | Child classes reuse a parent's code | `class Child(Parent):` |
| **Polymorphism** | Same method name, different behaviour | Methods with the same name across classes |