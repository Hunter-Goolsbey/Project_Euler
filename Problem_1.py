# Multiples of 3 or 5

def P1(rangeTo):
    l1 = []

    for i in range(0,rangeTo):
        if i%3 == 0:
            l1.append(i)

        elif i%5 ==0:
            l1.append(i)  
    x = 0
    for p in l1:
        x += p
    print(x)
    
P1(1000)
