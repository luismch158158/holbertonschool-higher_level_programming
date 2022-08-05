#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the
database hbtn_0e_6_usa"""

from sqlalchemy import create_engine, insert
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_data = State(name='Louisiana')
    session.add(new_data)
    session.commit()

    users = session.query(State).where(State.name == 'Louisiana')

    for user in users:
        print(f'{user.id}')

    session.close()
