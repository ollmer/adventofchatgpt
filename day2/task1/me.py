outcomes = {
    'rr': 1 + 3,
    'rp': 2 + 6,
    'rs': 3 + 0,
    'pr': 1 + 0,
    'pp': 2 + 3,
    'ps': 3 + 6,
    'sr': 1 + 6,
    'sp': 2 + 0,
    'ss': 3 + 3,
}
opponent_moves = {
    'A': 'r', 'B': 'p', 'C': 's'
}
your_moves = {
    'X': 'r', 'Y': 'p', 'Z': 's'
}
score = 0
with open('input.txt') as f:
    for l in f:
        opponent_code, your_code = l.strip().split(' ')
        op_move = opponent_moves[opponent_code]
        your_move = your_moves[your_code]
        outcome = outcomes[op_move+your_move]
        score += outcome
print('Final score given strategy is', score)
