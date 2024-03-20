# Declare variables
budget = 2000
cities = ["Rome", "Nairobi", "Phnom Penh", "Santiago", "Toronto", "Rotorua"]
cities_daily_cost = [150, 70, 60, 80, 110, 125]
days = input("How many days can you travel? ")
city_to_visit = input("What city would you like to visit? ")
daily_budget = 0
city_daily_cost = 0

# Check if days is a number, and convert it to an integer if it is
if days.isdigit():
    days = int(days)

# Else print an error
else:
    print('error, not a digit')

# Check if budget and days are integers, and if so, calculate the daily budget
if isinstance(budget, int) and isinstance(days, int):
    daily_budget = budget / days


# Else print an error
else:
    print('error, not an int')

# Check if the city_to_visit is in the cities list, and if so,
# get the daily cost for the city
print('city to visit', city_to_visit)
city_index = cities.index(city_to_visit)
print('city to visit index', city_index)

if city_to_visit in cities:
    print('daily cost for city', cities_daily_cost[city_index])
    city_daily_cost = cities_daily_cost[city_index]

# Else set the city_daily_cost to 0 to be used for error checking
# else:
#     city_daily_cost = 0


# Check if the city_daily_cost is greater than 0 and equal to or less than the
# daily budget, and if so, tell the traveler they can afford the vacation
print('city daily cost', city_daily_cost)
print('daily budget', daily_budget)
print()
if city_daily_cost > 0 and daily_budget >= city_daily_cost:
    print("you're good")

# Else if the city_daily_cost is greater than 0 and greater than the daily budget,
# calculate and print out how much more per day the traveler needs
elif city_daily_cost > 0 and daily_budget < city_daily_cost:
    print("can't go")

# Else print an error
else:
    print('got an error')