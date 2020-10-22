import json
import os


class Constant:
    """
    class used to load constants
    """
    constant = None

    @staticmethod
    def load_constant():
        with open(os.path.dirname(os.path.abspath(__file__)) + '/{}'.format('constant.json')) as file:
            Constant.constant = json.load(file)
