text = "29535123p48723487597645723645"

import string
from colorama import Back, Style

for start in range (len (text)): 
    nextind = start+1    
    while nextind < len(text): 
        if text[start] not in string.digits or text[nextind] not in string.digits:
            break
        if text [start] == text [nextind]:
            print(f"\n{text[:start]}{Back.GREEN}{text [start:nextind+1]}{Style.RESET_ALL}{text[nextind:]}")
            break
        nextind += 1