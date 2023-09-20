from lib.letter_counter import *

def test_expected_output():
    letter = LetterCounter("Digital Punk")
    result = letter.calculate_most_common()
    assert result == [2, "i"]