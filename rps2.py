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
