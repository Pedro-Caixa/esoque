from pymongo import MongoClient

uri = 'mongodb+srv://pedroschutz:JsEGKeiFr3OiZgEV@cluster0.hpalcoc.mongodb.net/'
client = MongoClient(uri)
db = client.estoque_db
collection = db.estoques

def modificarProduto():
    from main import admMenu
    while True:
        produto = input("Insira o nome do produto que deseja modificar: ")
        produto_mongo = collection.find_one({"nomeProduto": produto})
        if produto == "MENU":
            print("[🔄 REDIRECIONANDO]: Redirecionando ao menu!")
            admMenu()
            break
        else:

            if produto_mongo:
                print("Você está no painel de modificação. se não deseja mudar a informação, apenas deixe o local em branco.")
                filtro = {"nomeProduto": produto}
                change_name = input("Nome: ") or produto_mongo['nomeProduto']
                change_amount = input("Quantidade: ")  or produto_mongo['quantidade']
                change_sal = input("Saldo: ") or produto_mongo['saldo']
                change_price = input("Preço: ") or produto_mongo['preco']
                change_for = input("Fornecedor: ") or produto_mongo['fornecedor']
                change_dep = input("Departamento: ") or produto_mongo['departamento']
                change_category = input("Categoria: ") or produto_mongo['categoria']

                collection.update_many(filtro, {"$set": {"nomeProduto": change_name, "quantidade": change_amount, "saldo": change_sal, "preco": change_price, "fornecedor": change_for, "departamento": change_dep, "categoria": change_category}})
                print('[✅ SUCESSO]: Modificações completas')
                print("[INFO]:Se deseja retornar ao menu, apenas digite MENU")
            else:
                print("[❌ERRO]: O produto não está no estoque, verifique se o nome está exatamente escrito como na database.")

modificarProduto()

    

        
    