fills = [508,500,512,499,492,511,503,476,501,509]

def percentage(data, limit):
    def tolerance_pass(limit):
       return lambda x:(abs(500-x)/500)*100>limit
    wronglyfilled = list(filter(tolerance_pass(limit), data))
    return (len(wronglyfilled)/len(data))*100

print(percentage(fills, 2))

