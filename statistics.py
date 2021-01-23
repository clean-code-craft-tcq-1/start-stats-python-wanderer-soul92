import math

def calculateStats(number):
    global n
    n= len(number)
    if n <1:
        calculateStats.a = math.nan
        calculateStats.b = math.nan
        calculateStats.c = math.nan

    else:
        calculateStats.a = float(sum(number)/len(number))
        calculateStats.b = min(number)
        calculateStats.c = max(number)
 
    return {"avg": calculateStats.a, "min": calculateStats.b , "max": calculateStats.c}
