elf_calories = []
current_inventory_calories = 0
with open('input.txt') as f:
    for l in f:
        if l == '\n':
            elf_calories.append(current_inventory_calories)
            current_inventory_calories = 0
        else:
            current_inventory_calories += int(l.strip())

print(max(elf_calories))
