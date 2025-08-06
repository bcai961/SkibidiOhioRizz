class Recipe:
    def __init__(self, id, name, author, description, ingredientList, prepInstructions, cookingTime, category, other):
        self.__id = id
        self.__name = name
        self.__author = author
        self.__description = description
        self.__ingredientList = ingredientList
        self.__preparationInstructions = prepInstructions
        self.__cookTime = cookingTime
        self.__category = category
        self.__other = other

    def printRecipe(self):
        print(f"<Recipe {self.__name} with id: {self.__id} was created by {self.__author} on a date.")

