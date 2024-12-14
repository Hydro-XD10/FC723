
class Math:

    def find_the_greatest_common_factor(Num1,Num2):# find the greatest common factor between two numbers   
            if Num1==0:
                return Num2# if one of the numbers is zero so the greatest common factor is the other number
            if Num2==0:
                return Num1
            
            else: # if non of the numbers is zero
            
                The_remainder=Num1%Num2
                return Math.find_the_greatest_common_factor(Num2,The_remainder)
'''
from line 10 to 13

this will continue until the remainder equal zero so the other number will be the greatest common factor following the euclidean algorithm
'''


result=Math.find_the_greatest_common_factor(22, 2)
        
print(result)