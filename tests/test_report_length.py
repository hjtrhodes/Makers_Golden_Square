from lib.report_length import *

def test_report_length():
    result = report_length('Harry')
    assert result == "This string was length 5 characters long"