from lib.string_builder import *

def test_string_builder_size():
    string_build = StringBuilder()
    string_build.add("Harry")
    result = string_build.size()
    assert result == 5
    
def test_string_builder_output():
    string_build = StringBuilder()
    string_build.add("Harry")
    result = string_build.output()
    assert result == "Harry"

    