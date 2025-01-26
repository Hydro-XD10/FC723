# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 08:30:54 2024

@author: hydro
"""



#================================================================================================================================
def find_the_greatest_common_factor(Num1,Num2):# find the greatest common factor between two numbers   

        # v, checks if the input are 0 and 0 if true will return erorr with message "The GCD between 0 and 0 is mathematically undefined"
        if Num1==0 and Num2==0:
            raise ValueError("The GCD between 0 and 0 is mathematically undefined")
            
        
        if Num1==0:
            return Num2# <, if one of the numbers is zero so the greatest common factor is the other number
        if Num2==0:
            return Num1
        
        else: # <, if non of the numbers is zero
        
            The_remainder=Num1%Num2
            return find_the_greatest_common_factor(Num2,The_remainder)


def find_Least_Common_Multible(Num1,Num2):# function to find the least common multible between two intgers
    if Num1==0 or Num2==0: # if one of the number is zero the result will be not defined
        raise ValueError("The LCM undefined")# show an erorr message
    
    
    numerator= abs(Num1*Num2)# get the absloute value of the multiblication of the two numbers
    result= numerator/find_the_greatest_common_factor(Num1, Num2)# to find the LCM
    return result


#===============================================================================================================================





def test_find_the_greatest_common_factor(): # Test the GCD
    gcd = find_the_greatest_common_factor(0, 3)
    assert gcd == 3, "The greatest common factor should be 3 when one of the inputs is 0"


def test_lcm_function():
    # Test the LCM
    lcm = find_Least_Common_Multible(-6,18)
    assert lcm == 18, "The least common multiple of 18 and -6 should be 18"
