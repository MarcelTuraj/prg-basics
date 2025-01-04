def f(d):
    data = {}
    result = []
    for item in d:
        if not item[0] in data.keys():
            data[item[0]] = item[1]
        else :
            if item[1] == "out" :
                del data[item[0]]
    for key in data.keys():
        result.append(f"{key}")
    return sorted(result)
print(f([["KR234","in"],["KR234","out"]]))
        