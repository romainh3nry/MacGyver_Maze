import json


class Constant:
    """
    class used to load constants
    """
    constant = None

    @staticmethod
    def load_constant():
        with open('constant.json') as file:
            Constant.constant = json.load(file)
