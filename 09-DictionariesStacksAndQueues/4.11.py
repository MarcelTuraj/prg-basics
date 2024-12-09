import json
# Read the contents of the json file
with open("vote.json", encoding="utf-8") as file:
    vote_statement = json.load(file)
    person_name = input('Name of the person you are voting for:')
    if person_name not in vote_statement:
      vote_statement[person_name] = 1
    else :
        vote_statement[person_name] += 1

with open("vote.json", "w", encoding="utf-8") as file:
   json.dump(vote_statement, file)

# Vote for a person



# Save voting data to json file
