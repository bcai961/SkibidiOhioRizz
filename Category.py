from Recipe import Recipe

class Category:
    def __init__(self, name, id, recipes):
        self.__name = name
        self.__id = id
        self.__recipes = []

    @property
    def recipe(self):
        return self.__recipes

    @recipe.setter
    def recipe(self, recipe):
        self.__recipes.append(recipe)

    def addRecipe(self, recipe):
        self.__recipes.append(recipe)

    def __repr__(self):
        return(f"Category {self.__name} has the following associated recipes: {self.__recipes} ")

    def __str__(self):
        return(f"Category {self.__name} has the following associated recipes: {self.__recipes} ")