def rangechecker(x, y , num):
    is_in_range = False
    if num >= x and num <= y:
        is_in_range = True
    else :
        is_in_range = False
    return bool(is_in_range)
