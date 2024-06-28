#!/usr/bin/python3
"""
     lists all State objects, and corresponding City objects
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for request in session.query(State).order_by(State.id):
        print(request.id, request.name, sep=": ")
        for namE in request.cities:
            print("    ", end="")
            print(namE.id, namE.name, sep=": ")
