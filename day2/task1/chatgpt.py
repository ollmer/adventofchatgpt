# Open the file and read in the contents
with open('input.txt') as file:
    data = file.read()

# Split the data by newline characters to create a list of lines
lines = data.split('\n')

# Initialize a dictionary to map hand shapes and outcomes to their scores
scores = {
    'X': 1, # Rock
    'Y': 2, # Paper
    'Z': 3, # Scissors
    ('A', 'X'): 3, # Draw if opponent chose Rock and you chose Rock
    ('A', 'Y'): 6, # Win if opponent chose Rock and you chose Paper
    ('A', 'Z'): 0, # Lose if opponent chose Rock and you chose Scissors
    ('B', 'X'): 0, # Lose if opponent chose Paper and you chose Rock
    ('B', 'Y'): 3, # Draw if opponent chose Paper and you chose Paper
    ('B', 'Z'): 6, # Win if opponent chose Paper and you chose Scissors
    ('C', 'X'): 6, # Win if opponent chose Scissors and you chose Rock
    ('C', 'Y'): 0, # Lose if opponent chose Scissors and you chose Paper
    ('C', 'Z'): 3, # Draw if opponent chose Scissors and you chose Scissors
}

# Initialize a variable to keep track of the total score
total_score = 0

# Loop through each line in the list of lines
for line in lines:
    # Get the opponent's choice and your choice from the line
    opponent_choice, your_choice = line.split()
    
    # Get the score for the outcome of the round using the dictionary
    round_score = scores[(opponent_choice, your_choice)]
    
    # Add the score for the shape that you selected to the round score
    round_score += scores[your_choice]
    
    # Add the round score to the total score
    total_score += round_score

# Print the total score
print(total_score)
