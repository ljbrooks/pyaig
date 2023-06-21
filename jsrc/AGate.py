
class AGate(list):
    def __init__(self, inputx, outputx, covered_litx=[]):
        list.__init__(self, inputx)
        self.covered_litx = covered_litx
        self.outputx = inputx
        pass
    pass
class AGate_OR(AGate):
    pass
class AGate_AND(AGate):
    pass
class AGate_XOR(AGate):
    pass
