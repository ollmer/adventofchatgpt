# Open the file and read in the contents
with open('input.txt') as file:
    data = file.read()

# Split the data by newline characters to create a list of lines
lines = data.split('\n')

# Initialize a list to keep track of the Elves and their calorie counts
elves = []

# Initialize a variable to keep track of the current Elf
current_elf = 1

# Initialize a variable to keep track of the current calorie count for the current Elf
current_calories = 0

# Loop through each line in the list of lines
for line in lines:
    # Check if the line is empty, indicating the end of an Elf's inventory
    if line == '':
        # Add the current Elf and their calorie count to the list of Elves
        elves.append((current_elf, current_calories))
        
        # Reset the current calorie count for the next Elf
        current_calories = 0
        
        # Increment the current Elf
        current_elf += 1
    else:
        # If the line is not empty, it contains the calorie count for a food item.
        # Add the calorie count to the current Elf's total calorie count
        current_calories += int(line)

# Sort the list of Elves by their calorie count in descending order
elves.sort(key=lambda x: x[1], reverse=True)

# Initialize a variable to keep track of the total calorie count for the top three Elves
total_calories = 0

# Loop through the first three Elves in the list
for i in range(3):
    # Get the calorie count for the current Elf
    calories = elves[i][1]
    
    # Add the calorie count to the total calorie count
    total_calories += calories

# Print the answer to the question
print(f'The top three Elves are carrying a total of {total_calories} calories.')
