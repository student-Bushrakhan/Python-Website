def find_cheapest_flight(destination, flexibility_days, budget, preferred_airlines):
 

  # Use a travel API or web scraping to search for flights from different airlines and booking platforms.
  # This is a placeholder for the actual flight search logic.
  flight_results = search_flights(destination, flexibility_days, budget, preferred_airlines)

  # Filter out flights that are above the budget.
  filtered_results = [flight for flight in flight_results if flight["price"] <= budget]

  # Sort the filtered results by price, ascending.
  filtered_results.sort(key=lambda flight: flight["price"])

  # Return the top 3 cheapest flight options.
  return filtered_results[:3]

# Example usage
cheapest_flights = find_cheapest_flight(
    destination="Bali",
    flexibility_days=3,
    budget=2000,
    preferred_airlines=["Garuda Indonesia", "Singapore Airlines"]
)

# Print the top 3 cheapest flight options
for flight in cheapest_flights:
  print(f"Airline: {flight['airline']}, Price: ${flight['price']}, Dates: {flight['depart_date']} - {flight['return_date']}")
