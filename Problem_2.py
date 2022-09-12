def P2():
    z=[1,2]
    y=[]
    i = 0
    val=0
    while (val <= 4000000):
        z.append(z[0+i]+z[1+i])
        val = z[i]
        #print(val)
        i+=1
    	
    #print(z)
	
    for q in z:
        if (q%2 == 0 and q <= 4000000):
            y.append(q)

    #print (y)

    hold = 0
    for s in y:
        hold += s
    print('P2: '+ str(hold))
    
    
    
P2()
