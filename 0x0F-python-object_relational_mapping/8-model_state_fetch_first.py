#!/usr/bin/python3
"""
prints first state object from database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine(
                           'mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True
                           )
    session = Session(engine)
    first_state = session.query(State).first()
    if first_state is None:
        print("Nothing")
    else:
        print(first_state.id, first_state.name, sep=": ")
    session.close()
