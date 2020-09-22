import json


class Constant:
    """
    class used to load constants
    """
    def __init__(self):
        self.constant = self.load_constant()

    @staticmethod
    def load_constant():
        with open('constant.json') as file:
            return json.load(file)
