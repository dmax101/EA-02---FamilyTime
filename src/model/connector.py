from neo4j import GraphDatabase
from utils.log import Log

class Connector:
    # Construtor da conexão
    def __init__(self, host, port, user, pw) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = pw

    def connect(self):
        try:
            uri = "neo4j://{}:{}".format(
                self.host,
                self.port
            )
            user = self.user
            password = self.password

            self.driver = GraphDatabase.driver(uri, auth=(user, password))
            Log.info("Conexão estabelecida com sucesso!","success","Connector")
        except:
            Log.info("Ocorreu algum erro!","error","Connector")

    def close(self):
        self.driver.close()
        Log.info("Conexão encerrada com sucesso!","success","Connector")