#Project Euler Problem 4

arr1 = []
n = 0

for i in range(999,100, -1):
    for c in range(i,100, -1):
        product = i*c
        if product > n:
            s = str(i*c)
            if s == s[::-1]:
                n = i*c
                print (n)
