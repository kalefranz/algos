def average(salaries):
    min = 10**6
    max = 1000
    sum = 0
    for x in salaries:
        if x < min:
            min = x
        if x > max:
            max = x
        sum += x
    sum -= min + max
    return sum / (len(salaries) - 2)

print(average([4000,3000,1000,2000])) 
