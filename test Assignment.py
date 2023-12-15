# GUESSING GAME
import random
num = random.randint(1, 100)
guesses = 0
while guesses < 5:
  guess = int(input("Guess the number between 1 and 100: "))
  guesses += 1
  if guess < num:
    print("Too low.")
  elif guess > num:
    print("Too high.")
  else:
    print("Congratulations! You guessed the number in", guesses, "guesses!")
    break
if guesses == 5:
  print("Game over! You ran out of guesses.")


# QUESTION NO.1
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
if num1 %2 ==1 and num2 %2==1:
 result=(num1*num1)+(num2*num2)
 print(result)
else:
   print("Calculation is not performed")

# Factorial
i=int(input("Enter a number:"))
fac=1
while i>0:
  fac=fac*i
  i=i-1
print("The factorial of",fac)

#Resturant Bill CCALCULATOR
Number_of_people=int(input("Enter a number:"))
Cost_of_each_meal=float(input("Enter a number:"))
Sales_tax_percentage=10
Tip_percentage=5
Total_cost_of_food=(Cost_of_each_meal + Sales_tax_percentage+Tip_percentage)
print(Total_cost_of_food)
Total_Sales_tax=(Total_cost_of_food % Sales_tax_percentage )
print(Total_Sales_tax)
Total_tip_Ammount=(Total_cost_of_food % Tip_percentage)
print(Total_tip_Ammount)
Total_Bill_Ammount_per_Person=(Total_cost_of_food % Number_of_people)
print(Total_Bill_Ammount_per_Person)
  