opponent_moves = {
    'A': 'r', 'B': 'p', 'C': 's' # r - rock, p - paper, s - scissors
}
your_moves = {
    'X': 'l', 'Y': 'd', 'Z': 'w' # l - loose, d - draw, w - win
}

outcomes = {
    'rl': 0 + 3,
    'rd': 3 + 1,
    'rw': 6 + 2,
    'pl': 0 + 1,
    'pd': 3 + 2,
    'pw': 6 + 3,
    'sl': 0 + 2,
    'sd': 3 + 3,
    'sw': 6 + 1,
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
