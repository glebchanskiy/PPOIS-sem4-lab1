from sqlalchemy.orm import sessionmaker
from lab1.atm.app.State import State

from lab1.templates.messages import NO_CARD, NO_PIN

from lab1.atm.db.Models import Card, CardAccount, Transfer
from tabulate import tabulate


def transfers_info(state: State, sessionmaker: sessionmaker, arg: str) -> None:

    if not state.card_number:
        print(NO_CARD)
        exit(0)
    elif not state.pincode:
        print(NO_PIN)
        exit(0)

    s = sessionmaker()
    transfers = s.query(
        Transfer.completed_at,
        Transfer.operation_name,
        Transfer.operation_type,
        Transfer.amount
    ).join(
        CardAccount, CardAccount.id == Transfer.account_id
    ).join(
        Card, Card.account_id == CardAccount.id
    ).filter(Card.number == state.card_number).all()
    s.close()

    if not transfers:
        print('No transfers found')
    else:
        print('\nTRANSFERS')
        print(tabulate(transfers, headers=[
              'datetime', 'operation', 'type', 'amount'], tablefmt='simple_grid'))
