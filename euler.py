import math 
def e_cuadratica(n):
    
    a=0
    for i in range(n):
    	a=a+1/math.factorial(i)



    return a

def e_lineal(n):
  
    fact=[1]
    index=1
    while index<n+1:
    	fact.append(fact[index-1]*index)
    	index=index+1

    res=0
    for i in range (len(fact)-1):
    	res=res+1/fact[i]


    return res
