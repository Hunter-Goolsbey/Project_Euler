#Problem 6

def sumsqdif(naturalNum):
    arr1 = []
    arr2 = []
    counter = 0

    for i in range(1,naturalNum+1):
        
        arr1.append(i**2)
        arr2.append(i)
        
    sumsq = sum(arr1)
    sqsum = sum(arr2)**2

    print("Difference: " + str(sqsum - sumsq))


sumsqdif(100)
