# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 23:24:28 2024

@author: hydro
"""


def find_the_greatest_common_factor(Num1,Num2):# find the greatest common factor between two numbers   
        if Num1==0:
            return Num2# if one of the numbers is zero so the freatest common factor is the other number
        if Num2==0:
            return Num1
        
        else: # if non of the numbers is zero
        
            The_remainder=Num1%Num2
            return find_the_greatest_common_factor(Num2,The_remainder)# get the remain and Num2/the remain and this will contune until the remain is zero
        
    
print(find_the_greatest_common_factor(270, 192))
