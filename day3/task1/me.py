same_items = []
item_priorities = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)} # lowercase letter prioriries mapping
item_priorities.update({chr(i): i - ord('A') + 27 for i in range(ord('A'), ord('Z') + 1)}) # add uppercase letters mapping
with open('input.txt') as f:
    for l in f:
        rucksack = l.strip()
        compartment_size = len(rucksack) // 2
        left = rucksack[:compartment_size]
        right = rucksack[compartment_size:]
        common_items = set(left).intersection(set(right))
        same_items += list(common_items)

score = 0
for item in same_items:
    score += item_priorities[item]
print(score)