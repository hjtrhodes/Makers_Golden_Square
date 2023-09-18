import pytest
from lib.present import *

def test_present_wrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.wrap('contents')
        present.wrap(None)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."


def test_present_unwrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
