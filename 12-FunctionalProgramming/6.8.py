grades = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
        return lambda pts:pts>=limit

get_grades = list(filter(min_pts(70), grades))
print(get_grades)
get_grades = list(filter(min_pts(40), grades))
print(get_grades)
get_grades = list(filter(min_pts(30),  grades))
print(get_grades)



    
