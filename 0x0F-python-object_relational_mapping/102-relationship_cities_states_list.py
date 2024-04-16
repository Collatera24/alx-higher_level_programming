#!/usr/bin/python3
"""Module that lists all City objects from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Get the command-line args
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(mysql_username, mysql_password, database_name))

    # Create a configured Session class
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Query all city objects and their associated state objects
    cities = session.query(City).join(State).order_by(City.id)

    # Display the results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
