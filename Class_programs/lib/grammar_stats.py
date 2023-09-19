class GrammarStats:
    def __init__(self):
        self.total_texts = 0
        self.total_texts_passed = 0

    def check(self, text):
        self.text = text
        self.total_texts += 1
        pass_or_fail = bool(self.text[0].isupper() == True and self.text[-1] == '.')
        if pass_or_fail == True:
            self.total_texts_passed += 1
        return pass_or_fail
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise

    def percentage_good(self):
        percentage = round((self.total_texts_passed / self.total_texts) * 100, 1)
        return f"The percentage of texts correct is {percentage}%"
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%