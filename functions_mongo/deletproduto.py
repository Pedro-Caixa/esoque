from pymongo import MongoClient 

uri = 'mongodb+srv://pedroschutz:JsEGKeiFr3OiZgEV@cluster0.hpalcoc.mongodb.net/'
client = MongoClient(uri)
db = client.estoque_db
collection = db.estoques


def deletar_produto():
    from main import admMenu
    while True:
        produto_id = input("Digite o ID do produto a ser deletado (ou 'sair' para voltar ao menu): ")

        item_a_deletar = {'idProduto':int(produto_id)}
        deletar = collection.delete_one(item_a_deletar)
        
        if deletar.deleted_count > 0:
            print("[✅ SUCESSO] Produto deletado com sucesso.")
            admMenu()
        else:
            print("[❌ ERRO] Nenhum produto encontrado com o ID informado.")

