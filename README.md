# Smart Travel Planner

## Project Overview

**Smart Travel Planner** is a beginner-friendly Python console application designed to help travellers calculate and plan the costs of their trips. The program collects information about the traveller, destination, and various cost details, then performs calculations to provide a comprehensive breakdown of trip expenses.

## Project Purpose

This project demonstrates fundamental Python programming concepts in a practical, real-world scenario. It's designed to be educational and easy to understand for beginners learning Python.

## What the Program Does

The Smart Travel Planner application:
1. **Collects traveller information** - name, destination, number of travellers, and number of days
2. **Gathers cost details** - transportation, hotel, food, and activity costs
3. **Validates all inputs** - ensures data is correct and in the right format
4. **Calculates expenses** - computes various cost breakdowns
5. **Displays a summary** - shows a formatted, easy-to-read trip cost summary

## Features

✓ User-friendly console interface  
✓ Comprehensive input validation  
✓ Separate functions for each calculation  
✓ Clear error messages for invalid input  
✓ Professional formatted output  
✓ Easy to understand and modify  
✓ Built with Python built-in features only  

## Input Details

The program asks the user to provide:

| Input | Type | Constraint |
|-------|------|-----------|
| Traveller Name | String | Cannot be empty |
| Destination | String | Cannot be empty |
| Number of Travellers | Integer | Must be greater than 0 |
| Number of Travel Days | Integer | Must be greater than 0 |
| Transportation Cost per Traveller | Float | Cannot be negative |
| Hotel Cost per Day | Float | Cannot be negative |
| Food Cost per Traveller per Day | Float | Cannot be negative |
| Activity Cost per Traveller | Float | Cannot be negative |

## Calculations Performed

The program calculates the following values:

1. **Total Transportation Cost** = Number of Travellers × Transportation Cost per Traveller
2. **Total Hotel Cost** = Number of Days × Hotel Cost per Day
3. **Total Food Cost** = Number of Travellers × Number of Days × Food Cost per Traveller per Day
4. **Total Activity Cost** = Number of Travellers × Activity Cost per Traveller
5. **Overall Trip Cost** = Total Transportation + Total Hotel + Total Food + Total Activity
6. **Cost Per Traveller** = Overall Trip Cost ÷ Number of Travellers
7. **Average Daily Cost** = Overall Trip Cost ÷ Number of Days

## Python Concepts Demonstrated

The program demonstrates the following Python concepts:

- **Variables** - Storing traveller and cost information
- **Data Types** - Using `str`, `int`, and `float` appropriately
- **User Input** - Using `input()` function to collect data from users
- **Type Conversion** - Converting string inputs to `int` and `float` using `int()` and `float()`
- **Data Structures** - Using a dictionary to organize trip information
- **Functions** - Creating modular, reusable code blocks
- **Function Parameters** - Passing values to functions
- **Return Values** - Getting results back from functions
- **Arithmetic Operations** - Performing calculations with multiplication, division, and addition
- **Input Validation** - Checking data validity before processing
- **Formatted Output** - Using f-strings to display results with proper formatting
- **Loops** - Using `while` loops for input validation
- **Conditionals** - Using `if` statements for validation logic

## How to Run the Program

### Prerequisites
- Python 3.6 or higher installed on your computer

### Steps to Run

1. **Open a terminal or command prompt**
   - On Windows: Press `Win + R`, type `cmd`, and press Enter
   - On macOS/Linux: Open Terminal

2. **Navigate to the project directory**
   ```bash
   cd path/to/smart-travel-planner-using-python
   ```

3. **Run the program**
   ```bash
   python smart_travel_planner.py
   ```

4. **Follow the on-screen prompts** to enter your trip information

## Example Output

Here's what the program output looks like:

```
============================================================
          Welcome to SMART TRAVEL PLANNER
============================================================
This program will help you calculate the total cost of your trip!

Enter traveller name: John Smith
Enter destination: Paris, France
Enter number of travellers: 3
Enter number of travel days: 5

Now, enter the cost details:
Enter transportation cost per traveller: $150
Enter hotel cost per day: $200
Enter food cost per traveller per day: $50
Enter activity cost per traveller: $100

============================================================
               SMART TRAVEL PLANNER - TRIP SUMMARY
============================================================

Traveller Name:              John Smith
Destination:                Paris, France
Number of Travellers:       3
Number of Days:             5

------------------------------------------------------------
COST BREAKDOWN:
------------------------------------------------------------
Total Transportation Cost:  $450.00
Total Hotel Cost:           $1000.00
Total Food Cost:            $750.00
Total Activity Cost:        $300.00

------------------------------------------------------------
SUMMARY:
------------------------------------------------------------
Overall Trip Cost:          $2500.00
Cost Per Traveller:         $833.33
Average Daily Cost:         $500.00

============================================================
```

## Program Functions

### Input Collection Functions
- `get_traveller_name()` - Collects and validates traveller name
- `get_destination()` - Collects and validates destination
- `get_positive_integer(prompt)` - Collects and validates positive integers
- `get_non_negative_float(prompt)` - Collects and validates non-negative floats

### Calculation Functions
- `calculate_total_transportation()` - Calculates transportation expenses
- `calculate_total_hotel()` - Calculates hotel expenses
- `calculate_total_food()` - Calculates food expenses
- `calculate_total_activity()` - Calculates activity expenses
- `calculate_overall_trip_cost()` - Calculates total trip cost
- `calculate_cost_per_traveller()` - Calculates per-person cost
- `calculate_average_daily_cost()` - Calculates daily average cost

### Display Function
- `display_trip_summary(trip_info)` - Displays formatted trip summary

### Main Function
- `main()` - Orchestrates the entire program flow

## Data Structures Used

The program uses a **dictionary** to organize all trip information:

```python
trip_info = {
    'name': traveller_name,
    'destination': destination,
    'num_travellers': number_of_travellers,
    'num_days': number_of_days,
    'total_transportation': calculated_value,
    'total_hotel': calculated_value,
    'total_food': calculated_value,
    'total_activity': calculated_value,
    'overall_trip_cost': calculated_value,
    'cost_per_traveller': calculated_value,
    'average_daily_cost': calculated_value
}
```

This dictionary makes it easy to pass all the information to the display function and organize related data together.

## Input Validation Rules

The program implements the following validation rules:

1. **Names and Destinations** - Cannot be empty or contain only spaces
2. **Number of Travellers** - Must be an integer greater than 0
3. **Number of Days** - Must be an integer greater than 0
4. **All Costs** - Must be numbers (integer or float) and cannot be negative
5. **Type Conversion** - Invalid numeric inputs trigger error messages and re-prompt

When invalid input is detected, the user sees a clear error message and is asked to try again.

## Learning Outcomes

After studying this program, you will understand:
- How to structure a Python program with functions
- How to validate user input properly
- How to perform calculations in separate functions
- How to use dictionaries to organize data
- How to format output for readability
- How to create a complete, working console application

## Future Enhancements (Optional)

Here are some ideas to expand this program (not included in current version):
- Save trip summaries to a file
- Create multiple trip estimates and compare them
- Add currency conversion
- Store frequent destinations and traveller profiles
- Create a graphical user interface (GUI)

## Technical Requirements

- **Language:** Python 3.6+
- **Libraries Used:** Only Python built-in features (no external libraries)
- **Operating System:** Windows, macOS, or Linux
- **Memory:** Minimal (less than 1 MB)
- **Storage:** Less than 50 KB

## Author

Created as a beginner-friendly Python learning project.

## License

This project is free to use and modify for educational purposes.