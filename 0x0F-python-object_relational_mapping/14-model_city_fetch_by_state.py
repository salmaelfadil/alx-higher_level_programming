#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
                           'mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True
                           )
    session = Session(engine)
    lis = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in lis:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
