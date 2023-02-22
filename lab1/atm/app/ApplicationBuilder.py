from lab1.atm.app.Application import Application
from lab1.atm.app.State import State
from lab1.atm.db.crud import session


class ApplicationBuilder:
    def __init__(self) -> None:
        pass

    @staticmethod
    def build() -> Application:
        '''
        Constructs and returns the application.
        Defines the state and session.
        '''
        return Application()._set_state(State())._set_sassion_maker(session)
