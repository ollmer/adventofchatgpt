# create a dictionary that maps the possible combinations of
# the opponent's choice and the outcome of the round
# to the player's choice
choice_map = {
    ('A', 'Z'): 'B',
    ('B', 'Z'): 'C',
    ('C', 'Z'): 'A',
    ('A', 'Y'): 'A',
    ('B', 'Y'): 'B',
    ('C', 'Y'): 'C',
    ('A', 'X'): 'C',
    ('B', 'X'): 'A',
    ('C', 'X'): 'B',
}

# create a dictionary that maps the player's shape
# to the corresponding score
score_map = {
    'A': 1,
    'B': 2,
    'C': 3
}

# create a dictionary that maps the outcome of the round
# to the corresponding score
outcome_map = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

# read the input from the file
with open('input.txt', 'r') as f:
    lines = f.readlines()

# initialize the total score to 0
total_score = 0

# loop over the lines in the input
for line in lines:
    # split the line on whitespace and get the first and second
    # elements from the resulting list, which represent the
    # opponent's choice and the outcome of the round, respectively
    opp_choice, outcome = line.split()

    # determine the player's choice using the choice_map dictionary
    player_choice = choice_map.get((opp_choice, outcome), 'A')

    # use the score_map dictionary to determine the player's score
    player_score = score_map[player_choice]

    # use the outcome_map dictionary to determine the round outcome score
    round_score = outcome_map[outcome]

    # add the player's score and the round outcome score
    # to the total score
    total_score += player_score + round_score

# print the total score
print(total_score)
