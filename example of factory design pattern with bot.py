from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProductA(Product):
    def operation(self):
        return "Operation from ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self):
        return "Operation from ConcreteProductB"

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = product.operation()
        return result

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Usage
creator_a = ConcreteCreatorA()
result_a = creator_a.some_operation()
print(result_a)  # Output: Operation from ConcreteProductA

creator_b = ConcreteCreatorB()
result_b = creator_b.some_operation()
print(result_b)  # Output: Operation from ConcreteProductB