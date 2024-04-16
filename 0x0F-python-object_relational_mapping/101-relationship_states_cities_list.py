#!/usr/bin/python3
"""Module that lists all State objects, and corresponding City objects in the database"""

mport sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)

    # Create a session that interacts with database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and print the states and their cities
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("   {}:  {}".format(city.id, city.name))
