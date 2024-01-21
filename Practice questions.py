# Question NO.01
def monitor_crop(temperature,humidity,rainfall):
   if humidity=="low" and rainfall=="average below":
      return "watering needed"
   else:
      return "Optimal Condition"
temperature=int(input("Enter a temperature:"))
humidity=input("Enter a humidity:")
rainfall=input("Enter a rainfall:")
print(monitor_crop(temperature,humidity,rainfall))


# Question NO.02
def reserve_book(book_tittle,student_status):
   if book_tittle=="book available"and student_status=="regular":
      print("Reserve the book ")
   elif book_tittle=="book available"and student_status=="VIP student":
      print("instant reservation")
   else:
       print("book is not available") 
book_tittle=input("Enter a book tittle:")
student_status=input("Enter a student status:")
print(reserve_book(book_tittle,student_status))

# Question NO.03
def calculate_fare(distance,time):
   basefare=1
   if 8<=time>=10 and 5<=distance>=7:
      fare=basefare*0.2
   else:
      fare=0
   if 10<=time>=5:
      fare=basefare*0.1
      total_fare=(distance*time)
      return total_fare
distance=int(input("Enter a Distance:"))
time=int(input("Enter a time:"))
print(calculate_fare(distance,time))

# Question NO.04
def check_activity_goal(step_taken,goal):
   if step_taken>=goal:
      return "Goal achieved"
   step_needed=goal-step_taken
   return (f"keep going!you need {step_needed}to reach your goal")
step_taken=int(input("Enter a step:"))
goal=(input("Enter a goal:"))
message=(check_activity_goal(step_taken,goal))
print(message)

# Question NO.5
def check_out():
    discount=cart_total*0.05
    pre_discount=cart_total*0.1
    vip_discount=cart_total*0.15
    if membership == "regular":
        final_amount=cart_total-discount
        print(final_amount)
    elif membership == "premium" :
        final_amount=cart_total-pre_discount
        print(final_amount)
    elif membership == "vip":
        final_amount=cart_total-vip_discount
        print(final_amount)
    else:
        print("no discount") 
membership=input("enter a member level:")
cart_total=int(input ("enter a total:"))
check_out(cart_total)
   
# Question No.6
def weather_advice(temperature,precipitation):
   if weather_advice=="hot"and weather_advice=="Sunny":
      return("Wearing sunscreen")
   elif weather_advice=="raining" :
      return("Carrying an umbrella")  
   elif weather_advice=="Cold":
      return("Dressing warmly")
   else:
      return("Enjoy the weather!")
temperature=input("Enter a weather:")
precipitation=input("Enter a precipitation")
print(weather_advice(temperature,precipitation))