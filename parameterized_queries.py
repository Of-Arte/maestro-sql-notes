import sqlite3

title = input("Movie title: ")
year = int(input("Release year: "))

conn = sqlite3.connect("movies.db")
cur = conn.cursor()

# Looking up a row safely

sql = "SELECT * FROM movies WHERE title = ? AND year = ?"
cur.execute(sql, (title, year))   # 2 placeholders, 2 values (in order)

rows = cur.fetchall()

print("Results:")
for row in rows:
    print(row)

conn.close()

# Inserting a new row safely

# sql = "INSERT INTO movies (title, year, rating, director_id) VALUES (?, ?, ?, ?)"
# cur.execute(sql, ("New Movie", 2025, 7.5, 1))
# conn.commit()   # makes the change permanent

# conn.close()

# Updating an existing row safely

# sql = "UPDATE movies SET rating = ? WHERE title = ?"
# cur.execute(sql, (9.0, "New Movie"))  # 1st ? → rating, 2nd ? → title

# conn.commit()
# conn.close()

# Deleting a row safely

# sql = "DELETE FROM movies WHERE id = ?"
# cur.execute(sql, (9,))

# conn.commit()
# conn.close()