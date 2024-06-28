#!/usr/bin/python3
""" list all City objects from database
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for request in session.query(State).order_by(State.id):
        for namE in request.cities:
            print(namE.id, namE.name, sep=": ", end="")
            print(" -> " + request.name)
