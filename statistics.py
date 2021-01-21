
  
  #import math

def calculateStats(number):
    n = len(number)
    if n < 1:
        calculateStats.a = None
        #Sort=number.sort()
        calculateStats.b = None
        calculateStats.c = None
    else :
        calculateStats.a = float(sum(number)/len(number))
        #Sort=number.sort()
        calculateStats.b = min(number)
        calculateStats.c = max(number)
 
    return {"avg": calculateStats.a, "min": calculateStats.b , "max": calculateStats.c}
