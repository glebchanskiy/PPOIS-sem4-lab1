from lab1.atm.app.ApplicationBuilder import ApplicationBuilder
from lab1.atm.app.CommandHandler import CommandHandler

from lab1.templates.messages import USAGE

from lab1.handlers.account_info import account_info
from lab1.handlers.transfers_info import transfers_info
from lab1.handlers.get_card import get_card
from lab1.handlers.insert_card import insert_card
from lab1.handlers.input_pincode import input_pincode
from lab1.handlers.withdrawal_operation import withdrawal_operation
from lab1.handlers.phone_payment_operation import phone_payment_operation



def main():
    app = ApplicationBuilder.build()
    app.add_handler(CommandHandler(('c:', 'card='), insert_card))
    app.add_handler(CommandHandler(('p:', 'pin='), input_pincode))
    app.add_handler(CommandHandler(('i', 'info'), account_info))
    app.add_handler(CommandHandler(('t', 'transfers'), transfers_info))
    app.add_handler(CommandHandler(('w:', 'withdraw='), withdrawal_operation))
    app.add_handler(CommandHandler(('o:', 'phone='), phone_payment_operation))
    app.add_handler(CommandHandler(('g', 'get_card'), get_card))
    app.add_root_handler(lambda : print(USAGE))
    app.start()


if __name__ == '__main__':
    main()
