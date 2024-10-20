###
# Survey
#
quest1 = str(input("Are you interested in computer science? (y/n) "))
quest2 = str(input("Do you like playing computer games? (y/n) "))
quest3 = str(input("Do you have an Instagram account? (y/n) "))
ans1 = "Interested in computer science: "
ans2 = "Playing computer games: "
ans3 = "Has an Instagram account: "

if quest1 == "y" :
    ans1 += "Yes"
else :
    ans1 += "No"

if quest2 == "y" :
    ans2 += "Yes"
else :
    ans2 += "No"

if quest3 == "y" :
    ans3 += "Yes"
else : 
    ans3 += "No"

print(f"""SURVEY RESULTS : {ans1}
                           {ans2}
                           {ans3}""")
    