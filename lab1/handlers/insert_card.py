from sqlalchemy.orm import sessionmaker
from lab1.atm.app.State import State

from lab1.templates.messages import CARD_ACCEPTED, CARD_NOT_ACCEPTED

from lab1.atm.db.Models import Card


def insert_card(state: State, sessionmaker: sessionmaker, arg: str) -> None:

    state.card_number = arg
    state.pincode = None

    s = sessionmaker()
    card = s.query(Card).filter_by(number=state.card_number).first()
    s.close()

    if not card:
        print(CARD_NOT_ACCEPTED)
        state.card_number = None
    else:
        print(CARD_ACCEPTED)
     
    