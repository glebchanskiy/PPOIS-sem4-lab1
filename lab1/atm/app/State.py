from typing import Dict, List, Tuple

import json
import os

# JsonType = Dict[str, str]


class State:
    card_number: str = None
    pincode: str = None
    monies: int = None

    args: List[Tuple[str, str]]

    def __init__(self) -> None:
        with open(os.path.join(os.getcwd(), 'lab1', 'atm', 'app', 'resources', 'state.json'), "r") as file:
            data = json.load(file)
            self.card_number = data['card_number']
            self.pincode = data['pincode']
            self.monies = data['monies']

    def setUserInput(self, args: List[Tuple[str, str]]) -> None:
        self.args = args

    def __del__(self) -> None:
        with open(os.path.join(os.getcwd(), 'lab1', 'atm', 'app', 'resources', 'state.json'), "w") as file:
            json.dump(
                {
                    "card_number":  self.card_number,
                    "pincode":  self.pincode,
                    "monies": self.monies
                },
                file,
                indent=4
            )
