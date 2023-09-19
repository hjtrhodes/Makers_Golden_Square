def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), key=lambda item: item[1])[0][1]
    return letter

"""The function was as above, we used print( statements to discover that the variable
'letter' above) was returning the final number in the final entry in a sorted list
The list had been sorting alphabetically by key so had no relevance to returning the key
with the highest value. We changed letter to the below""" 

def get_most_common_letter(text):
#Returns the letter which appears most in the string
    counter = {}
    for char in text:
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1
        letter = max(counter, key=counter.get)
    return letter

print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")