from utils.log import Log
import pprint as pp

class Menu:
    def __init__(self, fc):
        self.fc = fc[0]

    def show_display(self):
        while True:
            print(50 * "*")
            print("FamilyTime")
            print(50 * "*")
            print("1 - pesquisar profissão")
            print("2 - pesquisar quem é o pai")
            print("3 - pesquisar tempo de casado")
            print("0 - sair")
            print(50 * "-")
            op = input("selecione a opção desejada: ")
            print(50 * "-")

            if op == "0":
                break
            elif op == "1": # Pesquisar profissão
                self.fc.search_occupation(input("digite a profissão:\n"))
            elif op == "2":
                self.fc.search_father(input("digite o nome do filho(a):\n"))
            elif op == "3":
                self.fc.search_married_time(input("digite o nome:\n"))
            else:
                print("opção incorreta")

            print(50 * "-")
            
            input("pressione enter para continuar...")