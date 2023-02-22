import enum 

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.sql import func

class OperationType(enum.Enum):
    withdrawal = 1,
    expenditure = 2,
    receipt = 3

Base = declarative_base()


class Card(Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    number = Column(String)
    pincode = Column(String)
    account_id = Column(Integer, ForeignKey("CardAccount.id"))

    def __repr__(self):
        return f"<Card(number='{self.number}', account_id='{self.account_id}', pincode='{self.pincode}')>"


class CardAccount(Base):
    __tablename__ = 'card_account'
    id = Column(Integer, primary_key=True)
    number = Column(String)
    currency = Column(String)
    balance = Column(Integer)

    def __repr__(self):
        return f"<CardAccount(number='{self.number}', currency='{self.currency}', balance='{self.balance}')>"

class Transfer(Base):
    __tablename__ = 'transfer'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("card_account.id"))
    operation_type = Column(Enum(OperationType))
    operation_name = Column(String)
    completed_at = Column(DateTime, default=func.now())
    amount = Column(Integer)

    def __repr__(self):
        return f"<Transfer(operation_type='{self.operation_type.name}', operation_name='{self.operation_name}', amount='{self.amount}')>"