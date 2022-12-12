from abc import ABC, abstractmethod


class Storage(ABC):
    
    @abstractmethod
    def add(self, name, amount):
        pass
    
    @abstractmethod
    def remove(self, name, amount):
        pass
    
    @abstractmethod
    def get_free_space(self):
        pass
    
    @abstractmethod
    def get_items(self):
        pass
    
    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store:
    items = {}
    capacity = 100
    
    def __init__(self, items, capacity=100):
        self.capacity = capacity
        self.items = items
    
    def add(self, name, amount):
        self.name = name
        self.amount = amount
        if self.amount > 0:
            self.items[self.name] += self.amount
