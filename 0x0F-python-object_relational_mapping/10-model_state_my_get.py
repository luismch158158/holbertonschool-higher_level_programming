#!/usr/bin/python3
"""script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    from sys import argv
    import re

    if (len(argv) != 5):
        print("You must be use mysql username, mysql password,\
               database name and state name searched")
        exit(1)

    argument = ''.join(argv[4].split())

    if (re.search('^[a-zA-Z]+$', argument) is None):
        print('Please enter a valid name State')
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
        State.name.like(argument))

    if (states.count() == 0):
        print("Not found")
    else:
        for state in states:
            print(f'{state.id}')

    session.close()
