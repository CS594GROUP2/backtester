class Portfolio:

    # Constructor to initialize the portfolio
    # Right now, expecting a float parameter that will have the initial cash available

    def __init__(self, starting_cash: float):
        self.starting_cash = starting_cash

    # getters
    
    def get_starting_cash(self) -> float:

        return self.starting_cash
