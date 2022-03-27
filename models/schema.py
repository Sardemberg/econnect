from contextlib import nullcontext


class Schema:
    def __init__(self, name = nullcontext, code = nullcontext, monthly_payment = nullcontext):
        self.name = name
        self.code = code
        self.monthly_payment = monthly_payment