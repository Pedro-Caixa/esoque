from pymongo import MongoClient

uri = 'mongodb+srv://pedroschutz:JsEGKeiFr3OiZgEV@cluster0.hpalcoc.mongodb.net/'
client = MongoClient(uri)
db = client.estoque_db
collection = db.estoques

def modificarProduto():
   while True:
    produto = input("Insira o nome do produto que deseja modificar")

    isInDB = collection.find_one(produto)

    if isInDB:
        while True:
            print("Qual modificação deseja realizar?") 
            modify_selection = input("[N] Nome\n[Q] Quantidade\n[S] Saldo\n[P] Preço\n[F] Fornecedor\n[C] Categoria")
            if modify_selection == "N":
                print("VOCE SELECIONOU NOME")
                break
            elif modify_selection == "Q":
                print("QUANTIDADE")
                break
            elif modify_selection == "P":
                print("PREÇO")
                break
            elif modify_selection == "F":
                print("FORNECEDOR")
                break
            elif modify_selection == "C":
                print("CATEGORIA")
                break
            else:
                print("[❌ERRO] A ação não foi encontrada, tente novamente.")
    else:
        print("[❌ERRO] O produto não está no estoque, verifique se o nome está exatamente escrito como na database.")
    