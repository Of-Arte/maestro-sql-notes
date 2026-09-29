import sqlite3 

db_path = "movies.db"

with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, year, rating FROM movies;") 
    rows = cursor.fetchall()
    print('Movies in database:')
    print(rows) 