class Recipe:
    def __init__(self, name, images, ingredients, author, date, rating, ingQuantities, prepTime, instructions, category, id, cookTime, recipeYield, servings, descriptions, reviews):
        self.__name = name
        self.__images = images
        self.__ingredients = ingredients
        self.__author = author
        self.__date = date
        self.__rating = rating
        self.__ingQuantities = ingQuantities
        self.__prepTime = prepTime
        self.__instructions = instructions
        self.__category = category
        self.__id = id
        self.__cookTime = cookTime
        self.__recipeYield = recipeYield
        self.__servings = servings
        self.__descriptions = descriptions
        self.__reviews = reviews

# except reviews

    def printRecipe(self):
        print(f"<Recipe {self.__name} with id: {self.__id} was created by {self.__author} on {self.__date}.>\n")

    def printName(self):
        print(self.__name)

    def __repr__(self):
        print(f"{self.__name}: ")