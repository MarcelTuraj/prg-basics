import json 
file_name = "favourite.json"
favourite_movie = {
    "title":"Forrest Gump",
    "year":1994,
    "Main actor":"Tom Hanks",
    "Director":"Robert Zemeckis",
    "Awarded": True
}

with open(file_name, "w",) as file:
    json.dump(favourite_movie, file, indent=4)
    