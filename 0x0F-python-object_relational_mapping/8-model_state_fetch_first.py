#!/usr/bin/python3
"""script that prints the first State object
from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).limit(1)

    if (states.count() == 0):
        print("Nothing")
    else:
        for user in states:
            print(f'{user.id}: {user.name}')

    session.close()
