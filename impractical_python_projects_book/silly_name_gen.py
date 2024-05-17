import random

# Create a list of first and last names
FIRST_NAME = ['Pitambar', 'Tabbu', 'Supriya', 'Jumba', 'Tubalu', 'Quirey', 'Kaley', 'Sherey']
LAST_NAME = ['Prasad', 'Kumar', 'Dullah', 'Kalumba', 'Ghiyampey', 'Sutta', 'Takley', 'Alchi']

def play_game():
    """Function to play the name generation game.""" #DOCSTRINGS helps other and you to understand your code easier
    while True:
        # Generate a random name
        random_fnames = random.choice(FIRST_NAME)
        random_lnames = random.choice(LAST_NAME)
        print(random_fnames + " " + random_lnames)

        # Prompt user to play again or exit
        try_again = input("Press any key to stop or 'n' to exit: \n")
        if try_again.lower() == 'n':
            print("\nThank you for playing 👋")
            break
if __name__ == "__main__":
# Start the game
    play_game()
