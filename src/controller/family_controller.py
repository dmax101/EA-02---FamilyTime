import pprint as pp
import os
from utils.log import Log

class FamilyController:
    def __init__(self, driver):
        self.driver = driver[0]

    def db_engine(self, query, list=False):
        with self.driver.session() as graphDB_Session:
            nodes = graphDB_Session.run(query)
        
            if list == True:
                for node in nodes:
                    if len(node) == 1:
                        name = "{}".format(node[0])
                        print(name)
                    else:
                        name = "{}".format(node[0])
                        price = "{}".format(node[1])
                        print(name + ": R$ " + price)
            else:
                for node in nodes:
                    if "SUM(p.price)" in node.data():
                        sum_node = float(node["SUM(p.price)"])
                        return sum_node
                    
                    if len(node['p']) == 1:
                        name = node['p']['name']
                        return [name]
                    else:
                        name = node['p']['name']
                        price = float(node['p']['price'])
                        
                        return {"name": name, "price": price}

    def build_standard_database(self):
        # Using readline()
        cur_path = os.path.dirname(__file__)
        path = cur_path.replace("\\controller", "") + "\\database\\database.cql"
        
        file = open(path, 'r', encoding='utf-8')
        
        query = ""

        while True:
            line = file.readline()
            query = line.strip()

            if not (query == ""):
                self.db_engine(query, True)

            if not line:
                break

        Log.info("Database construído com sucesso!", "success", "FamilyController")

        file.close()
    
    def search_occupation(self, occupation):
        query = "MATCH (p:" + occupation + ") RETURN p.nome"

        self.db_engine(query, True)

    def search_father(self, name):
        query = "MATCH (:Person{nome: '" + name + "'})<-[:PAI_DE]-(p:Person) RETURN p.nome"

        self.db_engine(query, True)

    def search_married_time(self, name):
        query = "MATCH (p:Person{nome: '" + name + "'})-[r:CASADO_COM]->() RETURN r.tempo"

        self.db_engine(query, True)