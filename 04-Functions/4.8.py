

def time_string(hours,minutes,time_format) :
    answer = ""
    if time_format == "24" :
        hours = int(hours)
        minutes = int(minutes)
        answer = f"{hours}:{minutes}"
        if hours < 10 and minutes < 10 :
            answer = f"0{hours}:0{minutes}"
        elif hours < 10 and minutes > 10 :
            answer = f"0{hours}:{minutes}"
        elif hours > 10 and minutes < 10 :
            answer = f"{hours}:0{minutes}"
        elif hours > 10 and minutes > 10 :
            answer = f"{hours}:{minutes}"
    if time_format == "12" :
        hours = int(hours)
        if hours >= 0 and hours < 12 :
            answer = f"{hours}:{minutes}am"
        if hours == 12 :
            answer = f"12:{minutes} pm"
        if hours > 12 and hours <= 24 :
            answer = f"{hours - 12}:{minutes} pm"
    return answer

give_hours = input("Input hours : ")
give_minutes = input("Enter minutes")
give_format = input("Enter format")
print(time_string(give_hours, give_minutes, give_format))