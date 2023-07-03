from pymongo import MongoClient
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

uri = 'mongodb+srv://pedroschutz:JsEGKeiFr3OiZgEV@cluster0.hpalcoc.mongodb.net/'
client = MongoClient(uri)
db = client.estoque_db
collection = db.estoques

def deletar_produto():
    janela_deletar_produto = ctk.CTkToplevel()
    janela_deletar_produto.title("Deletar Produto")

    frame = ctk.CTkFrame(master=janela_deletar_produto)  
    frame.pack(pady=20,padx=40, fill='both',expand=True) 

    label_produto_id = ctk.CTkLabel(frame, text="ID do produto a ser deletado:")
    label_produto_id.pack()

    entry_produto_id = ctk.CTkEntry(frame)
    entry_produto_id.pack()



    def deletar():
        produto_id = entry_produto_id.get()

        info_produto = collection.find_one({'idProduto': int(produto_id)})
        item_a_deletar = {'idProduto': int(produto_id)}
      
        deletar = collection.delete_one(item_a_deletar)
     
        if deletar.deleted_count > 0:
          CTkMessagebox(
                title="Sucesso",
                message="O produto {} foi deletado com sucesso!".format(info_produto["nomeProduto"]),
                icon="check",
                option_1=["OK"]
                )
        else:
          CTkMessagebox(
                title="Erro",
                message="Nenhum produto com o ID {} foi encontrado!".format(produto_id),
                icon="cancel",
                option_1=["OK"]
                )

    button_deletar = ctk.CTkButton(frame, text="Deletar", command=deletar)
    button_deletar.pack(pady=12,padx=10) 
    janela_deletar_produto.mainloop()