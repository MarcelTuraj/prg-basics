def aritmethic(x,y,sign):
    result = ""
    if sign == "+" :
        result += f"{x}+{y} = {x+y}"
    elif sign == "-" :
        result += f"{x}-{y} = {x-y}"
    elif sign == "**" :
        result += f"{x}**{y} = {x**y}"
    elif sign == "%" :
        result += f"{x}%{y} = {x%y}"
    elif sign == "*" :
        result += f"{x}*{y}={x*y}"
    return result
