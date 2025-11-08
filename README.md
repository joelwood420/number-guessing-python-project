# Number Guessing Game

This is a simple number guessing game built using Python, Flask, HTML, CSS, and JavaScript. The objective of the game is to guess a randomly generated number within a certain range.

## Project Structure

```
number-guessing-game
├── src
│   ├── app.py
│   ├── game.py
│   ├── templates
│   │   └── index.html
│   └── static
│       ├── css
│       │   └── style.css
│       └── js
│           └── main.js
├── tests
│   └── test_game.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd number-guessing-game
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python src/app.py
   ```

5. **Access the Game**
   Open your web browser and go to `http://127.0.0.1:5000` to play the game.

## How to Play

1. When the game loads, a random number will be generated.
2. Enter your guess in the input field and submit.
3. The game will provide feedback on whether your guess is too high, too low, or correct.
4. Keep guessing until you find the correct number!

## Testing

To run the tests for the game logic, navigate to the `tests` directory and run:

```bash
python -m unittest test_game.py
```

## License

This project is open-source and available under the MIT License.