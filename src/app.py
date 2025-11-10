# Import necessary Flask modules for web framework functionality
from flask import Flask, render_template, request, session, redirect, url_for
import random
# Import custom game logic functions from the game module
from game import generate_random_number, check_guess

# Create Flask application instance
app = Flask(__name__)
# Set secret key for session management (used to encrypt session data)
# Set secret key for session management (used to encrypt session data)
app.secret_key = 'your_secret_key'


# Route for the home page (root URL '/')
@app.route('/')
def index():
    # Initialize a new game if no current game exists in the session
    if 'number_to_guess' not in session:
        # Generate a random number for the user to guess
        session['number_to_guess'] = generate_random_number()
        # Initialize attempt counter to track how many guesses the user has made
        session['attempts'] = 0
    # Retrieve and remove any one-time message from the session (like restart notifications)
    message = session.pop('message', None)
    # Render the main game page with any message to display
    return render_template('index.html', message=message)


# Route for handling user guesses (accepts POST requests only)
@app.route('/guess', methods=['POST'])
def guess():
    # Safely extract and validate the user's guess from the form data
    try:
        # Get the 'guess' field from the form, strip whitespace, and convert to integer
        user_guess = int(request.form.get('guess', '').strip())
    except (ValueError, TypeError):
        # If conversion fails (non-numeric input), display error message
        message = "Please enter a valid integer."
        return render_template('index.html', message=message)

    # Increment the attempt counter each time a guess is made
    session['attempts'] += 1
    # Get the secret number that the user is trying to guess
    secret = session['number_to_guess']

    # Use the game logic function to check if guess is correct, too high, or too low
    result = check_guess(user_guess, secret)

    # Check if the player has successfully guessed the number
    if result.startswith("Congratulations"):
        # Create a success message that includes the secret number and attempt count
        message = f"Congratulations! You've guessed the number {secret} in {session['attempts']} attempts."
        # Clear the game state from session to end the current game
        session.pop('number_to_guess', None)
        session.pop('attempts', None)
    else:
        # If guess was wrong, use the feedback message from check_guess function
        # (e.g., "Too high!" or "Too low!")
        message = result

    # Render the game page with the appropriate message
    return render_template('index.html', message=message)

# Route for restarting the game (accepts POST requests only)
# This route is registered before app.run() to ensure proper routing
@app.route('/restart', methods=['POST'])
def restart():
    # Clear all game-related data from the session to start fresh
    session.pop('number_to_guess', None)  # Remove the secret number
    session.pop('attempts', None)         # Reset the attempt counter
    # Set a one-time welcome message that will be displayed after redirect
    # This message will be picked up and removed by the index() function
    session['message'] = "Game restarted. Good luck!"
    # Redirect the user back to the home page to start a new game
    return redirect(url_for('index'))

# Entry point for running the application
# This block only executes if the script is run directly (not imported as a module)
if __name__ == '__main__':
    # Start the Flask development server with debug mode enabled
    app.run(debug=True)