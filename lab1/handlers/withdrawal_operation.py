from sqlalchemy.orm import sessionmaker
from lab1.atm.app.State import State

from lab1.templates.messages import NO_CARD, NO_PIN, FAILUR, SUCCESS

from lab1.atm.db.Models import Card, CardAccount, Transfer, OperationType


def withdrawal_operation(state: State, sessionmaker: sessionmaker, arg: str) -> None:

    if not state.card_number:
        print(NO_CARD)
        exit(0)
    elif not state.pincode:
        print(NO_PIN)
        exit(0)

    try:
        withdrawal_amount = int(arg)
        if (withdrawal_amount <= 0):
            raise ValueError
    except ValueError:
        print(FAILUR.INVALID_INPUT, arg)
        return

    s = sessionmaker()
    (account_id,) = s.query(Card.account_id).filter(
        Card.number == state.card_number).first()
    (balance,) = s.query(CardAccount.balance).join(
        Card, Card.account_id == CardAccount.id
    ).filter(Card.number == state.card_number).filter(Card.pincode == state.pincode).first()

    if (balance - withdrawal_amount) < 0:
        print(FAILUR.INSUFFICIENT_FOUNDS)
        s.close()
        return
    elif (state.monies - withdrawal_amount) < 0:
        print(FAILUR.INSUFFICIENT_FOUNDS_IN_ATM)
        s.close()
        return

    s.query(CardAccount).filter(CardAccount.id == account_id).update(
        {CardAccount.balance: CardAccount.balance - withdrawal_amount})

    s.add(Transfer(
        account_id=account_id,
        operation_type=OperationType.withdrawal,
        operation_name="Withdrawal of money from the account",
        amount=withdrawal_amount
    ))
    s.commit()
    s.close()

    state.monies -= withdrawal_amount

    print(SUCCESS)
