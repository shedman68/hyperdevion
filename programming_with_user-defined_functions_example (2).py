def hotel_cost(num_nights):
    price_per_night = 100  # Example price per night
    return num_nights * price_per_night

def plane_cost(departure_city, destination_city):
    # Example flight costs with (departure, destination) as keys
    flight_costs = {
        ('Geneva', 'Istanbul'): 250,
        ('Geneva', 'Cairo'): 350,
        ('Istanbul', 'Geneva'): 250,
        ('Istanbul', 'Cairo'): 200,
        ('Cairo', 'Geneva'): 350,
        ('Cairo', 'Istanbul'): 200
    }
    # Returns cost based on departure and destination cities, 0 if not found
    return flight_costs.get((departure_city, destination_city), 0)

def car_rental(rental_days):
    daily_rental_cost = 40  # Example daily rental cost
    return rental_days * daily_rental_cost

def holiday_cost(num_nights, departure_city, destination_city, rental_days):
    return hotel_cost(num_nights) + plane_cost(departure_city, destination_city) + car_rental(rental_days)


print("Welcome to the Holiday Cost Tracker!")
print("Available cities: Geneva, Istanbul, Cairo")
departure_city = input("Enter your departure city: ")
destination_city = input("Enter your destination city: ")
num_nights = int(input("How many nights will you stay at the hotel? "))
rental_days = int(input("For how many days will you rent a car? "))


total_cost = holiday_cost(num_nights, departure_city, destination_city, rental_days)

print(f"Your total holiday cost is: £{total_cost}")
