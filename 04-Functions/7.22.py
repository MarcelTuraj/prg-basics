def checker(password) :
    if len(password) < 6 :
        return False
    for char in password :
        container = password.count(char)
        if container > 1 :
            return False
    return True

password = "abcdefgg"
print(f"{checker(password)}")