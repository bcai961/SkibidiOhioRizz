class Category:
    def __init__(self, name, id, recipes):
        self.__name = name
        self.__id = id
        self.__recipes = recipes


    def printCategories(self):
        print(f"<Category {self.__id}: {self.__name}>")

