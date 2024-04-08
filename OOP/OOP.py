from abc import ABC, abstractmethod

import math

# Encapsulation
# attributes and methods encapsulated in the Email class
print("Encapsulation")


class Email:
    def __init__(self, sender, recipient, subject, body):
        self.body = body
        self.subject = subject
        self.recipient = recipient
        self.sender = sender

    def send(self):
        # sending
        pass

    def read_email(self):
        # reading
        pass


# Inheritance
# car has access to its parent class attributes and to it's owm attributes and methods
print("__________________________________")
print("Inheritance")


class Vehicle:
    def __init__(self, make, model):
        self.model = model
        self.make = make

    def print_info(self):
        print(f"Make: {self.make}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, door_qty):
        super().__init__(make, model)
        self.door_qty = door_qty

    @staticmethod
    def move_forward():
        # move forward functionality
        print("Moving forward")


new_car = Car("Audi", "A6", 4)

new_car.print_info()
new_car.move_forward()
print(new_car.door_qty)

# Polymorphism
# The same method is implemented differently for different child classes
print("__________________________________")
print("Polymorphism")


class Shape:
    def calc_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, a, b):
        self.b = b
        self.a = a

    def calc_area(self):
        return self.a * self.b


shapes = [Circle(5), Rectangle(10, 5), Circle(78), Rectangle(33, 21)]

for shape in shapes:
    area = shape.calc_area()
    print(area)

# Abstraction
# The same method is implemented differently for different child classes
print("__________________________________")
print("Abstraction")


class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class CreditCardPayment(Payment):

    def process_payment(self):
        pass


class StripePayment(Payment):

    def process_payment(self):
        pass


class PayPalPayment(Payment):
    def process_payment(self):
        pass
