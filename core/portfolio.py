import numpy as np

class Portfolio:

    # Constructor to initialize the portfolio

    def __init__(self, starting_cash):
        self.starting_cash = starting_cash

    # getters
    
    def get_starting_cash(self) -> float:

        return self.starting_cash
