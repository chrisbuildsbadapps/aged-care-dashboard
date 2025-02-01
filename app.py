from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '12345'  # Replace with a random key for production

# Dummy credentials for the proof of concept
USERNAME = "clinician"
PASSWORD = "password"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid credentials. Please try again."
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    # Made-up data to display on the dashboard
    data = [
        {"metric": "Occupancy Rate", "value": "85%"},
        {"metric": "Staff On Duty", "value": "12"},
        {"metric": "Incidents Reported", "value": "3"},
    ]
    return render_template('dashboard.html', data=data)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
