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
        if self.get_free_space >= amount:
            self.items[name] += amount
        else:
            return "Нет свободных мест на складе"

    def remove(self, name, amount):
        if self.get_free_space > amount:
            self.items[name] += amount
        else:
            return "Не хватает товара для совершения операции"
    
    def get_free_space(self):
        free_space = 0
        for item in self.items.values():
            free_space += item
        return self.capacity - free_space

    
    
    
            
