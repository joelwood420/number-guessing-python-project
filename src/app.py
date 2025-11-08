from flask import Flask, render_template, request, session, redirect, url_for
import random
from game import generate_random_number, check_guess

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    if 'number_to_guess' not in session:
        session['number_to_guess'] = generate_random_number()
        session['attempts'] = 0
    # pop any one-time message set by other routes (like /restart)
    message = session.pop('message', None)
    return render_template('index.html', message=message)


@app.route('/guess', methods=['POST'])
def guess():
    # get guess safely
    try:
        user_guess = int(request.form.get('guess', '').strip())
    except (ValueError, TypeError):
        message = "Please enter a valid integer."
        return render_template('index.html', message=message)

    session['attempts'] += 1
    secret = session['number_to_guess']

    # use your helper
    result = check_guess(user_guess, secret)



    if result.startswith("Congratulations"):
        # build a message that includes attempts, then reset the game
        message = f"Congratulations! You've guessed the number {secret} in {session['attempts']} attempts."
        session.pop('number_to_guess', None)
        session.pop('attempts', None)
    else:
        message = result

    return render_template('index.html', message=message)

# add restart route here so it's registered before the app runs
@app.route('/restart', methods=['POST'])
def restart():
    # remove old state so index() creates a fresh game
    session.pop('number_to_guess', None)
    session.pop('attempts', None)
    # set a one-time message that index() will show after redirect
    session['message'] = "Game restarted. Good luck!"
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)