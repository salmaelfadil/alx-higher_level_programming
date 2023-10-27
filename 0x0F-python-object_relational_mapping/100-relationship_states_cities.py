#!/usr/bin/python3
"""
creates State “California” with the City “San Francisco” from
the database hbtn_0e_100_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True
                          )
    session = Session(engine)

    new_state = State(name='California')
    new_city.cities = [City(name='San Francisco')]
    session.add(new_state)
    session.commit()
    session.close()