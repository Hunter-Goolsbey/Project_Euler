#Problem 16

power = 1000
base = 2
digSum = base**power
s = 0

for i in str(digSum):
    s += int(i)

print (s)
