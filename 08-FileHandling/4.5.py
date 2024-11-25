import re
with open("email.txt", encoding="utf-8") as file:
    content = file.read()
    contentstring = str(content)


def email_sender(filer):

    # Updated regex pattern to match Return-Path header
    pattern = r"From:\s.*<([^>]+)>"
    array = re.findall(pattern,filer)
    return array

def email_receiver(filer):
    pattern_for_receiver = r"To:\s.*<([^>]+)>"
    array1 = re.findall(pattern_for_receiver,filer)
    return array1

def email_subject(filer):
    pattern2 = r"Subject:\s(.*)\s"
    array2 = re.findall(pattern2,filer)
    return array2

def email_body(filer):
    pattern3 = r"(?s)Hi.+\d"
    array3 = re.findall(pattern3,filer)
    bag = [item.split() for item in array3]
    string_result = ""
    for word in bag:
        for element in word:
            string_result+= f"{element} "
    return string_result

print(email_body(content))
    

