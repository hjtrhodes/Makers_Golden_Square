# File: lib/letter_counter.py

class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        for char in self.text.lower():
            if char.isalpha() and char not in counter:
                counter[char] = 1
            elif char.isalpha() == False:
                pass
            else:
                counter[char] = counter[char] + 1
        most_common = max(counter, key= lambda x: counter[x])
        return [counter[most_common], most_common]