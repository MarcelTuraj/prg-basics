def hider(card_number) :
    string = card_number
    core = string[2:12]
    result = f"**{core}****"
    return str(result)