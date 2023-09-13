def palindrome (text):
    """checks whether the word or frase reads the same way backward and forward"""
    
    no_whitespaces = text.replace (" ", "")
    back_text = no_whitespaces[::-1]
    
    print (f"It's {'not' if back_text != no_whitespaces else ''} a palindrome!") 
    
palindrome ("nurse run")