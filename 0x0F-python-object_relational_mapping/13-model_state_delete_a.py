#!/usr/bin/python3

'''
Deletes all State objects with 'a' in its name in the database.
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        pword = sys.argv[2]
        db_name = sys.argv[3]
        DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(
            user, pword, db_name
        )
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        session.query(State).filter(State.name.like('%a%')).delete(
            synchronize_session=False
        )
        session.commit()
