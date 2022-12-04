# create a dictionary that maps each letter to its corresponding priority
priority_map = {}
for i in range(97, 123):
    priority_map[chr(i)] = i - 96
for i in range(65, 91):
    priority_map[chr(i)] = i - 38

# open the input file
with open("input.txt", "r") as input_file:
    # initialize the total priority to 0
    total_priority = 0

    # loop over the lines in the input file
    for line in input_file:
        # initialize a set to store the items in the first compartment
        first_compartment = set()
        # initialize a set to store the items in the second compartment
        second_compartment = set()

        # loop over the characters in the line
        # and add each character to the appropriate set
        for c in line[:len(line) // 2]:
            first_compartment.add(c)
        for c in line[len(line) // 2:]:
            second_compartment.add(c)

        # find the items that appear in both compartments
        # and add the priorities of these items to the total priority
        for c in first_compartment & second_compartment:
            total_priority += priority_map[c]

    # print the total priority
    print(total_priority)
