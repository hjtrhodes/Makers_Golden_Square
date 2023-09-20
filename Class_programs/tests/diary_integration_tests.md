"""
Given (Argument)
It returns (Output)
"""
extract_uppercase("Input") => ["Output"]





diary.py
Add function adds to entries list

All function returns a list of instances for diary entry

Count words - int counting all words in all diary entries (connected to count words in diary_entry)

Reading_time - returns an integer representing reading time in minutes if the reader were to read ALL entries in a day

Best entry for reading time: returns An instance of DiaryEntry representing the entry that is closest to, but not over, the length that the user could read in the minutes they have available given their reading speed. 





diary_entry.py
count_words - An integer representing the number of words in the contents

reading_time -  An integer representing an estimate of the reading time in minutes for the contents at the given wpm.

reading_chunk
A string representing a chunk of the contents that the user could
read in the given number of minutes.
If called again, `reading_chunk` should return the next chunk,
skipping what has already been read, until the contents is fully read.
The next call after that it should restart from the beginning.


Take a chunk


create a new list without the original chunk

repeat until the list has no more contents

go back to the original list and start again



123



456



789






