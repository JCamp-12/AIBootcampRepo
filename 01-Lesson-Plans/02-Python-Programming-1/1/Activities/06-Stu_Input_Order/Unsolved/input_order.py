# Take input of an item the user wants to purchase
item_to_purchase = input("what are you buying? ")

# Ask how much the item costs and cast it as a number.
# What type of number should it be cast as?
cost_of_item = float(input("how much does this item cost? "))

# Ask what quantity of the item should be purchased and cast it as a number.
# What type of number should it be cast as?
quantity_of_item = int(input("quantity of item? "))

# Print the item cost along with its data type
print("float ", cost_of_item)

# Print the item quantity along with its data type
print("int", quantity_of_item)

# Print results
total_cost = cost_of_item * quantity_of_item
print(f"the cost of the {item_to_purchase} is {total_cost}")