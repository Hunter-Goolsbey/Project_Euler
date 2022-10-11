#Problem 6

arr1 = []
arr2 = []
counter = 0

for i in range(1,101):
    
    arr1.append(i**2)
    arr2.append(i)
    
sumsq = sum(arr1)
sqsum = sum(arr2)**2

##print(sumsq)
##print(sqsum)

print("Difference: " + str(sqsum - sumsq))
