# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:25:53 2024

@author: hydro
"""

def aaa(A,B):        
        if A==0:
            return B
        if B==0:
            return A
        
        else:
        
            R=A%B
            return aaa(B, R)
        
    
print(aaa(270,192))




'''
define function take input A,B to gind GCD
check if A or B equal zero if yes we return the other
if not we use the function again using recursion conscept putting the same B but it will be our A and 
and the remain will be our B which is will be the remain of A/B

'''