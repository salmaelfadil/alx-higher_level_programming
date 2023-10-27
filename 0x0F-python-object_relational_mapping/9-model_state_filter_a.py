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
    state_list = []
    state_list = session.query(State).filter(State.name.like('%a%'))
    for state in state_list:
        print(state.id, state.name, sep=": ")
    session.close()
