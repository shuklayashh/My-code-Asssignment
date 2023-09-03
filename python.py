# Define a function to calculate the area of a square
def calculate_square_area(side_length):
    return side_length ** 2

# Get the input from the user
side_length = float(input("Enter the length of a side of the square: "))

# Calculate the area using the function
area = calculate_square_area(side_length)

# Display the result
print(f"The area of the square with side length {side_length} units is {area} square units.")
