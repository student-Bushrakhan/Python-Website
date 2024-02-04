# Fitness Tracker
daily_steps = 7500
distance_walked = 5.2  # in km
calories_burned = 350

# Calculate average steps per week
average_steps_per_week = daily_steps * 7
print("Average steps per week:", average_steps_per_week)

# Calculate total distance covered in a month (assuming 30 days)
total_distance_month = distance_walked * 30
print("Total distance covered in a month:", total_distance_month, "km")

# Shopping List
item_names = ["apples", "bread", "milk"]
quantities = [2, 1, 1]
prices = [1.5, 2.5, 3.0]  # in dollars

# Calculate total cost of items
total_cost = sum(price * quantity for price, quantity in zip(prices, quantities))
print("Total cost of items:", total_cost, "dollars")

# Check if budget is enough (assuming budget is $20)
budget = 20
if total_cost <= budget:
    print("Enough budget!")
else:
    print("Not enough budget. Please adjust quantities or prices.")

# Recipe Calculator
recipe_ingredients = {"eggs": 2, "flour": 1.5, "milk": 1, "sugar": 0.5}  # in cups
num_servings = 4

# Calculate adjusted quantities based on servings
adjusted_quantities = {ingredient: quantity * num_servings / 2 for ingredient, quantity in recipe_ingredients.items()}
print("Adjusted recipe quantities for", num_servings, "servings:")
for ingredient, quantity in adjusted_quantities.items():
    print(ingredient, quantity, "cups")

# Movie Recommendation System
movies = [
    {"genre": "comedy", "rating": 8.5, "year": 2023},
    {"genre": "action", "rating": 9.0, "year": 2022},
    {"genre": "drama", "rating": 8.0, "year": 2021},
]

user_genre = "comedy"
min_rating = 8.0

# Recommend movies based on user preferences
recommendations = [movie for movie in movies if movie["genre"] == user_genre and movie["rating"] >= min_rating]
print("Recommended movies:")
for movie in recommendations:
    print(movie["genre"], movie["rating"], movie["year"])

# Time Management Tool
tasks = ["coding", "reading", "exercise"]
durations = [2, 1, 0.5]  # in hours

# Calculate total time spent on each task
total_time_per_task = {task: duration for task, duration in zip(tasks, durations)}
print("Total time spent on each task:")
for task, duration in total_time_per_task.items():
    print(task, duration, "hours")

# Identify areas for improvement (assuming you want to maximize coding time)
max_time_task = max(total_time_per_task.values())
improvement_areas = [task for task, duration in total_time_per_task.items() if duration < max_time_task and task != "coding"]
print("Areas for improvement (to maximize coding time):")
for area in improvement_areas:
    print(area)
