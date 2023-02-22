from __future__ import annotations
from typing import List, Tuple, Callable

import getopt
import sys


from sqlalchemy.orm import sessionmaker

from lab1.atm.app.CommandHandler import CommandHandler
from lab1.atm.app.State import State


class Application:

    _handlers: List[CommandHandler] = None
    _root_handler: Callable[[None], None] = None
    _state: State
    _sessionmaker: sessionmaker

    def __init__(self) -> None:
        self._handlers = list()

    def start(self) -> None:
        '''
        Application startup.
        '''
        self._state.args = self._get_user_entered_agruments()

        if not self._state.args:
            if self._root_handler is not None:
                self._root_handler()

        for argument, value in self._state.args:
            for handler in self._handlers:
                if handler.is_expecting(argument):
                    handler.handle(self._state, self._sessionmaker, arg=value)

    def _get_user_entered_agruments(self) -> List[Tuple[str, str]]:
        short_flags, long_flags = self._get_handlers_expected_flags()

        try:
            arguments, values = getopt.getopt(
                sys.argv[1:],
                short_flags,
                long_flags
            )

        except getopt.error as err:
            print(str(err))
            exit()

        return arguments

    def _get_handlers_expected_flags(self) -> Tuple[str, List[str]]:
        short_flags = list()
        long_flags = list()

        for handler in self._handlers:
            short, long = handler.get_expected_flags()
            short_flags.append(short)
            long_flags.append(long)

        # getopt accepts shorts flags as str, long flags as list
        return (''.join(short_flags), long_flags)

    def add_handler(self, handler: CommandHandler):
        '''
        Provides the application with a handler
        '''
        self._handlers.append(handler)

    def add_root_handler(self, root_handler: Callable[[None], None]) -> None:
        '''
        Called if there are no arguments from the user
        '''
        self._root_handler = root_handler

    def _set_state(self, state: State) -> Application:
        self._state = state
        return self

    def _set_sassion_maker(self, sessionmaker: sessionmaker) -> Application:
        self._sessionmaker = sessionmaker
        return self
