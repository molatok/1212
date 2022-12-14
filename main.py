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


class Store(Storage):
    
    def __init__(self, items, capacity=100):
        self.capacity = capacity
        self.items = items
    
    def add(self, name, amount):
        if name in self.items.keys():
            if self.get_free_space() >= amount:
                self.items[name] += amount
                print("Товар добавлен")
                return True
            else:
                if isinstance(self, Shop):
                    print("Нет свободных мест в магазине")
                else:
                    print("Нет свободных мест на складе")
                return False
        
        else:
            if self.get_free_space() >= amount:
                print("Товар добавлен")
                self.items[name] = amount
                return True
            else:
                print("Нет свободных мест на складе")
            return False
    
    def remove(self, name, amount):
        if self.get_free_space > amount:
            print("Товаров достаточно!")
            self.items[name] += amount
        else:
            print("Не хватает товара для совершения операции")
        return False
    
    def get_free_space(self):
        free_space = 0
        for item in self.items.values():
            free_space += item
        return int(self.capacity - free_space)
    
    def get_items(self):
        return self.items
    
    def get_unique_items_count(self):
        return len(self.items.keys())
    
    def __str__(self):
        st = '\n'
        for key, value in self.items.items():
            st += f"{key}: {value}\n"
        return st


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)
    
    def add(self, name, amount):
        if self.get_unique_items_count() >= 5:
            "Не можем разметить больше 5 разных товаров"
        else:
            super().add(name, amount)


class Request:
    def __init__(self, user_input):
        user_data = user_input.split(" ")
        action = user_data[0]
        self.capacity = int(user_data[1])
        self.items = user_data[2]
        if action == "Доставить":
            self.__from = user_data[4]
            self.__to = user_data[6]
        elif action == "Забрать":
            self.__from = user_data[4]
            self.__to = None
        elif action == "Привезти":
            self.__from = user_data[4]
            self.__to = None
    
    def move(self):
        if self.__to and self.__from:
            if eval(self.__to).add(self.items, self.capacity):
                eval(self.__from).remove(self.items, self.capacity)
        if self.__to:
            eval(self.__to).add(self.items, self.capacity)
        elif self.__from:
            eval(self.__from).remove(self.items, self.capacity)


store1 = Store(items={"Товар1": 10, "Товар2": 10, "Товар3": 10})
store2 = Store(items={"Товар1": 10, "Товар2": 10, "Товар3": 10})
shop1 = Shop(items={"Товар1": 1, "Товар2": 2, "Товар3": 3})

test = "Доставить 23 телевизор из store1 в shop1"
req = Request(test)
req.move
print(store1)
print(shop1)