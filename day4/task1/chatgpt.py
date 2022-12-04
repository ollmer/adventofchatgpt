# Read the input from the input.txt file and split it into pairs.
with open('input.txt') as f:
    pairs = [line.strip() for line in f]

# Initialize the count of fully-contained ranges to 0.
count = 0

# For each pair of ranges...
for pair in pairs:
    # Split the pair into two ranges.
    range1, range2 = pair.split(',')

    # Split each range into a start and end value.
    start1, end1 = map(int, range1.split('-'))
    start2, end2 = map(int, range2.split('-'))

    # If one range fully contains the other, increment the count.
    if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
        count += 1

# Print the count of fully-contained ranges.
print(count)
