# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            for char in self.text.lower():
                if char in self.vowels:
                    self.text = self.text.replace(char, "")
            i += 1
        return self.text

# It is removing every SECOND vowel?