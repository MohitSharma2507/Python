# Hide internal implementation details and show only essential features to the user:-
# No object can be created of abstract class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,n): 
        self.no_of_tyres=n
    @abstractmethod
    def start(self):
        pass    
    def display(self):
        print("Hi i am calling from vehicle class")
