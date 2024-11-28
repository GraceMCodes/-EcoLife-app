import sqlite3

# Create database and connect
conn = sqlite3.connect('eco_life.db')
cursor = conn.cursor()

# Create Users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    carbon_footprint REAL DEFAULT 0)''')

# Create Challenges table
cursor.execute('''CREATE TABLE IF NOT EXISTS challenges (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    description TEXT,
                    points INTEGER)''')

# Create User Challenges table
cursor.execute('''CREATE TABLE IF NOT EXISTS user_challenges (
                    user_id INTEGER,
                    challenge_id INTEGER,
                    completed BOOLEAN,
                    FOREIGN KEY(user_id) REFERENCES users(id),
                    FOREIGN KEY(challenge_id) REFERENCES challenges(id))''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Database created successfully!")
