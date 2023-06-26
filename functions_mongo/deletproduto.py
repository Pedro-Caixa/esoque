from pymongo import MongoClient 

uri = 'mongodb+srv://pedroschutz:JsEGKeiFr3OiZgEV@cluster0.hpalcoc.mongodb.net/'
client = MongoClient(uri)
db = client.estoque_db
collection = db.estoques


def deletar_produto():
    while True:
        produto_id = input("Digite o ID do produto a ser deletado (ou 'sair' para voltar ao menu): ")
        
        if produto_id.lower() == 'sair':
            break
        
        result = collection.delete_one({'_id': produto_id})
        
        if result.deleted_count > 0:
            print("Produto deletado com sucesso.")
        else:
            print("Nenhum produto encontrado com o ID informado.")
        print()