import sqlite3
import pathlib

class ClientDAO:
    def __init__(self):
        self.cursor = sqlite3.connect(f"{pathlib.Path().resolve()}/db/banco.db", isolation_level=None).cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS clients(id integer primary key autoincrement, nome varchar(200) not null, cpf varchar(11) not null, email varchar(100), id_plano integer);")
    
    def create(self, client):
        query = f"insert into clients(nome, cpf, email, id_plano) values ('{client.name}', '{client.cpf}', '{client.email}', {client.code_schema});"
        print(query)
        self.cursor.execute(query)
        print("Sucesso!", end="\n\n")

    def update(self, client):
        query = f"UPDATE clients set nome = '{client.name}', cpf = '{client.cpf}', email = '{client.email}', id_plano = {client.code_schema} where cpf = '{client.cpf}';"
        self.cursor.execute(query)
        print("Sucesso!", end="\n\n")

    def show_all(self):
        query = "Select * from clients;"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            print(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")

    def delete(self, client):
        query = f"delete from clients where cpf = '{client.cpf}';"
        self.cursor.execute(query)
        print("Sucesso!", end="\n\n")