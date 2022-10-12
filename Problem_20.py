#Problem 20

arr1 = []
num = 100
x = 0
c = 1

for i in range(1,(num+1)):
    c*=i
for l in str(c):
    x += int(l)
    
print(x)
