import tkinter as tk
from pymongo import MongoClient 
from functions_mongo.adicionar_estoque import stockAddition
from functions_mongo.checar_por_id import checkStart
from functions_mongo.deletproduto import deletar_produto
from functions_mongo.modificar import modificarProduto

# Projeto

uri = 'mongodb+srv://pedroschutz:JsEGKeiFr3OiZgEV@cluster0.hpalcoc.mongodb.net/'
client = MongoClient(uri)
login_db = client.login_db
login_collection = login_db.user_information

def startCadastro():
    while True:
        user = input("====================== / SISTEMA DE LOGIN - CADASTRO \ ======================\nQual é o nome de usuário?: ")
        password = input("Qual é a senha?: ")
        
        existing_name = login_collection.find_one({"nomeDeUsuario": user})
        if existing_name:
                print("[❌ ERRO] O nome de usuário já está em uso")
        else:

            add_user = {
            'nomeDeUsuario': user,
            'senhaUsuario': password
            }

            login_collection.insert_one(add_user)
            print("[✅ SUCESSO] Seu usuário foi criado")
            print("[🔄 REDIRECIONANDO] Redirecionando a tela inicial")
            mainMenu()
            break

def startLogin():
     while True:
        user = input("====================== / SISTEMA DE LOGIN - ENTRAR \ ======================\nQual é o nome de usuário? ")
        password = input("Qual é a senha? ")

        user_info = {"nomeDeUsuario": user, "senhaUsuario": password}
        
        check_login = login_collection.find_one(user_info)
        if check_login:
           print("[✅ SUCESSO] Entrando no menu de administração de estoque")
           admMenu()
           break
        else: 
           print("[❌ ERRO] Seu nome de usuário ou senha está incorreto, digite novamente.")
    
def mainMenu():
    while True:
        choice1 = input("====================== / ESTOQUE$ \ ======================\nBem-vindo(a) ao ESTOQUE$, deseja fazer login ou criar uma nova conta?\n[L] Login\n[C] Cadastrar\n")
        if choice1 == "C":
            startCadastro()
            break
        elif choice1 =="L":
            startLogin()
            break
        else:
            print("[❌ ERRO] Digite uma letra válida")


def admMenu():
    print("============================================== / ESTOQUE$ \ ============================================\nVocê está logado(a) no painel de controle do estoque, aqui você poderá configurar a database e manter em vista seu estoque.\n[                        PAINEL DE CONTROLE                        ]\nSelecione o que deseja fazer.\n[V] Checar produto\n[A] Adicionar produtos\n[R] Remover produtos\n[M] Modificar produtos")

    while True:
        choice2 = input("Resposta: ")
        if choice2 == "V":
            checkStart()
            break
        elif choice2 == "A":
            stockAddition()
            break
        elif choice2 == "R":
            deletar_produto()
            break
        elif choice2 == "M":
            modificarProduto()
            break
        else:
            print("[❌ ERRO] Digite uma letra válida")

mainMenu()


# checkStart()
# stockAddition()
# deletar_produto