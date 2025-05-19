import mysql.connector  # to connect
from mysql.connector import errorcode
import dotenv  # to use .env file
from dotenv import dotenv_values

# Using our .env file
secrets = dotenv_values(".env")

""" Database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True  # not in .env file
}

""" Connection test code """
try:
    """ Try/catch block for handling potential MySQL database errors """ 
    db = mysql.connector.connect(**config)  # Connect to the movies database 
    
    # Output the connection status 
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\nPress any key to continue...")

except mysql.connector.Error as err:
    """ On error code """
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    """ Close the connection to MySQL """
    try:
        db.close()
    except NameError:
        pass  # If db was never created due to an error