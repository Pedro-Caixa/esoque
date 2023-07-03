from pymongo import MongoClient
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

uri = 'mongodb+srv://pedroschutz:JsEGKeiFr3OiZgEV@cluster0.hpalcoc.mongodb.net/'
client = MongoClient(uri)
db = client.estoque_db
collection = db.estoques

def modificarProduto():
    janela_modificar_produto = ctk.CTkToplevel()
    janela_modificar_produto.title("Modificar Produto")
    
    frame = ctk.CTkFrame(master=janela_modificar_produto)  
    frame.grid()

    label_nome_produto = ctk.CTkLabel(frame, text="Nome do produto que deseja modificar:")
    label_nome_produto.grid(row=0, column=0, pady=10, padx= 10)
    entry_nome_produto = ctk.CTkEntry(frame)
    entry_nome_produto.grid(row=0, column=1, pady=10, padx= 10)

    label_info_modificacao = ctk.CTkLabel(frame, text="Novas Modificações")
    label_info_modificacao.grid(row=1, column=0, pady=10, padx= 10)

    label_nome = ctk.CTkLabel(frame, text="Nome:")
    label_nome.grid(row=2, column=0, pady=10, padx= 10)
    entry_nome = ctk.CTkEntry(frame)
    entry_nome.grid(row=2, column=1, pady=10, padx= 10)

    label_quantidade = ctk.CTkLabel(frame, text="Quantidade:")
    label_quantidade.grid(row=3, column=0, pady=10, padx= 10)
    entry_quantidade = ctk.CTkEntry(frame)
    entry_quantidade.grid(row=3, column=1, pady=10, padx= 10)

    label_saldo = ctk.CTkLabel(frame, text="Saldo:")
    label_saldo.grid(row=4, column=0, pady=10, padx= 10)
    entry_saldo = ctk.CTkEntry(frame)
    entry_saldo.grid(row=4, column=1, pady=10, padx= 10)

    label_preco = ctk.CTkLabel(frame, text="Preço:")
    label_preco.grid(row=5, column=0, pady=10, padx= 10)
    entry_preco = ctk.CTkEntry(frame)
    entry_preco.grid(row=5, column=1, pady=10, padx= 10)

    label_fornecedor = ctk.CTkLabel(frame, text="Fornecedor:")
    label_fornecedor.grid(row=6, column=0, pady=10, padx= 10)
    entry_fornecedor = ctk.CTkEntry(frame)
    entry_fornecedor.grid(row=6, column=1, pady=10, padx= 10)

    label_departamento = ctk.CTkLabel(frame, text="Departamento:")
    label_departamento.grid(row=7, column=0, pady=10, padx= 10)
    entry_departamento = ctk.CTkEntry(frame)
    entry_departamento.grid(row=7, column=1, pady=10, padx= 10)

    label_categoria = ctk.CTkLabel(frame, text="Categoria:")
    label_categoria.grid(row=8, column=0, pady=10, padx= 10)
    entry_categoria = ctk.CTkEntry(frame)
    entry_categoria.grid(row=8, column=1, pady=10, padx= 10)

    def modificar():
        produto = entry_nome_produto.get()
        produto_mongo = collection.find_one({"nomeProduto": produto})

        if produto_mongo:
            filtro = {"nomeProduto": produto}
            change_name = entry_nome.get() or produto_mongo['nomeProduto']
            change_amount = entry_quantidade.get() or produto_mongo['quantidade']
            change_sal = entry_saldo.get() or produto_mongo['saldo']
            change_price = entry_preco.get() or produto_mongo['preco']
            change_for = entry_fornecedor.get() or produto_mongo['fornecedor']
            change_dep = entry_departamento.get() or produto_mongo['departamento']
            change_category = entry_categoria.get() or produto_mongo['categoria']
          
            collection.update_many(filtro, {
                "$set": {
                    "nomeProduto": change_name,
                    "quantidade": change_amount,
                    "saldo": change_sal,
                    "preco": change_price,
                    "fornecedor": change_for,
                    "departamento": change_dep,
                    "categoria": change_category
                }
            })
            CTkMessagebox(
                  title="Sucesso",
                  message="O produto {} foi modificado com sucesso!".format(produto_mongo["nomeProduto"]),
                  icon="check",
                  option_1=["OK"]
                  )           
        else:
          CTkMessagebox(
                title="Erro",
                message="Nenhum produto com o nome {} foi encontrado!".format(produto_mongo["nomeProduto"]),
                icon="cancel",
                option_1=["OK"]
                )
        janela_modificar_produto.destroy()

    button_modificar = ctk.CTkButton(janela_modificar_produto, text="Modificar", command=modificar)
    button_modificar.grid()
    janela_modificar_produto.mainloop()
