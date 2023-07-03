import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from pymongo import MongoClient
from functions_mongo.checar_por_id import checkStart
from functions_mongo.deletproduto import deletar_produto
from functions_mongo.modificar import modificarProduto
from functions_mongo.adicionar_estoque import stockAddition

# Conexão com o banco de dados
uri = 'mongodb+srv://pedroschutz:JsEGKeiFr3OiZgEV@cluster0.hpalcoc.mongodb.net/'
client = MongoClient(uri)
login_db = client.login_db
login_collection = login_db.user_information




def admMenu():
    janela_adm = ctk.CTkToplevel(root)
    janela_adm.title("ESTOQUE$ - Painel de Controle")

    label_title = ctk.CTkLabel(janela_adm, text="PAINEL DE CONTROLE")
    label_title.pack()

    label_instrucao = ctk.CTkLabel(janela_adm, text="Selecione o que deseja fazer:")
    label_instrucao.pack(pady=12,padx=10)

    frame_admmenu = ctk.CTkFrame(master=janela_adm)  
    frame_admmenu.pack(pady=20,padx=40, fill='both',expand=True)  

    button_check = ctk.CTkButton(frame_admmenu, text="Checar produto", command=checkStart)
    button_check.pack(pady=12,padx=10)

    button_adicionar = ctk.CTkButton(frame_admmenu, text="Adicionar produtos", command=stockAddition)
    button_adicionar.pack(pady=12,padx=10)

    button_remover = ctk.CTkButton(frame_admmenu, text="Remover produtos", command=deletar_produto)
    button_remover.pack(pady=12,padx=10)

    button_modificar = ctk.CTkButton(frame_admmenu, text="Modificar produtos", command=modificarProduto)
    button_modificar.pack(pady=12,padx=10)

    janela_adm.mainloop() 

def startCadastro():
    janela_cadastro = ctk.CTkToplevel(root)
    janela_cadastro.title("ESTOQUE$ - Cadastro")
    janela_cadastro.geometry("300x320")

    def registrar():
        username = entry_username.get()
        password = entry_password.get()

        existing_name = login_collection.find_one({"nomeDeUsuario": username})
        if existing_name:
            CTkMessagebox(
                title="Erro",
                message="O nome de usuário já está em uso",
                icon="error",
                option_1=["OK"]
            )
        else:
            add_user = {
                'nomeDeUsuario': username,
                'senhaUsuario': password
            }
            login_collection.insert_one(add_user)
            CTkMessagebox(
                title="Sucesso",
                message="Seu usuário foi criado",
                icon="info",
                option_1=["OK"]
            )
            janela_cadastro.destroy()

    label = ctk.CTkLabel(janela_cadastro,text="Faça seu cadastro aqui")  
    label.pack(pady=20) 

    frame_registrar2 = ctk.CTkFrame(master=janela_cadastro)  
    frame_registrar2.pack(pady=20,padx=40, fill='both',expand=True)  

    label_login = ctk.CTkLabel(master=frame_registrar2, text='CADASTRO DE CONTA')  
    label_login.pack(pady=12,padx=10)  

    entry_username= ctk.CTkEntry(master=frame_registrar2, placeholder_text="Username")  
    entry_username.pack(pady=12,padx=10)  
    entry_password= ctk.CTkEntry(master=frame_registrar2, placeholder_text="Senha", show="*")  
    entry_password.pack(pady=12,padx=10)  

    button_registrar = ctk.CTkButton(master=frame_registrar2, text='Cadastrar', command=registrar)  
    button_registrar.pack(pady=12,padx=10)  

def startLogin():
    janela_login = ctk.CTkToplevel(root)
    janela_login.title("Login")
    janela_login.title("ESTOQUE$ - LOGIN")
    janela_login.geometry("300x320")

    windowWidth = janela_login.winfo_reqwidth()
    windowHeight = janela_login.winfo_reqheight()
    positionRight = int(janela_login.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(janela_login.winfo_screenheight() / 2 - windowHeight / 2)
    janela_login.geometry("+{}+{}".format(positionRight, positionDown))

    def login():
        username = entry_username.get()
        password = entry_password.get()

        user_info = {"nomeDeUsuario": username, "senhaUsuario": password}
        check_login = login_collection.find_one(user_info)

        if check_login:
            CTkMessagebox(
                title="Login bem-sucedido",
                message="Login bem-sucedido!",
                icon="info",
                option_1=["OK"]
            )
            janela_login.destroy()
            admMenu()
        else:
            CTkMessagebox(
                title="Erro de login",
                message="Credenciais inválidas!",
                icon="error",
                option_1=["OK"]
            )

    label = ctk.CTkLabel(janela_login,text="Faça seu login aqui")  
    label.pack(pady=20) 

    frame_login2 = ctk.CTkFrame(master=janela_login)  
    frame_login2.pack(pady=20,padx=40, fill='both',expand=True)  

    label_login = ctk.CTkLabel(master=frame_login2, text='LOGIN')  
    label_login.pack(pady=12,padx=10)  

    entry_username= ctk.CTkEntry(master=frame_login2, placeholder_text="Username")  
    entry_username.pack(pady=12,padx=10)  
    entry_password= ctk.CTkEntry(master=frame_login2, placeholder_text="Senha", show="*")  
    entry_password.pack(pady=12,padx=10)  

    button_login = ctk.CTkButton(master=frame_login2, text='Login', command=login)  
    button_login.pack(pady=12,padx=10)  


root = ctk.CTk()
root.title("Menu de Login")
root.geometry("200x220")

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
root.geometry("+{}+{}".format(positionRight, positionDown))

label_title = ctk.CTkLabel(root, text="ESTOQUE$")
label_title.pack(pady= 20, padx= 20)

frame = ctk.CTkFrame(master=root)  
frame.pack(pady=20,padx=40, fill='both',expand=True)  


button_login = ctk.CTkButton(frame, text="Login",  command=startLogin).pack(pady= 12, padx= 10)
button_cadastro = ctk.CTkButton(master=frame, text="Cadastrar", command=startCadastro).pack(pady= 12, padx= 10)

root.mainloop()
