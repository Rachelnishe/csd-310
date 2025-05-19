import mysql.connector
from mysql.connector import errorcode

# Connect to the MySQL database
try:
    db = mysql.connector.connect(
        host="localhost",
        user="movies_user",
        password="popcorn",  
        database="movies"  # Ensure this is the correct database name
    )
    print("Database connection successful!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

    if 'db' in locals():
        print("DB variable exists.")
else:
    print("DB variable does not exist.")

# Create a cursor object
cursor = db.cursor()

# Query 1: Select all fields from the studio table
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
print("\n-- DISPLAYING STUDIO RECORDS --")
for studio in studios:
    print(f"Studio ID: {studio[0]}")
    print(f"Studio Name: {studio[1]}")

# Add a blank line for separation
print()  

# Query 2: Select all fields from the genre table
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
print("-- DISPLAYING GENRE RECORDS --")
for genre in genres:
    print(f"Genre ID: {genre[0]}")
    print(f"Genre Name: {genre[1]}")

# Add a blank line for separation
print()  

# Query 3: Select film names with runtime less than two hours
cursor.execute("SELECT film_name, film_runtime FROM movies WHERE film_runtime < 120")  # Include runtime in the query
short_films = cursor.fetchall()
print("-- DISPLAYING SHORT FILM RECORDS --")
for film in short_films:
    print(f"Film Name: {film[0]}")
    print(f"Runtime: {film[1]}")

# Add a blank line for separation
print()  

# Query 4: Get list of film names and directors grouped by director
cursor.execute("SELECT film_director, GROUP_CONCAT(film_name) FROM movies GROUP BY film_director")
directors_films = cursor.fetchall()
print("-- DISPLAYING DIRECTOR RECORDS IN ORDER --")
for director_film in directors_films:
    films_list = director_film[1].split(',')  # Split concatenated film names into a list
    for film in films_list:
        print(f"Film Name: {film.strip()}")  # Strip any leading/trailing whitespace
        print(f"Director: {director_film[0]}")

# Close the cursor and connection
cursor.close()
db.close()