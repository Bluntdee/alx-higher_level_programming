#!/usr/bin/python3
"""
Module Docs
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def main():
    """
    Function DOC
    """
    db_user = argv[1]
    db_password = argv[2]
    db_db = argv[3]
    db_host = "localhost"

    try:
        engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(db_user,
                        db_password,
                        db_host,
                        db_db),
                pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = Session(engine)
        states = session.query(State).filter(
                State.name.like("%a%")
                ).order_by(State.id).all()
        for state in states:
            print("{}: {}".format(state.id, state.name))
        session.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()

