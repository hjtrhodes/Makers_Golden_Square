def how_many_spaces(string):
    #count the spaces before each alphabetical char then map alphabetical char (key) to spaces(value) in dictionary (counts_before)
    spaces_before = 0
    counts_before = {}
    for char in string:
        if char == ' ':
            spaces_before += 1
        elif char.isalpha():
            counts_before[char] = spaces_before
            spaces_before = 0

    #REVERSE the string then repeat above
    spaces_after = 0
    counts_after = {}
    string_reverse = string[::-1]
    for char in string_reverse:
        if char == ' ':
            spaces_after += 1
        elif char.isalpha():
            counts_after[char] = spaces_after
            spaces_after = 0

    # Use .get() to retrieve the value for the same key in each dict, add the value then append to a new dict with the original key but the added value
    # Return the letter with the highest value in the final dict
    final_values_dict = {}
    for key in counts_before:
        final_value = counts_before.get(key) + counts_after.get(key)
        final_values_dict[key] = final_value
    return max(final_values_dict, key= lambda x: final_values_dict[x])

print(how_many_spaces(' abc       d     e f  g          z            '))