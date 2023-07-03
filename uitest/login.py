import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from pymongo import MongoClient
import datetime
import random

uri = 'mongodb+srv://pedroschutz:JsEGKeiFr3OiZgEV@cluster0.hpalcoc.mongodb.net/'
client = MongoClient(uri)
db = client.estoque_db
collection = db.estoques



def checarPorId():
    janela_checar_id = ctk.CTkToplevel()
    janela_checar_id.title("Checar Produto por ID")

    label_id = ctk.CTkLabel(janela_checar_id, text="ID do produto:")
    label_id.pack()
    entry_id = ctk.CTkEntry(janela_checar_id)
    entry_id.pack()

    def checar():
        id_produto = entry_id.get()
        produto = collection.find_one({"idProduto": int(id_produto)})


        if produto:
            resultado = "ID do Produto: {}\n".format(produto["idProduto"])
            resultado += "Nome do produto: {}\n".format(produto["nomeProduto"])
            resultado += "Quantidade: {}\n".format(produto["quantidade"])
            resultado += "Preço: {}\n".format(produto["preco"])
            resultado += "Fornecedor: {}\n".format(produto["fornecedor"])
            resultado += "Departamento: {}\n".format(produto["departamento"])
            resultado += "Categoria: {}\n".format(produto["categoria"])

            CTkMessagebox(
                title="Checar Produto",
                message= resultado,
                icon="check",
                option_1=["OK"]
                )
            janela_checar_id.destroy()
        else:
            CTkMessagebox(
                title="Erro",
                message="Não foi possível verificar o produto. Verifique se foi inserido o ID correto ou se o produto existe.",
                icon="cancel",
                option_1=["OK"]
                )
    button_checar = ctk.CTkButton(janela_checar_id, text="Checar", command=checar)
    button_checar.pack()


def listarPorId():
    janela_listar_id = ctk.CTkToplevel()
    janela_listar_id.title("Listar Produtos por ID")

    label_ordem = ctk.CTkLabel(janela_listar_id, text="Escolha a ordem:")
    label_ordem.pack()

    var_ordem = ctk.StringVar(janela_listar_id)
    var_ordem.set("crescente")

    radio_crescente = ctk.CTkRadioButton(janela_listar_id, text="Crescente", variable=var_ordem, value="crescente")
    radio_crescente.pack()

    radio_decrescente = ctk.CTkRadioButton(janela_listar_id, text="Decrescente", variable=var_ordem, value="decrescente")
    radio_decrescente.pack()

    def listar():
        ordem = var_ordem.get()
        sort_order = 1 if ordem == "crescente" else -1
        produtos = collection.find().sort("idProduto", sort_order)

        lista_produtos = []
        for produto in produtos:
            produto_formatado = "ID: {}, Nome: {}, Quantidade: {}, Preço: {}, Fornecedor: {}, Departamento: {}, Categoria: {}".format(
                produto["idProduto"], produto["nomeProduto"], produto["quantidade"], produto["preco"],
                produto["fornecedor"], produto["departamento"], produto["categoria"]
            )
            lista_produtos.append(produto_formatado)

        resultado = "\n".join(lista_produtos)

        CTkMessagebox(
                    title="Listar produtos",
                    message=resultado,
                    icon="check",
                    option_1=["OK"]
                )  
        janela_listar_id.destroy()

    button_listar = ctk.CTkButton(janela_listar_id, text="Listar", command=listar)
    button_listar.pack()


def checkStart():
    janela_check_start = ctk.CTkToplevel()
    janela_check_start.title("Checar Produtos")

    label_opcao = ctk.CTkLabel(janela_check_start, text="Como deseja checar os produtos?")
    label_opcao.pack()

    var_opcao = ctk.StringVar(janela_check_start)
    var_opcao.set("id")

    radio_id = ctk.CTkRadioButton(janela_check_start, text="Checar por ID", variable=var_opcao, value="id")
    radio_id.pack()

    radio_listar = ctk.CTkRadioButton(janela_check_start, text="Listar em ordem crescente/decrescente", variable=var_opcao, value="listar")
    radio_listar.pack()

    def abrir_opcao():
        opcao = var_opcao.get()
        if opcao == "id":
            checarPorId()
        elif opcao == "listar":
            listarPorId()
        janela_check_start.destroy()

    button_abrir_opcao = ctk.CTkButton(janela_check_start, text="Abrir Opção", command=abrir_opcao)
    button_abrir_opcao.pack()
    janela_check_start.mainloop()