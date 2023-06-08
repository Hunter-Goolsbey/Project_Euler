# Largest prime factor


def P3(number):
    p=2
    n=number
    while n >= p**2:
        if n%p == 0:
            #print(p)
            n = n/p
        else:
            p = p + 1
            
P3(600851475143)
