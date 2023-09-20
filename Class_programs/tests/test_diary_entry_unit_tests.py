from lib.diary_entry import DiaryEntry

"""given contents of diary entry, returns word count of content"""

def test_count_words():
    diary = DiaryEntry("entry1","the quick brown dog jumped over the lazy dog!")
    result = diary.count_words()
    assert result == 9
    
"""given wpm, return content divided by wpm as an integer"""

def test_reading_time():
    diary = DiaryEntry("entry1","the quick brown dog jumped over the lazy dog!")
    result = diary.reading_time(3)
    assert result == "the reading time is 3 minute(s)"
    
"""given wpm and minutes return a string of contents that the user could read in (minutes)"""
"""if called again, should call the next chunk that could be read, skipping what has been read, until contents are read"""
"""after that, call should restart"""

def test_reading_chunk():
    diary = DiaryEntry("entry 1","the quick brown dog jumped over the lazy frog")
    result = diary.reading_chunk(3,2)
    assert result == "the quick brown dog jumped over"
    
"""testing reading chunk with multiple iterations"""

def test_iterate_reading_chunk():
    diary = DiaryEntry("entry 1","the quick brown dog jumped over the lazy frog")
    diary.reading_chunk(3,2)
    result = diary.reading_chunk(3,2)
    assert result == "the lazy frog"


