"""
Module 09: Object-Oriented Programming (OOP) in Python
=====================================================

This module provides a comprehensive reference for OOP principles in Python:
1. Classes, Objects, and Constructors (`__init__`)
2. Instance Attributes vs Class Attributes
3. Instance Methods, `@classmethod`, and `@staticmethod`
4. Inheritance (Single, Multilevel, Multiple) & `super()`
5. Encapsulation & Name Mangling (`__private_attr`)
6. Abstraction via Abstract Base Classes (`abc.ABC`, `@abstractmethod`)
7. Dunder / Magic Methods (`__str__`, `__add__`)
8. Properties (`@property`)
"""

from abc import ABC, abstractmethod

# ==============================================================================
# 1. CLASSES, CONSTRUCTORS, & METHOD TYPES
# ==============================================================================

class ProductFactory:
    factory_name = "Global Manufacturing Co."  # Class attribute

    def __init__(self, material: str, zips: int, pockets: int):
        self.material = material  # Instance attribute
        self.zips = zips
        self.pockets = pockets

    def show_specs(self) -> str:
        """Instance method operating on instance state."""
        return f"Specs -> Material: {self.material}, Zips: {self.zips}, Pockets: {self.pockets}"

    @classmethod
    def get_factory_info(cls) -> str:
        """Class method bound to the class state."""
        return f"Factory Name: {cls.factory_name}"

    @staticmethod
    def calculate_shipping_cost(weight_kg: float) -> float:
        """Static method independent of class or instance state."""
        return weight_kg * 5.0


# ==============================================================================
# 2. INHERITANCE & POLYMORPHISM
# ==============================================================================

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def speak(self) -> str:
        return f"{self.name} makes a general sound."

    def __str__(self) -> str:
        """Dunder method for readable string representation."""
        return f"Animal(name='{self.name}', age={self.age})"

    def __add__(self, other) -> int:
        """Dunder method overloading '+' to add ages of animals."""
        if isinstance(other, Animal):
            return self.age + other.age
        elif isinstance(other, (tuple, list)):
            return self.age + sum(item.age for item in other if isinstance(item, Animal))
        return self.age


class Human(Animal):
    def __init__(self, name: str, age: int, occupation: str):
        super().__init__(name, age)  # Call parent constructor
        self.occupation = occupation

    def speak(self) -> str:
        """Method overriding."""
        return f"Hello, my name is {self.name} and I am a {self.occupation}."


# Multiple Inheritance Example
class Walker:
    def walk(self) -> str:
        return "Walking on land."

class Swimmer:
    def swim(self) -> str:
        return "Swimming in water."

class AmphibianRobot(Walker, Swimmer):
    def __init__(self, model_name: str):
        self.model_name = model_name


# ==============================================================================
# 3. ENCAPSULATION & PRIVATE ATTRIBUTES
# ==============================================================================

class EncapsulatedVault:
    def __init__(self, secret_code: str):
        self.__secret_code = secret_code  # Private attribute (Name mangled)

    def reveal_secret(self, passkey: str) -> str:
        if passkey == "admin123":
            return f"Secret Code: {self.__secret_code}"
        return "Access Denied!"


# ==============================================================================
# 4. ABSTRACTION (Abstract Base Classes)
# ==============================================================================

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side


# ==============================================================================
# 5. PROPERTY DECORATORS (@property)
# ==============================================================================

class Circle(Shape):
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def radius(self) -> float:
        """Getter for radius property."""
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """Setter for radius property with validation."""
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    def area(self) -> float:
        import math
        return math.pi * (self._radius ** 2)

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self._radius


if __name__ == "__main__":
    print("--- 1. Class Instance & Static Methods ---")
    bag = ProductFactory("Leather", 3, 2)
    print(bag.show_specs())
    print(ProductFactory.get_factory_info())
    print(f"Shipping Cost (3kg): ${ProductFactory.calculate_shipping_cost(3.0)}")

    print("\n--- 2. Inheritance & Dunder Methods ---")
    lion = Animal("Lion", 12)
    person = Human("Nischal", 23, "Developer")
    print(str(lion))
    print(person.speak())
    print(f"Sum of ages (Lion + Person): {lion + person}")

    print("\n--- 3. Multiple Inheritance ---")
    robot = AmphibianRobot("HydroBot-V1")
    print(f"{robot.model_name}: {robot.walk()} | {robot.swim()}")

    print("\n--- 4. Abstraction & Property Decorator ---")
    sq = Square(4)
    print(f"Square(4) Area: {sq.area()} | Perimeter: {sq.perimeter()}")

    circ = Circle(7)
    print(f"Circle Radius property: {circ.radius}")
    print(f"Circle(7) Area: {circ.area():.2f}")
