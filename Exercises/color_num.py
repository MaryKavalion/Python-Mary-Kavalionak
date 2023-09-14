text = "29535123p48723487597645723645"

import string
from colorama import Back, Style

for start in range (len (text)): 
    end = start+1    
    while end < len(text): 
        if (text[start] or text[end]) not in string.digits:
            break
        if text [start] == text [end]:
            print(f"\n{text[:start]}{Back.GREEN}{text [start:end+1]}{Style.RESET_ALL}{text[end:]}")
            break
        end += 1