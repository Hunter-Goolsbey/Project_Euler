#Project 9


def pythagoreanTrip(limSum):
    
    import math

    limSumUse = limSum+1
    
    found = False
    arr1 = []

    for i in range(1,limSumUse):
        arr1.append(i)
        
        for l in range(i+1,limSumUse-i):
            c = math.sqrt(i**2 + l**2)

            if i + l + c == limSum:
                z = [i,l,c]
                found = True
                
    ##print(z)
                
    q = 1
    
    for i in z:
        q*=i
        
    return(q)


print(pythagoreanTrip(1000))
