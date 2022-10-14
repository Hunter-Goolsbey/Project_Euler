#Problem 5 (NOT EFFECIENT ENOUGH TO BE PRACTICAL)

def smallestMultiple(maxDivisor):
    
    found = False
    i = 1
    
    while found != True:
        i+=1
        if (all(i%n == 0 for n in range(1,maxDivisor+1))):
            print(i)
            break
        

smallestMultiple(20)
