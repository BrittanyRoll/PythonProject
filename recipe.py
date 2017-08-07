ingredients = ["cake flour", "vanilla instant pudding mix", "baking powder", "baking soda", "kosher salt", "eggs", "vanilla extract", "milk", "butter", "sugar", "lavender extract", "purple food coloring", "vegetable oil cooking spray"]
dict = {'cake flour' : '2 1/2 cup',
    'vanilla instant pudding mix' : '8 tablespoons',
    'baking powder' : '1 tablespoon',
    'baking soda' : '1/4 teaspoon',
    'kosher salt' : '1/2 teaspoon',
    'eggs' : '5',
    'vanilla extract' : '2 teaspoons',
    'milk' : '1 cup',
    'butter' : '3/4 cup',
    'sugar' : '1 1/2 cups',
    'lavender extract' : '25 drops',
    'purple food coloring' : '3 drops',
    'vegetable oil cooking spray' : '1 spray'}

intstructions = ["Preheat the oven to 300 degrees F. Prepare a cupcake pan with 24 cupcake liners.", "Combine the flour, pudding mix, baking powder, baking soda, and salt in a medium bowl. Crack the eggs into a second bowl and add vanilla extract. Measure the milk and half-and-half into a third bowl.", "In a 5-quart mixer with the paddle attachment, cream the butter until fluffy. Add sugar.", "Add the eggs 1 at a time.", "Add the dry ingredients, alternating with the wet.", "Mix the batter until smooth and no lumps are present. Add the extracts and food coloring gel. Mix well using a spatula until all the color is incorporated completely.", "Fill the cupcake liners using a 2-ounce scoop. Spray the cupcake pan with the cooking spray this is done after the liners are filled. Bake until golden brown and fluffy, 17 minutes."]

user_input = input()



def recipe() :
    print ("The ingredients are:")
    print (ingredients)
    print("dict['cake flour']: ", dict['cake flour'])
    print(intstructions)

def ingredients() :
    print("The ingredients are:")
    for item in dict.items():
        print(item)
    print(intstructions)

def search():
    if user_input ==

ingredients()
