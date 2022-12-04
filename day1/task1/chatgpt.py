# Open the file and read in the contents
with open('input.txt') as file:
    data = file.read()

# Split the data by newline characters to create a list of lines
lines = data.split('\n')

# Initialize variables to keep track of the Elf with the most calories and their calorie count
max_calories = 0
max_elf = 0

# Initialize a variable to keep track of the current Elf
current_elf = 1

# Initialize a variable to keep track of the current calorie count for the current Elf
current_calories = 0

# Loop through each line in the list of lines
for line in lines:
    # Check if the line is empty, indicating the end of an Elf's inventory
    if line == '':
        # Check if the current Elf's calorie count is greater than the maximum calorie count
        if current_calories > max_calories:
            # If it is, update the maximum calorie count and the Elf with the maximum calorie count
            max_calories = current_calories
            max_elf = current_elf
        
        # Reset the current calorie count for the next Elf
        current_calories = 0
        
        # Increment the current Elf
        current_elf += 1
    else:
        # If the line is not empty, it contains the calorie count for a food item.
        # Add the calorie count to the current Elf's total calorie count
        current_calories += int(line)

# Print the answer to the question
print(f'Elf {max_elf} is carrying the most calories with a total of {max_calories} calories.')
