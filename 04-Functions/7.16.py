def function(palindrome) :
    text = palindrome
    if text[::-1] == text :
        return True
    else :
        return False
    
texting = "radarb"
print(f"{function(texting)}")