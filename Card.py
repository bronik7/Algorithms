class Card:

    def __init__(self,suite,value):
        self.suite =suite
        self.value=value


    def __repr__(self):
        return f"{self.suite} of {self.value}"



