import mysql.connector
from mysql.connector import Error

def show_films (cursor, title) :
    # method to execute an inner join on all tables,
    #   iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute(
        "SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' "
        "FROM movies "
        "INNER JOIN genre ON movies.genre_id=genre.genre_id "
        "INNER JOIN studio ON movies.studio_id=studio.studio_id"
    )

    # get the results from the cursor object
    films = cursor.fetchall()

    print ("\n -- {} -- ".format (title) )

    # iterate over the film data set and display the results
    for film in films:
        print ("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n". format (film[0], film[1], film[2], film[3] ) )
    
if __name__ == "__main__":
    # Step 1: Connect to the database
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="movies_user",
            password="popcorn",
            database="movies"
        )
    
        if db is not None:
            cursor = db.cursor()

            # Step 2: Display films using the show_films function
            show_films(cursor, "DISPLAYING FILMS")

            # Insert a new film record
            insert_query = """
                INSERT INTO movies (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(
                insert_query,
                ("The Hitchhiker's Guide to the Galaxy", "Garth Jennings", 2, 1, "2005", 109)  # Adjust genre_id, studio_id, runtime as needed
            )
            db.commit()
            print("DISPLAYING FILMS AFTER INSERTION")

            # Update the film Alien to be a Horror film
            update_query = """
                UPDATE movies
                SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
                WHERE film_name = 'Alien'
            """
            cursor.execute(update_query)
            db.commit()
            print("Updated Alien to Horror genre.")

            # Delete the film Gladiator
            delete_query = """
                DELETE FROM movies
                WHERE film_name = 'Gladiator'
            """
            cursor.execute(delete_query)
            db.commit()
            print("Deleted film: Gladiator.")

            # Optionally, display films after deletion
            show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

            # Close the cursor and connection
            cursor.close()
            db.close()
    except mysql.connector.Error as err:
        print("Database connection error:", err)