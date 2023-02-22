from typing import Callable, Tuple
from sqlalchemy.orm import sessionmaker

from lab1.atm.app.State import State


class CommandHandler:
    '''
    Accepts flags and callback function, it will be called when the expected flag is detected
    @param expected_flags: tuple of length 2
    @param handler: callback function

    Callback function:\\
    function signature - Callable[[State, Session, str], None]\\
    During calling in the application, application provides it with a State, a sessionmaker and arg.\\
    State - stores the state of the application between launches.\\
    sessionmaker - allows to get a session to communicate with the db.\\
    arg - if a value was passed with the argument, it will be there.\\
    '''
    def __init__(self, expected_flags: Tuple[str, str], handler: Callable[[State, sessionmaker, str], None]) -> None:
        self._expected_flags = expected_flags
        self._handler = handler

    def get_expected_flags(self) -> Tuple[str, str]:
        return self._expected_flags

    def is_expecting(self, arg: str) -> bool:
        '''
        Checking, if handler expecting flag
        @param arg: flag
        '''
        short, long = self._expected_flags
        short = '-' + short.replace(':', '')
        long = '--' + long.replace('=', '')
        return arg in (short, long)

    def handle(self, state: State, sessionmaker: sessionmaker, arg: str):
        '''
        Calling the callback function
        '''
        self._handler(state, sessionmaker, arg)
