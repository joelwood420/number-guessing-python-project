// This file contains JavaScript code to handle user interactions, such as submitting guesses and updating the UI dynamically without refreshing the page.

// Wait for the DOM to be fully loaded before executing any code
// This ensures all HTML elements are available for manipulation
document.addEventListener('DOMContentLoaded', function() {
    // Get references to key HTML elements that we'll interact with
    const guessForm = document.getElementById('guess-form');        // The form for submitting guesses
    const guessInput = document.getElementById('guess-input');      // Input field where user types their guess
    const messageDisplay = document.getElementById('message');      // Element to display feedback messages
    const attemptsDisplay = document.getElementById('attempts');    // Element to show attempt count
    
    // Initialize attempt counter on the client side
    // Initialize attempt counter on the client side
    let attempts = 0;

    // Add event listener to handle form submission
    guessForm.addEventListener('submit', function(event) {
        // Prevent the default form submission behavior (which would refresh the page)
        event.preventDefault();
        
        // Extract the user's guess from the input field and convert to integer
        const userGuess = parseInt(guessInput.value);
        
        // Increment the attempt counter and update the display
        attempts++;
        attemptsDisplay.textContent = `Attempts: ${attempts}`;
        
        // Call the function to check the guess against the server
        checkGuess(userGuess);
        
        // Clear the input field after submission for better UX
        // Clear the input field after submission for better UX
        guessInput.value = '';
    });

    // Function to send the user's guess to the server and handle the response
    function checkGuess(guess) {
        // Make an asynchronous HTTP POST request to the server's /check_guess endpoint
        fetch('/check_guess', {
            method: 'POST',                           // HTTP method for sending data
            headers: {
                'Content-Type': 'application/json',   // Tell server we're sending JSON data
            },
            body: JSON.stringify({ guess: guess }),   // Convert guess to JSON string format
        })
        // Handle the server's response
        .then(response => response.json())            // Parse the JSON response from server
        .then(data => {
            // Check the response data and update the UI accordingly
            if (data.correct) {
                // User guessed correctly - show success message
                messageDisplay.textContent = 'Congratulations! You guessed the number!';
            } else if (data.too_high) {
                // User's guess was too high - give hint to go lower
                messageDisplay.textContent = 'Too high! Try again.';
            } else {
                // User's guess was too low - give hint to go higher
                messageDisplay.textContent = 'Too low! Try again.';
            }
        })
        // Handle any errors that occur during the fetch operation
        .catch(error => {
            // Log error to browser console for debugging purposes
            console.error('Error:', error);
        });
    }
});