from model.connector import Connector
from controller.family_controller import FamilyController
from utils.log import Log
from view.menu import Menu

conf = {
        "host": "localhost",
        "port": 7687,
        "user": "neo4j",
        "password": "toor"
    }

def setup():
    if input('Deseja utilizar as configurações de conexão padrão?\n(s|n): ') == 'n':
        conf["host"] = input('Host\n> ')
        conf["port"] = input('Porta\n> ')
        conf["user"] = input('Usuário\n> ')
        conf["password"] = input('Senha\n> ')
    else:
        ('Usando configurações padrão.')

    if input('\nDeseja reconstruir o banco de dados?\n!!! Isto irá eliminar todos os dados preexistentes !!!\n(s|n): ') == 's':
        cn = Connector(
            conf["host"],
            conf["port"],
            conf["user"],
            conf["password"]
        )

        cn.connect()

        fc = FamilyController([cn.driver])
        fc.build_standard_database()

        cn.close()
    else:
        Log.info('Base de dados inalterada.', "success")

def main():
    cn = Connector(
        conf["host"],
        conf["port"],
        conf["user"],
        conf["password"]
    )

    cn.connect()

    fc = FamilyController([cn.driver])

    menu = Menu([fc])

    menu.show_display()
    cn.close()

if __name__ == '__main__':
    setup()
    main()