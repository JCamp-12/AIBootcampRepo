# Dictionary full of info

full_info = {
    "name": "test",
    "age": "21",
    "hobbies": ["eat", "sleep", "walk dog"],
    "wake-up": {
        "Monday": "10:00",
        "TuesDay": "9:00",
        "Friday": "11:00"
    }
}
# Print out results stored in the dictionary
print(full_info)

# Use a loop to print out the key-value pairs in the dictionary
print('these are items: ', full_info.items())
for items in full_info.items():
    print('items in a loop ', items)
# Use a loop to print out the keys of the wake-up dictionary
print('these are keys: ', full_info.keys())
for items in full_info.keys():
    print('keys in a loop ', items)
# Use a loop to print out the values of the wake-up dictionary
print('these are values: ', full_info.values())
for items in full_info.values():
    print('values in a loop ', items)
