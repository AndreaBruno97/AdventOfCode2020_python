''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.readlines()

ingredients = []
allergens = {}

for line_dirty in content:
    ingredients_str, allergens_str = line_dirty.replace("\n", "").split(" (contains ")
    curr_ingredients = ingredients_str.split(" ")
    curr_allergens = allergens_str.replace(")", "").split(", ")

    ingredients = ingredients +  curr_ingredients
    for curr_aller in curr_allergens:
        if not curr_aller in allergens.keys():
            allergens[curr_aller] = set(curr_ingredients)
        else:
            allergens[curr_aller] = set(curr_ingredients).intersection(allergens[curr_aller])

# Once we have the list of possible ingredients for an allergen,
# we filter from the ones that have only one ingredient
while True:
    count_ingr_set = 0
    for aller, ingr_set in allergens.items():
        count_ingr_set += len(ingr_set)
        if len(ingr_set) == 1:
            for inner_aller, inner_ingr_set in allergens.items():
                if not inner_aller == aller:
                    allergens[inner_aller] = inner_ingr_set.difference(ingr_set)

    if count_ingr_set == len(allergens):
        break


ingr_with_allerg = []
for aller in sorted(allergens):
    ingr_with_allerg = ingr_with_allerg + list(allergens[aller])

print("The canonical dangerous ingredient list is " + ",".join(ingr_with_allerg))
