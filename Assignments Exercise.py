#EXERCISE.1
# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print("Even")
else:
 print("Odd")


#EXERCISE.2
 def is_leap_year(year):
    # A leap year is divisible by 4, except for century years, which must
    # also be divisible by 400 to be leap years.

    if year % 4 != 0:
        return False

    if year % 100 == 0 and year % 400 != 0:
        return False

    return True



#EXERCISE.3
# Get input from the user
year= int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print("{} is a leap year.".format(year))
else:
    print("{} is not a leap year.".format(year))

    # Get input from the user
age = int(input("Enter your age: "))

# Check if the user is an adult
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
 

 #EXERCISE4
username="admin"
password="12345"
input_username=input("enter username:")
input_password=input("enter password:")
if  input_username == username and input_password ==password:
   print(f"login successful")
else:
    print(f"login failed")


#EXERCISE.5
def is_positive(num):
  return num > 0
# Get input from the user
num = float(input("Enter a number: "))

# Check if the number is positive
if is_positive(num):
  print("The number {} is positive.".format(num))
elif num == 0:
  print("The number {} is zero.".format(num))
else:
  print("The number {} is negative.".format(num))


  #Exercise 6: 
  # Find and print the maximum of three numbers
# Ask the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum of the three numbers
max_number = max(num1, num2, num3)

# Print the maximum number
print("The maximum number is:",max_number)


#EXERCISE7
def calculate_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"


# Get the student's score from the user.
score = float(input("Enter the student's score: "))

# Calculate the student's grade.
grade = calculate_grade(score)

# Print the student's grade.
print("The student's grade is: {}".format(grade))
  


  #EXERCISE.8
print= int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")


#Exercise.9
if year % 4 != 0:
   print("False")
elif year % 100 == 0:
       print(year % 400 == 0)
else:
       print("True")

year = int(input("Enter a year: "))

if is_leap_year(year):
    print("Leap year.")
else:
    print("Not a leap year.")


#Exercise.10
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 == num2:
  print("These numbers are equal.")
elif num1 > num2:
    print ("num1")
else:
    print(num2)


# Exercise 1
for i in range(1, 11):
    print(i)

    # Exercise 2
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x{i}= {num*i}")

    # Exercise 3
num = int(input("Enter a number: "))
sum_natural = 0
while num > 0:
    sum_natural += num
    num -= 1
print("Sum of natural numbers:",sum_natural)


# Exercise 4
names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    print(name)


# Exercise 5
num = int(input("Enter a number: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print("Factorial:",factorial)


# Exercise 6
terms = int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a+ b


# Exercise 7
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10
print("Reversed number:",reversed_num)


# Exercise 8
string = "Hello, World!"
vowel_count = 0
for char in string:
    if char.lower() in "aeiou":
        vowel_count += 1
print("Number of vowels:", vowel_count)


# Exercise 9
num = input("Enter a number: ")
reversed_num = num[::-1]
if num == reversed_num:
    print("Palindrome!")
else:
    print("Not a palindrome.")



# Exercise 10
sum_squares = 0
for i in range(1, 6):
    sum_squares += i ** 2
print("Sum of squares:",sum_squares)

















































