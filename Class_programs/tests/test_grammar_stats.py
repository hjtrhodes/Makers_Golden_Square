from lib.grammar_stats import *

class TestGrammarStats():

    def test_no_capital(self):    
        grammar_stat = GrammarStats()
        result = grammar_stat.check("this is a bad sentence.")
        assert result == False

    def test_no_full_stop(self):
        grammar_stat = GrammarStats()
        result = grammar_stat.check("This is a bad sentence")
        assert result == False

    def test_no_capital_no_full_stop(self):
        grammar_stat = GrammarStats()
        result = grammar_stat.check("this is a bad sentence")
        assert result == False

    def test_correct_sentence(self):
        grammar_stat = GrammarStats()
        result = grammar_stat.check("This is a good sentence.")
        assert result == True

    def test_percentage_good(self):
        grammar_stat = GrammarStats()
        grammar_stat.check("this is a bad sentence.")
        grammar_stat.check("this is a bad sentence.")
        grammar_stat.check("this is a bad sentence.")
        grammar_stat.check("this is a bad sentence.")
        grammar_stat.check("this is a bad sentence.")
        grammar_stat.check("this is a bad sentence.")
        grammar_stat.check("this is a bad sentence.")
        grammar_stat.check("This is a good sentence.")
        grammar_stat.check("This is a good sentence.")
        grammar_stat.check("This is a good sentence.")
        result = grammar_stat.percentage_good()
        assert result == "The percentage of texts correct is 30.0%"

    def test_percentage_good_2(self):
        grammar_stat = GrammarStats()
        grammar_stat.check("this is a bad sentence.")
        grammar_stat.check("this is a bad sentence.")
        grammar_stat.check("this is a bad sentence.")
        grammar_stat.check("this is a bad sentence.")
        grammar_stat.check("this is a bad sentence.")
        grammar_stat.check("This is a good sentence.")
        grammar_stat.check("This is a good sentence.")
        result = grammar_stat.percentage_good()
        assert result == "The percentage of texts correct is 28.6%"