from contextlib import nullcontext


class Client:
    def __init__(self, name = nullcontext, cpf = nullcontext, email = nullcontext, code_schema = nullcontext, id = nullcontext):
        self.name = name
        self.cpf = cpf
        self.email = email
        self.code_schema = code_schema
        self.id = id
