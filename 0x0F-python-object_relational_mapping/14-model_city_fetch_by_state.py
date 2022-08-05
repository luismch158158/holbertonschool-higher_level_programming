#!/usr/bin/python3
"""script that lists all State objects from the database
hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State, City.id, City).filter(
        City.state_id == State.id).order_by(City.id).all()

    for data in rows:
        print(f'{data.State.name}: ({data.City.id}) {data.City.name}')

    session.close()
