import sqlite3

"""
GOAL 1:
Use fetchone() to get just one movie (any one is fine) and print it as a dict
Use row_factory = sqlite3.Row
Use a simple SELECT id, title FROM movies
Call fetchone()
Print dict(row)
"""

with sqlite3.connect("movies.db") as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM movies")
    row = cursor.fetchone()
    print("(GOAL 1) Printing a single row using fetchone():")
    print(dict(row))

"""
GOAL 2:
Connect to movies.db
Use row_factory = sqlite3.Row
Run a query that selects:
movies.id
movies.title
directors.name as director_name
Use fetchall() to get all rows into a variable
Loop over those rows and print each one as a dict
"""

with sqlite3.connect("movies.db") as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
        SELECT movies.id, movies.title, directors.name AS director_name
        FROM movies
        JOIN directors 
          ON movies.director_id = directors.id
        """)
    rows = cursor.fetchall()
    print("(GOAL 2) Printing rows from memory using fetchall():")
    for row in rows:
        print(dict(row))

"""
GOAL 3:
Use a JOIN to get all movies with director names, but this time iterate directly over the cursor (no fetchall()), printing dicts
Loop: for row in cursor: print(dict(row))
"""

with sqlite3.connect("movies.db") as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
    SELECT movies.id, movies.title, directors.name AS director_name
    FROM movies
    JOIN directors
        ON movies.director_id = directors.id
    """)
    print("(GOAL 3) Looping through each row:")
    for row in cursor:
        print(dict(row))

"""
Reading rows from a database using fetchone, fetchall, and iterating over the cursor

fetchone() – when you expect at most one row or want to step through rows one at a time
Example: get a movie by its unique id, or read the “next” row in a loop.

fetchall() – when you want all remaining rows in memory at once
Example: load all movies to send as one big JSON list, or to sort/filter them in Python.

Iterating over cursor – when you want to stream rows one by one without holding everything in memory
Example: there might be thousands of rows and you want to process/print each row as it comes.
"""

# Using fetchone and fetchall to store database rows into memory

# with sqlite3.connect("movies.db") as conn: # create a connection to the db
#     cursor = conn.cursor() # create db object
#     cursor.execute("SELECT id, title FROM movies") # executes the SQL statement on the db

#     # print("Iterating over cursor results:")
#     # for row in cursor: # iterate over the new table of results, returns all rows if fetched first.
#     #     print(row)

#     print("Using fetchone():")
#     row = cursor.fetchone() # gets one row
#     print(" First row:", row)

#     print("\nUsing fetchall():")
#     remaining_rows = cursor.fetchall() # gets all remaining rows minus the first fetch
#     print(" Remaining rows:", remaining_rows)
    
#     print("\nIterating over cursor after fetchall():")
#     for row in cursor: # will return nothing since all results have been fetched
#         print(" Cursor row:", row)

# Using JOIN with row_factory to return results as dictionary objects

# with sqlite3.connect("movies.db") as conn:
#     conn.row_factory = sqlite3.Row # row_factory allows rowsto be returned as dictionary objects
#     cursor = conn.cursor()

#     cursor.execute("""
#         SELECT
#             movies.id,
#             movies.title,
#             directors.name
#         FROM movies
#         JOIN directors
#           ON movies.director_id = directors.id
#     """)

#     print("Movies with their directors:")
#     for row in cursor:
#         print(dict(row)) # converts the row to a dictionary, allowing use with APIs such as Flask or FastAPI