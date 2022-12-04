# Read the input from the input.txt file and split it into pairs.
with open('input.txt') as f:
    pairs = [line.strip() for line in f]

# Initialize the count of overlapping ranges to 0.
count = 0

# For each pair of ranges...
for pair in pairs:
    # Split the pair into two ranges.
    range1, range2 = pair.split(',')

    # Split each range into a start and end value.
    start1, end1 = map(int, range1.split('-'))
    start2, end2 = map(int, range2.split('-'))

    # If the ranges overlap, increment the count.
    if (start1 <= end2) and (end1 >= start2):
        count += 1

# Print the count of overlapping ranges.
print(count)