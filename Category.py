class Category:
    def __init__(self, name, id, recipes):
        self.__name = name
        self.__id = id
        self.__recipes = []


    def printCategories(self):
        print(f"<Category {self.__id}: {self.__name}>")

    def addRecipe(self, recipe):
        self.__recipes.append(recipe)

    def printRecipes(self):
        print(f"{self.__name}: ")
        for pi in self.__recipes:
            pi.printName()
        print("\n")