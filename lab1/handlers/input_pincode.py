from sqlalchemy.orm import sessionmaker
from lab1.atm.app.State import State

from lab1.templates.messages import NO_CARD, PIN_ACCEPTED, PIN_NOT_ACCEPTED

from lab1.atm.db.Models import Card


def input_pincode(state: State, sessionmaker: sessionmaker, arg: str) -> None:

    state.pincode = arg

    if not state.card_number:
        print(NO_CARD)
        state.pincode = None
        exit(0)

    s = sessionmaker()
    card = s.query(Card).filter(Card.number == state.card_number).filter(
        Card.pincode == state.pincode).first()
    s.close()

    if not card:
        print(PIN_NOT_ACCEPTED)
        state.pincode = None
    else:
        print(PIN_ACCEPTED)
