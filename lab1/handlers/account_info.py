from sqlalchemy.orm import sessionmaker
from lab1.atm.app.State import State

from lab1.templates.messages import NO_CARD, NO_PIN, ACCOUNT_NOT_FOUND

from lab1.atm.db.Models import Card, CardAccount
from tabulate import tabulate


def account_info(state: State, sessionmaker: sessionmaker, arg: str) -> None:

    if not state.card_number:
        print(NO_CARD)
        exit(0)
    elif not state.pincode:
        print(NO_PIN)
        exit(0)

    s = sessionmaker()
    account_data = s.query(CardAccount.number, CardAccount.currency, CardAccount.balance).join(
        Card, Card.account_id == CardAccount.id).filter(Card.number == state.card_number).first()
    s.close()

    if not account_data:
        print(ACCOUNT_NOT_FOUND)
    if account_data:
        print('\nACCOUNT INFO')
        print(tabulate([account_data], headers=[
              'number', 'currency', 'balance'], tablefmt='simple_grid'))
