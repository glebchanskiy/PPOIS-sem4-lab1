from sqlalchemy.orm import sessionmaker
from lab1.atm.app.State import State


def get_card(state: State, sessionmaker: sessionmaker, arg: str) -> None:
    state.card_number = None
    state.pincode = None

    print("GOODBYE")
