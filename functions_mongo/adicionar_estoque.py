from pymongo import MongoClient
import datetime
import random
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

uri = 'mongodb+srv://pedroschutz:JsEGKeiFr3OiZgEV@cluster0.hpalcoc.mongodb.net/'
client = MongoClient(uri)
db = client.estoque_db
collection = db.estoques

def stockAddition():
    janela_add_produto = ctk.CTkToplevel()
    janela_add_produto.title("Adicionar Produto")

    frame = ctk.CTkFrame(master=janela_add_produto)  
    frame.pack(pady=20,padx=40, fill='both',expand=True)  

    label_nome = ctk.CTkLabel(frame, text="Nome do produto:")
    label_nome.grid(row=1, column=0, pady=10, padx= 10)
    entry_nome = ctk.CTkEntry(frame)
    entry_nome.grid(row=1, column=1, pady=10, padx= 10)

    label_quant_compra = ctk.CTkLabel(frame, text="Quantidade de compra:")
    label_quant_compra.grid(row=2, column=0, pady=10, padx= 10)
    entry_quant_compra = ctk.CTkEntry(frame)
    entry_quant_compra.grid(row=2, column=1, pady=10, padx= 10)


    label_quant_saldo = ctk.CTkLabel(frame, text="Quantidade do saldo:")
    label_quant_saldo.grid(row=3, column=0, pady=10, padx= 10)
    entry_quant_saldo = ctk.CTkEntry(frame)
    entry_quant_saldo.grid(row=3, column=1, pady=10, padx= 10)

    label_price = ctk.CTkLabel(frame, text="Preço do produto:")
    label_price.grid(row=4, column=0, pady=10, padx= 10)
    entry_price = ctk.CTkEntry(frame)
    entry_price.grid(row=4, column=1, pady=10, padx= 10)

    label_for = ctk.CTkLabel(frame, text="Nome do fornecedor:")
    label_for.grid(row=5, column=0, pady=10, padx= 10)
    entry_for = ctk.CTkEntry(frame)
    entry_for.grid(row=5, column=1, pady=10, padx= 10)

    label_dep = ctk.CTkLabel(frame, text="Departamento do item:")
    label_dep.grid(row=6, column=0, pady=10, padx= 10)
    entry_dep = ctk.CTkEntry(frame)
    entry_dep.grid(row=6, column=1, pady=10, padx= 10)

    label_cat = ctk.CTkLabel(frame, text="Categoria do produto:")
    label_cat.grid(row=7, column=0, pady=10, padx= 10)
    entry_cat = ctk.CTkEntry(frame)
    entry_cat.grid(row=7, column=1, pady=10, padx= 10)

    def adicionar():
            get_prod_name = entry_nome.get()
            get_quant_compra = entry_quant_compra.get()
            get_quant_saldo = entry_quant_saldo.get()
            get_price = entry_price.get()
            get_for = entry_for.get()
            get_dep = entry_dep.get()
            get_cat = entry_cat.get()

            random_id = random.randint(2, 99999)

            add_estoque = {
                "idProduto": random_id,
                "nomeProduto": get_prod_name,
                "quantidade": int(get_quant_compra),
                "saldo": int(get_quant_saldo),
                "preco": float(get_price),
                "fornecedor": get_for,
                "data": datetime.datetime.now(tz=datetime.timezone.utc),
                "departamento": get_dep,
                "categoria": get_cat,
            }

            collection.insert_one(add_estoque)

            resultado = "O produto {} foi adicionado com sucesso.\n".format(get_prod_name)
            resultado += "\n"
            resultado += "Nome do produto: {}\n".format(get_prod_name)
            resultado += "Quantidade: {}\n".format(get_quant_compra)
            resultado += "Preço: R$ {}\n".format(get_price)
            resultado += "Fornecedor: {}\n".format(get_for)

            CTkMessagebox(
                    title="Adicionar produto",
                    message=resultado,
                    icon="check",
                    option_1=["OK"]
                )
            janela_add_produto.destroy()



    button_adicionar = ctk.CTkButton(janela_add_produto, text="Adicionar", command=adicionar)
    button_adicionar.pack(pady=12,padx=10)  


    janela_add_produto.mainloop()
