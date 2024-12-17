grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

grades_excluded = list(filter(lambda x:x>2, grades))
mean = sum(grades_excluded)/len(grades_excluded)
print(round(mean, 2))