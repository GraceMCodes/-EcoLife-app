from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Connect to database
def connect_db():
    return sqlite3.connect('eco_life.db')

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return redirect(url_for('dashboard', user_id=user[0]))
        else:
            return "Invalid credentials!"
    
    return render_template('login.html')

# Dashboard route
@app.route('/dashboard/<user_id>')
def dashboard(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT carbon_footprint FROM users WHERE id=?", (user_id,))
    footprint = cursor.fetchone()[0]
    conn.close()
    
    return render_template('dashboard.html', carbon_footprint=footprint)

if __name__ == '__main__':
    app.run(debug=True)
