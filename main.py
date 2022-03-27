from contextlib import nullcontext
from utils import menus
from models.schema import Schema
from models.client import Client
from controllers.schemaDao import SchemaDAO
from controllers.clientDao import ClientDAO

first_selection = -1
while (first_selection != 3):
    menus.default_menu()
    first_selection = int(input())

    while (first_selection < 1 or first_selection > 3):
        print("Opção inválida, escolha novamente", end=" ")
        first_selection = int(input())

    if(first_selection == 1):
        second_selection = - 1
        while second_selection != 5:
            
            menus.clients_menu()
            second_selection = int(input())

            while(second_selection < 1 or second_selection > 5):
                print("Opção inválida, por favor selecione outra")
                second_selection = int(input())

            if second_selection != 5:
                client = nullcontext
                if (second_selection == 1 or second_selection == 3):
                    name = input("Qual o nome do cliente?")
                    email = input("Qual o email do cliente?")
                    code_schema = int(input("Qual o código do plano ao qual o cliente está associado?"))
                    cpf = input("Qual o cpf do cliente?")
                    client = Client(name=name, email=email, code_schema=code_schema, cpf=cpf)
                elif(second_selection == 4):
                    cpf = input("Qual o cpf do cliente?")
                    client = Client(cpf=cpf)

                clientController = ClientDAO()

                switch_dao = {
                    1: clientController.create,
                    2: clientController.show_all,
                    3: clientController.update,
                    4: clientController.delete,
                }

                switch_dao.get(second_selection)(client) if second_selection != 2 else switch_dao.get(second_selection)()
    elif(first_selection == 2):
        second_selection = -1
        while(second_selection != 5):
            menus.scheme_menu()
            second_selection = int(input())

            while(second_selection < 1 or second_selection > 5):
                print("Opção inválida, por favor selecione outra")
                second_selection = int(input())

            if second_selection != 5:
                schemaController = SchemaDAO()

                schema = nullcontext

                if(second_selection == 1 or second_selection == 3):
                    name = input("Qual o nome do plano?")
                    code = int(input("Qual o código do plano?"))
                    monthly_payment = float(input("Qual a mensalidade do plano?"))
                    schema = Schema(name=name, code=code, monthly_payment=monthly_payment)
                elif (second_selection == 4):
                    code_schema = input("Qual o código do plano?")
                    schema = Schema(code=code_schema)

                switch_dao = {
                    1: schemaController.create,
                    2: schemaController.show_all,
                    3: schemaController.update,
                    4: schemaController.delete,
                }

                switch_dao.get(second_selection)(schema) if second_selection != 2 else switch_dao.get(second_selection)()
