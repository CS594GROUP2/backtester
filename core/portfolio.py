import pandas as pd

class Portfolio:

    # Constructor to initialize the portfolio
    # Right now, expecting a float parameter that will have the initial cash available

    def __init__(self, starting_cash: float):
        self.starting_cash = starting_cash
        self.cash = starting_cash

        # Dictionary in case we want to implement the ability to see the stocks we hold
        self.holdings = {}

        # Here we are also initializing the value of the portfolio which should be 0 at first
        self.portfolio_value = 0.0

    # getters

    # For now, will keep it simple, but I believe we can use the holdings dictionary more efficient here
    def get_portfolio_value(self) -> float:

        return self.portfolio_value

    def get_available_cash(self) -> float:

        return self.cash