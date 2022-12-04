# Read the input from the input.txt file and split it into lines.
with open('input.txt') as f:
    lines = f.read().strip().split('\n')

# Group the lines into groups of three.
groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

# Create a dictionary that maps each letter to its priority.
priorities = {chr(i): i - 96 for i in range(97, 123)}
priorities.update({chr(i): i - 64 + 26 for i in range(65, 91)})

# Initialize the sum of priorities to 0.
sum_of_priorities = 0

# For each group of rucksacks...
for group in groups:
    # Create a set for each rucksack using a list comprehension.
    item_sets = [set(rucksack) for rucksack in group]

    # Find the item types that appear in all three rucksacks.
    common_item_types = item_sets[0].intersection(item_sets[1], item_sets[2])

    # For each common item type...
    for item_type in common_item_types:
        # Add the priority of the item type to the sum of priorities.
        sum_of_priorities += priorities[item_type]

# Print the sum of priorities.
print(sum_of_priorities)
