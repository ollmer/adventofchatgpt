elf_calories = []
current_inventory = 0
with open('input.txt') as f:
    for l in f:
        if l == '\n':
            elf_calories.append(current_inventory)
            current_inventory = 0
        else:
            current_inventory += int(l.strip())
elf_calories = sorted(elf_calories)
print('Top 3 elves carries ', sum(elf_calories[-3:]), 'calories')
