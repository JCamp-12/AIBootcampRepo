# Create a tuple containing the names of menu sections:
# snacks, meals, drinks, and dessert.

menu_selections = ('snacks', 'meals', 'drinks', 'dessert')
# Print the tuple.
print(menu_selections)

# Create a list of items for one of the menu sections.
snacks = ['taquitos', 'pizza']

# Create a list of prices for each of the menu items in the previous list.
snack_prices = [4,5]

# Ask a user to input a new item and append it to the relevant list.
snacks.append(input("what snack item? "))
print('these are the new snacks', snacks)
# Ask a user to input the price of the new item, referenced using list indexing
# and append it to the relevant list.
snack_prices.append(int(input("what is the price of the chips? ")))
print('these are the prices of the new snacks', snack_prices)
# Print the menu and prices.
# done above
# print('menu ', menu_selections) 

# Ask the user which item to remove from the menu.
# Find the index of the item and save it as a variable.
snack_to_remove = input("what is the item to remove? ")
index_of_snack_to_remove = snacks.index(snack_to_remove)





# Remove the item from the menu list using remove().
print('snacks pre remove', snacks)
print('index of snack to remove', index_of_snack_to_remove)

snacks.remove(snack_to_remove)

# print('snacks post remove', snacks)


# Remove the item from the prices list using pop().
snack_prices.pop(index_of_snack_to_remove)
# print('prices post remove', snack_prices)


# Print the menu and prices again to confirm removal.
print('prices post remove', snack_prices)
print('snacks post remove', snacks)

# Find the most expensive price on the menu.
print(f"Max price: {max(snack_prices)}")

# Find the cheapest price on the menu.
print(f"Max score: {min(snack_prices)}")

# Find the cost if someone bought every item on the menu.
print(f"bought everything price: {sum(snack_prices)}")

# Confirm that the menu and prices lists are the same length.
print('good? ', len(snacks) == len(snack_prices))