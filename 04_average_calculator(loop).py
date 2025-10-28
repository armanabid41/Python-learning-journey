# 03_average_calculator.py
# A program to calculate the average of a set of numbers provided by the user.

# Ask the user how many numbers they want to average.
n = int(input("How many numbers do you want to average? "))
# --- Initialization ---
# Create an empty list to store the numbers.
numbers = []
# Initialize a variable to keep the sum of the numbers, starting at 0.
total = 0
# --- The Loop ---
# Loop 'n' times to get each number from the user.
print("\nPlease enter the numbers:")
for i in range(n):
    # Prompt for each number. float() is used to allow for decimal numbers.
    num = float(input(f"Enter number {i+1}: "))
    # Add the entered number to our list.
    numbers.append(num)
    # Add the entered number to the running total.
    total += num
#Calculation & Output 
# Avoid dividing by zero if the user entered 0 for the number of inputs.
if n > 0:
    # Calculate the average by dividing the total sum by the count of numbers.
    average = total / n
    # Print the final result, formatted to show only two decimal places.
    print(f"\nThe list of numbers is: {numbers}")
    print(f"The average is: {average:.2f}")
else:
    print("Cannot calculate the average of zero numbers.")
