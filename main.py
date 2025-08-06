
from Recipe import Recipe
from Category import Category
weetbix = Recipe("weetbix", "img1", "weetbix, milk, spoon", "the pope", "1901", "6/10", "3, 1, 1", "0.5", "milk > bix > bowl > spoon", "bix", "1", "0", "1", "1", "bix of weet, add soggy", [])
weetbix.printRecipe()

gary = Recipe("gary", "gary.jpg", "water, brainpower, dumb", "Ann And Allen", "2004", "3/10", "10, 1, 1000", "21 years", "run and hide", "non_bix", "2", "Unknown", "1", "1", "gary, add soggy", [])
gary.printRecipe()

bix = Category("bix", "1", [])
bix.printCategories()

bix.add(gary)
print(bix)
