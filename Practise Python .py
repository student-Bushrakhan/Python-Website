# 2 variable print
print("bushra")
print("bushra")

# 2 values sepration
height,weight=339,500
print(height)
print(weight)

#hi+ name
your_name=input("Enter you name:")
print("hi!"  + your_name )
#space
print("bushra  Khan")

#addition
num1=input("Enter the number:")
num2=input("Enter the number:")
print(int(num1)+int(num2))

#substraction
num1=input("Enter the number:")
num2=input("Enter the number:")
print(int(num1)-int(num2))

#multiplication
num1=input("Enter the number:")
num2=input("Enter the number:")
print(int(num1)*int(num2))

#Division
num1=input("Enter the number:")
num2=input("Enter the number:")
print(float(num1)/float(num2))

#percentage
obt_marks=350
total_marks=500
percentage=(obt_marks/total_marks*100)
print(percentage)

#codition true or false
num=int(input("Enter the number:"))
if num>=10:
     print("true")
else:
     print("false")
    
#swapping variable
a=4
b=2
a=a+b#6
b=a-b#4
a=a-b#2
print(a)
print(b)


#Mini Calculator
num1=float(input("Enter your number:"))
num2=float(input("Enter your number:"))
print("press.1 for addition\npress.2 for substraction\npress.3 for multiplication\npress.4 for division ")
choice=int(input("enter your choice 1-4:"))
if choice==1:
     print ("The addition of two numbers is:",num1+num2)
if choice==2:
     print("The substraction of two numbers is:",num1-num2)
if choice==3:
     print("The Multiplication of two numbers is:",num1*num2)
if choice==4:
     print("The division of two numbers is:",num1/num2)

#leap year
year=int(input("Enter a year"))
if (year%400==0) and (year%100==0):
     print (year,"is a leaf year")
elif(year%4==0) and (year% 100 !=0):
     print(year,"is not a leaf year")

#even or odd
num=int(input("Enter a number:"))
if num%2==0:
     print("Even")
else:
     print("odd")

#adult or minior
age=int(input("Enter a age :"))
if age>=18:
    print("Your are adult")
else:
    print("you are minior") 

#login system
username="admin"
Password="12345"
input_username=input("Enter the Username:")
input_Password=input("Enter the Password:")
if input_username ==username and input_Password==Password:
     print(f"Login Successfull")
else:
     print(f"Login failled")


# positive, negative, zero
num=float(input("Enter a number:"))
if num>=0:
    print("The number is Positive")
elif num==0:
    print("The number is Zero")
elif num<=0:
     print("The number is negative")

#maximum Number
num1=float(input("Enter the Number:"))
num2=float(input("Enter the Number:"))
num3=float(input("Enter the Number:"))
maximum_number=max(num1,num2,num3)
print("The maximun number is:",maximum_number)


#Grade
marks=int(input("Enter the marks:"))
if marks>90:
     print("A1")
elif marks>80:
     print("A")
elif marks>70:
     print("B")
elif marks>60:
     print("C")
else:
     print ("F")

print=int(input("Enter the number:"))
if num>1:
     





           


















