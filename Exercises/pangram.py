def pangram (text): 
    """checks whether the word or phrase contains each letter of the alphabet at least once"""
   
    # we remove whitespaces and turn all the characters in lower case
    no_whitespaces = text.replace (" ", "")
    lower_text = no_whitespaces.lower()
        
    # we must remove the punctuation also
    import string
    punct = string.punctuation
    edited_text = list(lower_text)
       
    for symb in punct:
        if symb in edited_text:
            edited_text.remove(symb)

    # we will compare a set of symbols in the provided string
    # with a set of abc letters
    set_text = set(edited_text)
    set_abc = set(string.ascii_lowercase)
    
    print (f"It's {'not' if set_text != set_abc else ''} a pangram!") 
    
pangram ("The quick brown fox jumps over the lazy dog!")