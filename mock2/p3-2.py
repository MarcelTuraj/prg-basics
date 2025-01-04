def f(d):
    def average_num(d):
        return sum(value for value in d.values())/len(d.values())
    return len(list(filter(lambda x:x>average_num(d), d.values())))

print(f({"LO231":150,"BA787":20,"NZ15":30}))

