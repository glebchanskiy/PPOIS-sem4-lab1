import enum

USAGE = """
Usage: atm-client -c:p:itw:o:g

where:
-c | --card           eight-digit card number
-p | --pin            four-digit PIN code
-i | --info           main information about the bank account
-t | --transfers      all account transactions 
-w | --withdraw       withdraw cash
-o | --phone          pay the phone bill
-g | --get_card       card back
"""

NO_CARD = "Insert the card!"

NO_PIN = "Enter the PIN code!"

ACCOUNT_NOT_FOUND = "Error, card account not found"

PIN_ACCEPTED = "[pin code accepted]"

PIN_NOT_ACCEPTED = "[pin code NOT accepted]"

CARD_ACCEPTED = "[card accepted]"

CARD_NOT_ACCEPTED = "[card NOT accepted]"

SUCCESS = 'Successfully!'

class FAILUR:
    BASIC = "Failure!"
    INSUFFICIENT_FOUNDS = "Failure! Insufficient funds!"
    INSUFFICIENT_FOUNDS_IN_ATM = "Failure! Sorry, there are no funds in the ATM."
    INVALID_INPUT = "Refusal to withdraw funds\nInvalid input: "