# Logical Question

#Question No. 1
Num=int(input("Enter a number :"))
if Num>=0:
    print("The number is Positive ")
elif Num<=0:
    print("The Number is Negative ")
else:
    print("The Number is zero ")

#Question No.2
age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

#Question No.3
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("The larger number is:", num1)
elif num1 < num2:
    print("The larger number is:", num2)
else:
    print("Both numbers are equal.")

#Question No. 4
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
 
#Question No. 5
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

maximum = max(num1, num2, num3)
minimum = min(num1, num2, num3)

print("Maximum number:", maximum)
print("Minimum number:", minimum)

#Question No. 6
score = float(input("Enter your exam score: "))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Your grade is:",grade)

#Simple Practical Problem     

#Question No.1
def calculate_total_cost(unit_price, quantity):
    total_cost = unit_price * quantity
    if total_cost > 1000:
        total_cost =unit_price*0.9  # Apply 10% discount
    return total_cost

unit_price = float(input("Enter the unit price: "))
quantity = int(input("Enter the quantity: "))
total_cost = calculate_total_cost(unit_price, quantity)
print("Total cost:",total_cost)

#Question No.2
temperature = float(input("Enter the temperature in Celsius: "))
if temperature < 20:
    print("You should wear a jacket.")
else:
    print("You don't need to wear a jacket.")

#Question No.3
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
 
#Question No.4
pin_code=786
balance=50000

user_pin_code=int(input("enter your pin code:"))
if pin_code==user_pin_code:
    withdraw_amount=int(input("enter a withdraw amount:"))
    if withdraw_amount<=balance:
        new_balance=balance-withdraw_amount
        print("withdraw successfully")
        print("your new bank balance",new_balance)
    else:
        print("insufficient balance ")
else:
    print("invalid user_pin_code")
    
#Question No.5
month = int(input("Enter the month (as a number): "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month == 2:
    print("28 or 29 days")
else:
    print("Invalid month number")

#Question No.6
year = int(input("Enter the year: "))
month = int(input("Enter the month (as a number): "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("29 days (leap year)")
    else:
        print("28 days")
else:
    print("Invalid month number")

# Healthy Lifestyle
    
#Question No.1
# Calorie Counter 

age=int(input("enter a age:"))
weight=float(input("enter a weight:"))
activity=input("enter a activity level:")
pre_KG_calories=12
activity_high=1.80
activity_low=0.55
activity_moderate=1.65
calories=weight * pre_KG_calories
if activity=="high":
     calories_goal=calories * activity_high
     print("calories goal;",calories_goal)    
elif activity=="low":
     calories_goal=calories * activity_low
     print("calories goal;",calories_goal)
elif activity =="moderate":
     calories_goal=calories * activity_moderate
     print("calories goal;",calories_goal)
else:
     print("activity level is incorrect")

#Question No.2
# Sleep Tracker 
user_badtime=int(input("enter a badtime :(under a 24 hours)"))
user_wakeuptime=int(input("enter a wakeup time:(under a 24 hours )"))
total_sleep=user_badtime-user_wakeuptime
print("total sleep time:",total_sleep)
if total_sleep>=7:
    print("good sleep!")
else:
    print("need more sleep!")
   
#Question No.3
# Hydration Helper
weight=float(input("enter a weight:"))
desired_level=input("enter a hydration level:")
if desired_level=="light":
     daily_hyderation=weight*0.04
     print("daily water need:",daily_hyderation)
elif desired_level=="moderate":
     daily_hyderation=weight*0.12
     print("daily water need:",daily_hyderation)
elif desired_level=="intense exercise":
     daily_hyderation=weight*0.06
     print("daily water need:",daily_hyderation)
else:
     print("desired level is invalid")



# Time Manegement 

