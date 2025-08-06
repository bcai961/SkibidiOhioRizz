class Category:
    def __init__(self, name, id, recipes):
        this.__name = name
        this.__id = id
        this.__recipes = recipes


    def printCategories(self):
        print(f"<Category {self.__id}: {self.__name}>")