from lib.diary import Diary

"""
Initially the list is empty
Returns Empty list
"""
def test_initially_has_no_diary_entries():
    diary = Diary()
    assert diary.all() == []
    
