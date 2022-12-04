item_priorities = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)} # lowercase letter prioriries mapping
item_priorities.update({chr(i): i - ord('A') + 27 for i in range(ord('A'), ord('Z') + 1)}) # add uppercase letters mapping

rucksacks = []
with open('input.txt') as f:
    for l in f:
        rucksack = l.strip()
        rucksacks.append(rucksack)

same_items = []
for i in range(0, len(rucksacks), 3):
    r1, r2, r3 = rucksacks[i:i+3]
    common_items = set(r1).intersection(set(r2)).intersection(set(r3))
    same_items += list(common_items)

score = 0
for item in same_items:
    score += item_priorities[item]
print(score)