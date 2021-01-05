from abc import ABC, abstractmethod
# abstract base classes (ABC)

class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def comer(self):
        print('Animal come')




