import sqlite3
import pathlib

class SchemaDAO:
    def __init__(self):
        self.cursor = sqlite3.connect(f"{pathlib.Path().resolve()}/db/banco.db", isolation_level=None).cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS schemas(codigo integer, nome varchar(200), mensalidade decimal(10, 2));")
    
    def create(self, schema):
        query = f"insert into schemas(codigo, nome, mensalidade) values ({schema.code}, '{schema.name}', {schema.monthly_payment});"
        print(query)
        self.cursor.execute(query)
        print("Sucesso!", end="\n\n")

    def update(self, schema):
        query = f"UPDATE schemas set nome = '{schema.name}', mensalidade = {schema.monthly_payment} where codigo = {schema.code};"
        self.cursor.execute(query)
        print("Sucesso!", end="\n\n")

    def show_all(self):
        query = "Select * from schemas;"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            print(f"| {row[0]} | {row[1]} | {row[2]} |")

    def delete(self, schema):
        query = f"delete from schemas where codigo = {schema.code};"
        self.cursor.execute(query)
        print("Sucesso!", end="\n\n")