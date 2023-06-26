from pymongo import MongoClient

uri = 'mongodb+srv://pedroschutz:JsEGKeiFr3OiZgEV@cluster0.hpalcoc.mongodb.net/'
client = MongoClient(uri)
db = client.estoque_db
collection = db.estoques


def checarPorId():
    while True:
        id_produto = input("[SISTEMA] Insira o ID do produto que deseja checar.\n")
        produto = collection.find_one({"idProduto": int(id_produto)})

        if produto:
            print("====================== / CHECAR PRODUTO \ ======================\nID do Produto:", produto["idProduto"],"\nNome do produto:",produto["nomeProduto"] ,"\nQuantidade:", produto["quantidade"],"\nPreço:", produto["preco"],"\nFornecedor:", produto["fornecedor"],"\nDepartamento:", produto["departamento"],"\nCategoria:", produto["categoria"],"\n====================== / FIM CHECAR PRODUTO \ ======================")
            break
        else:
            print("[❌ERRO]: Não foi possivel verificar o produto, verifique se foi adicionado o ID corredo ou se o produto existe.")


def listarPorId():
    while True:
        escolhaListar = input("[LISTA]: Deseja que a lista seja crescente ou decrescente?\n[C] Crescente\n[D] Decrescente\n")
        if escolhaListar == "C":
            produtos = collection.find().sort("idProduto", 1)
          
            lista_ordem_crescente = []
            
            for produto in produtos:
                 produto_formatado = f"idProduto: {produto['idProduto']}, " \
                       f"nomeProduto: {produto['nomeProduto']}, " \
                       f"Quantidade: {produto['Quantidade']}, " \
                       f"Preço: {produto['preco']}, " \
                       f"Fornecedor: {produto['fornecedor']}, " \
                       f"Data: {produto['data']}, " \
                       f"Departamento: {produto['Departamento']}, " \
                       f"Categoria: {produto['Categoria']}"
                 lista_ordem_crescente.append(produto_formatado)
            return lista_ordem_crescente
            
        else: 
            print("[❌ERRO]: A letra digitada está incorreta, insira um valor válido.")
            
 

def checkStart():
    while True:
        escolhaMain = input("[SISTEMA]: Como deseja checar os produtos?\n[I] Checar por ID\n[L] Listar em ordem crescente/decrescente\n(DIGITE A LETRA CORRESPONDENTE)\n")
        if escolhaMain == "I":
            checarPorId()
            break
        elif escolhaMain == "L":
            listarPorId()
            break
        else:
         print("[❌ERRO]: A letra digitada está incorreta, insira um valor válido")

    
