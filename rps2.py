# Import modules for random choice and system exit functionality
import random, sys

# Print game title
print('ROCK, PAPER, SCISSORS')

# Initialize score counters
wins = 0    # Tracks number of player wins
losses = 0  # Tracks number of player losses
ties = 0    # Tracks number of tied games



# Main game loop (runs continuously until player quits)
while True:
    # Display current scoreboard using string formatting
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    
    # Player input validation loop
    while True:
        # Display move options
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        # Get player input
        player_move = input('>')
        
        # Quit game if player enters 'q'
        if player_move == 'q':
            sys.exit() # Terminate program immediately
            
        # Check if input is valid (r, p, or s)
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break # Exit input loop if valid
            
        # Show error message for invalid input
        print('Type one of r, p, s, or q.')
    
    # Display player's move
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Generate computer's move (random integer 1-3)
    move_number = random.randint(1, 3)
    # Convert number to move and display
    if move_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif move_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif move_number == 3:
        computer_move = 's'
        print('SCISSORS')

    # Determine game outcome
    # Tie condition
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1 # Increment tie counter
    # Win conditions
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1 # Increment win counter
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    # Lose conditions
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1 # Increment loss counter
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1
