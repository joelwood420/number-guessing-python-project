// This file contains JavaScript code to handle user interactions, such as submitting guesses and updating the UI dynamically without refreshing the page.

document.addEventListener('DOMContentLoaded', function() {
    const guessForm = document.getElementById('guess-form');
    const guessInput = document.getElementById('guess-input');
    const messageDisplay = document.getElementById('message');
    const attemptsDisplay = document.getElementById('attempts');
    let attempts = 0;

    guessForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const userGuess = parseInt(guessInput.value);
        attempts++;
        attemptsDisplay.textContent = `Attempts: ${attempts}`;
        checkGuess(userGuess);
        guessInput.value = '';
    });

    function checkGuess(guess) {
        fetch('/check_guess', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ guess: guess }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.correct) {
                messageDisplay.textContent = 'Congratulations! You guessed the number!';
            } else if (data.too_high) {
                messageDisplay.textContent = 'Too high! Try again.';
            } else {
                messageDisplay.textContent = 'Too low! Try again.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});