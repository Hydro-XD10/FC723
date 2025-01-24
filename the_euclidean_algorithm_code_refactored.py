
class Math:
    
#v, take the input of the first number and the second
    def take_input():
        Num1=int(input("Enter the first number "))
        Num2=int(input("Enter the first number "))
        return Num1 , Num2
    
#Menu to choose between finding GCD or LCM
    def menu(): # menu to choose options
        _input=input("If you want to find Greatest Common Divisor enter 1  \nIf you want to find Least Common Multiples enter 2\n ")
        n1,n2=Math.take_input()#take the input and assign it to n1 and n2
        if _input == "1" :#  find the GCD option
            result=Math.find_the_greatest_common_factor(n1,n2)# use the function to find the GCD
            print(f" The Greatest Common Divisor between {n1} and {n2} is {result}")# print the result
            return result # return the result to use it in the LCM function
        if _input == "2":# find the LCM option
            _result=Math.find_Least_Common_Multible(n1, n2) # usingg the function to find the LCM
            print(f"The Least Common Multiple between {n1} and {n2} is {_result}")#print the result
        

    def find_Least_Common_Multible(Num1,Num2):# function to find the least common multible between two intgers
        if Num1==0 or Num2==0: # if one of the number is zero the result will be not defined
            raise ValueError("The LCM undefined")# show an erorr message
        
        
        numerator= abs(Num1*Num2)# get the absloute value of the multiblication of the two numbers
        result= numerator/Math.find_the_greatest_common_factor(Num1, Num2)# to find the LCM
        return result 
    
    
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
                return Math.find_the_greatest_common_factor(Num2,The_remainder)
'''
from line 10 to 13

this will continue until the remainder equal zero so the other number will be the greatest common factor following the euclidean algorithm
'''

Math.menu()
