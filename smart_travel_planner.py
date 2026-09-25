# Smart Travel Planner - A Beginner-Friendly Console Application
# This program helps users calculate the total cost of a trip

def get_traveller_name():
    """Get and return the traveller's name from user input."""
    name = input("Enter traveller name: ").strip()
    while not name:
        print("Error: Name cannot be empty. Please enter a valid name.")
        name = input("Enter traveller name: ").strip()
    return name


def get_destination():
    """Get and return the destination from user input."""
    destination = input("Enter destination: ").strip()
    while not destination:
        print("Error: Destination cannot be empty. Please enter a valid destination.")
        destination = input("Enter destination: ").strip()
    return destination


def get_positive_integer(prompt):
    """Get and validate a positive integer from user input."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: Value must be greater than 0. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid whole number.")


def get_non_negative_float(prompt):
    """Get and validate a non-negative float from user input."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Error: Cost cannot be negative. Please enter a valid cost.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def calculate_total_transportation(num_travellers, cost_per_traveller):
    """
    Calculate total transportation cost.
    
    Parameters:
        num_travellers (int): Number of travellers
        cost_per_traveller (float): Transportation cost per traveller
    
    Returns:
        float: Total transportation cost
    """
    return num_travellers * cost_per_traveller


def calculate_total_hotel(num_days, hotel_cost_per_day):
    """
    Calculate total hotel cost.
    
    Parameters:
        num_days (int): Number of travel days
        hotel_cost_per_day (float): Hotel cost per day
    
    Returns:
        float: Total hotel cost
    """
    return num_days * hotel_cost_per_day


def calculate_total_food(num_travellers, num_days, food_cost_per_traveller_per_day):
    """
    Calculate total food cost.
    
    Parameters:
        num_travellers (int): Number of travellers
        num_days (int): Number of travel days
        food_cost_per_traveller_per_day (float): Food cost per traveller per day
    
    Returns:
        float: Total food cost
    """
    return num_travellers * num_days * food_cost_per_traveller_per_day


def calculate_total_activity(num_travellers, activity_cost_per_traveller):
    """
    Calculate total activity cost.
    
    Parameters:
        num_travellers (int): Number of travellers
        activity_cost_per_traveller (float): Activity cost per traveller
    
    Returns:
        float: Total activity cost
    """
    return num_travellers * activity_cost_per_traveller


def calculate_overall_trip_cost(total_transportation, total_hotel, total_food, total_activity):
    """
    Calculate overall trip cost.
    
    Parameters:
        total_transportation (float): Total transportation cost
        total_hotel (float): Total hotel cost
        total_food (float): Total food cost
        total_activity (float): Total activity cost
    
    Returns:
        float: Overall trip cost
    """
    return total_transportation + total_hotel + total_food + total_activity


def calculate_cost_per_traveller(overall_trip_cost, num_travellers):
    """
    Calculate cost per traveller.
    
    Parameters:
        overall_trip_cost (float): Overall trip cost
        num_travellers (int): Number of travellers
    
    Returns:
        float: Cost per traveller
    """
    return overall_trip_cost / num_travellers


def calculate_average_daily_cost(overall_trip_cost, num_days):
    """
    Calculate average daily cost.
    
    Parameters:
        overall_trip_cost (float): Overall trip cost
        num_days (int): Number of travel days
    
    Returns:
        float: Average daily cost
    """
    return overall_trip_cost / num_days


def display_trip_summary(trip_info):
    """
    Display a formatted travel summary.
    
    Parameters:
        trip_info (dict): Dictionary containing all trip information and costs
    """
    print("\n" + "=" * 60)
    print(" " * 15 + "SMART TRAVEL PLANNER - TRIP SUMMARY")
    print("=" * 60)
    
    print(f"\nTraveller Name:              {trip_info['name']}")
    print(f"Destination:                {trip_info['destination']}")
    print(f"Number of Travellers:       {trip_info['num_travellers']}")
    print(f"Number of Days:             {trip_info['num_days']}")
    
    print("\n" + "-" * 60)
    print("COST BREAKDOWN:")
    print("-" * 60)
    
    print(f"Total Transportation Cost:  ${trip_info['total_transportation']:.2f}")
    print(f"Total Hotel Cost:           ${trip_info['total_hotel']:.2f}")
    print(f"Total Food Cost:            ${trip_info['total_food']:.2f}")
    print(f"Total Activity Cost:        ${trip_info['total_activity']:.2f}")
    
    print("\n" + "-" * 60)
    print("SUMMARY:")
    print("-" * 60)
    
    print(f"Overall Trip Cost:          ${trip_info['overall_trip_cost']:.2f}")
    print(f"Cost Per Traveller:         ${trip_info['cost_per_traveller']:.2f}")
    print(f"Average Daily Cost:         ${trip_info['average_daily_cost']:.2f}")
    
    print("\n" + "=" * 60 + "\n")


def main():
    """Main function to run the Smart Travel Planner application."""
    print("\n" + "=" * 60)
    print(" " * 10 + "Welcome to SMART TRAVEL PLANNER")
    print("=" * 60)
    print("This program will help you calculate the total cost of your trip!\n")
    
    # Collect traveller information
    name = get_traveller_name()
    destination = get_destination()
    num_travellers = get_positive_integer("Enter number of travellers: ")
    num_days = get_positive_integer("Enter number of travel days: ")
    
    # Collect cost information
    print("\nNow, enter the cost details:")
    transportation_cost_per_traveller = get_non_negative_float(
        "Enter transportation cost per traveller: $"
    )
    hotel_cost_per_day = get_non_negative_float(
        "Enter hotel cost per day: $"
    )
    food_cost_per_traveller_per_day = get_non_negative_float(
        "Enter food cost per traveller per day: $"
    )
    activity_cost_per_traveller = get_non_negative_float(
        "Enter activity cost per traveller: $"
    )
    
    # Perform calculations
    total_transportation = calculate_total_transportation(
        num_travellers, 
        transportation_cost_per_traveller
    )
    
    total_hotel = calculate_total_hotel(
        num_days, 
        hotel_cost_per_day
    )
    
    total_food = calculate_total_food(
        num_travellers, 
        num_days, 
        food_cost_per_traveller_per_day
    )
    
    total_activity = calculate_total_activity(
        num_travellers, 
        activity_cost_per_traveller
    )
    
    overall_trip_cost = calculate_overall_trip_cost(
        total_transportation, 
        total_hotel, 
        total_food, 
        total_activity
    )
    
    cost_per_traveller = calculate_cost_per_traveller(
        overall_trip_cost, 
        num_travellers
    )
    
    average_daily_cost = calculate_average_daily_cost(
        overall_trip_cost, 
        num_days
    )
    
    # Create trip information dictionary
    trip_info = {
        'name': name,
        'destination': destination,
        'num_travellers': num_travellers,
        'num_days': num_days,
        'total_transportation': total_transportation,
        'total_hotel': total_hotel,
        'total_food': total_food,
        'total_activity': total_activity,
        'overall_trip_cost': overall_trip_cost,
        'cost_per_traveller': cost_per_traveller,
        'average_daily_cost': average_daily_cost
    }
    
    # Display the trip summary
    display_trip_summary(trip_info)


# Run the program
if __name__ == "__main__":
    main()
