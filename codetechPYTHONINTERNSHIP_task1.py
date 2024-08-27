print('''
OPERATORS      
+ ADD
- SUBSTRACT
* MULTIPLY
/ DIVIDE
sq SQUARE 
sqrt SQUARE ROOT 
cu  CUBE 
curt CUBE ROOT  
pert PERCENTAGE
rem  REMAINDER
''')
num1= int(input("enter the value of first number, Divident,Base,obtained number for percent  "))
num2= int(input("enter the value of second number, Divisor,power,total number for percent  "))
opr = (input("enter the operator "))
if opr == "+":
    print(num1+num2)
elif opr == "-" :
    print(num1-num2)
elif opr == "*":
    print(num1*num2)
elif opr == "/":
    print(num1/num2)  
elif opr == "sq":
    print(num1*num1)
elif opr =="sqrt":
    print(num**(1/2)) 
elif opr == "cu":
    print(num1**3)
elif opr == "curt" :
    print(num1**(1/3)) 
elif opr == "pert":
    print(num1*100/num2)
elif opr == "rem":
    print(num1%num2) 
else:
    print("invalid syntex")
           


     


