
class Math:

    def find_the_greatest_common_factor(Num1,Num2):# find the greatest common factor between two numbers   
            
    
    # v, checks if the input is string if yes will return error with message "The Input Should Be Intger Or Float"
            if isinstance(Num1 , str) or isinstance(Num2, str):
                raise ValueError("The Input Should Be Intger Or Float")
            
            # v, checks if the input are 0 and 0 if true will return erorr with message "The GCD between 0 and 0 is mathematically undefined"
            if Num1==0 and Num2==0:
                raise ValueError("The GCD between 0 and 0 is mathematically undefined")
                
            
            
            
            if Num1==0:
                return Num2# <, if one of the numbers is zero so the greatest common factor is the other number
            if Num2==0:
                return Num1
            
            else: # <, if non of the numbers is zero
            
                The_remainder=Num1%Num2
                return Math.find_the_greatest_common_factor(Num2,The_remainder)
'''
from line 10 to 13

this will continue until the remainder equal zero so the other number will be the greatest common factor following the euclidean algorithm
'''

# v, Running the function
result=Math.find_the_greatest_common_factor(-3, 0)
        
print(result)