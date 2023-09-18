from lib.counter import *

def test_the_counter():
    counter = Counter()
    counter.add(3)
    result = counter.report()
    assert result == 'Counted to 3 so far.'