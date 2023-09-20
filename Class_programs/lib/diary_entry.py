# File: lib/diary_entry.py


class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        # Side-effects:
        #   Sets the title and contents properties
        

    def count_words(self):
        return len(self.contents.split(" "))
        # Returns:
        #   An integer representing the number of words in the contents
        

    def reading_time(self, wpm):
        return f"the reading time is {round(self.count_words()/wpm)} minute(s)"
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        

    def reading_chunk(self, wpm, minutes):
        content_list = self.contents.split(" ")
        total_words = wpm*minutes
        if len(content_list) > total_words:
            current_chunk = content_list[0:total_words]
            del content_list[0:total_words]
            return current_chunk, content_list
        else:
            return content_list[:-1]
        
        
diary = DiaryEntry("entry 1","the quick brown dog jumped over the lazy frog the quick brown dog jumped over the lazy frog")  
print(diary.reading_chunk(2, 3)) 
        
        
        # total_words = wpm*minutes
        # rest_of_content = content_list[total_words:-1]
        
        # if len(rest_of_content) > 0:
        #     chunk = rest_of_content[0:total_words]
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # first_word = content_list[0]
        # place = content_list.index(first_word)
        # chunk = self.contents.split(" ")[0:total_words]
        # if place == 0:
        #     list_remains = content_list[first_word: -1]
        #     return chunk
        # else:
        
        
        # index of last word in string that we hand back to user
        
        
        
    

        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
