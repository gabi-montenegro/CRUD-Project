from Usuarios import Usuarios 
from tkinter import *

class Application:
    def __init__(self, master):
        self.font = ("Verdana", "12")
        
        

        self.container1 = Frame(master)
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8.pack()

    

        #teste
        #self.container9 = Frame(master)
        #self.container9.pack()
        #self.container10 = Frame(master)
        #self.container10.pack()

        #Titulo -> container1
        self.lblTitle = Label(self.container1, text="Informe os dados do usuário:", font=("Verdana", "12", "bold"))
        self.lblTitle.grid(row = 0, column=0, columnspan=6, pady=1)

        #Label id + caixa de entrada + botao Buscar -> container2
        self.lblId = Label(self.container2, text="Id:", font=self.font)
        self.lblId.grid(row = 1, column=0, pady=6, padx = 5)

        self.entryId = Entry(self.container2, font = self.font, width=8)
        self.entryId.grid(row = 1, column = 1,pady=6, padx=5)

        self.btnSearch = Button(self.container2, text="Buscar", font=self.font, width=7, command=self.buscarUsuario, bg='#63A7EB')
        self.btnSearch.grid(row = 1, column = 2, pady=6)

        #Label nome + caixa de entrada -> container 3
        self.lblName = Label(self.container3, text="Nome:", font=self.font)
        self.lblName.grid(row = 2, column = 0, pady = 6, padx=8)

        self.entryName = Entry(self.container3, font=self.font)
        self.entryName.grid(row = 2, column = 1, columnspan = 5, padx= 12)

        #Label idade + caixa de entrada -> container 4
        self.lblAge = Label(self.container4, text="Idade:", font=self.font)
        self.lblAge.grid(row = 3, column = 0, pady = 6)

        self.entryAge = Entry(self.container4, font=self.font)
        self.entryAge.grid(row = 3, column = 1, columnspan= 5, padx= 10)

        #Label usuario + caixa de entrada -> container 5
        self.lblUsu = Label(self.container4, text="Usuário:", font=self.font)
        self.lblUsu.grid(row = 4, column = 0, pady = 6)

        self.entryUsu = Entry(self.container4, font=self.font)
        self.entryUsu.grid(row = 4, column = 1, columnspan= 5)

        #Label senha + caixa de entrada -> container 6
        self.lblPwd = Label(self.container4, text="Senha:", font=self.font)
        self.lblPwd.grid(row = 5, column = 0, pady = 6)

        self.entryPwd = Entry(self.container4, font=self.font, show="*")
        self.entryPwd.grid(row = 5, column = 1, columnspan= 5)

        #Buttons Incluir + Alterar + Excluir -> container 7
        self.include = Button(self.container7, text="Incluir", font=self.font, width=8, command=self.inserirUsuario, bg='#76B882')
        self.include.grid(row = 6, column = 0, pady = 6, padx = 3)

        self.update = Button(self.container7, text="Alterar", font=self.font, width=8, command=self.updateUsuario, bg='#F0E347')
        self.update.grid(row = 6, column = 1, pady = 6, padx = 3)

        self.delete = Button(self.container7, text="Excluir", font=self.font, width=8, command=self.excluirUsuario, bg='#E03E36')
        self.delete.grid(row = 6, column = 2, pady = 6, padx= 3)

        #Mensagem
        self.lblMsg = Label(self.container8, text="", font=self.font)
        self.lblMsg.grid(row = 7, column = 0, columnspan= 6)

        #Tabela de usuarios
        '''self.lblTable = Label(self.container9, text="Tabela de Usuários", font=self.font)
        self.lblTable.grid(row = 8, column = 0, columnspan= 6, pady=6)
        self.lblTable2 = Label(self.container10, text="", font=self.font)
        self.lblTable2.grid(row = 8, column = 0, columnspan= 6, pady=6)'''




    def inserirUsuario(self):
        user = Usuarios()

        if(self.verificaIdade() == False):
            self.lblMsg["text"] = "Idade inválida."

        elif(self.verificaUsuario(user)):
            self.lblMsg["text"] = "Nome de Usuario invalido"

        elif(self.verificaNome() == False):
            self.lblMsg["text"] = "Nome invalido"

        else:

            user.nome = self.entryName.get()
            user.idade = self.entryAge.get()
            user.usuario = self.entryUsu.get()
            user.senha = self.entryPwd.get()


            self.lblMsg["text"] = user.insertUser()

            self.entryId.delete(0, END)
            self.entryName.delete(0, END)
            self.entryAge.delete(0, END)
            self.entryUsu.delete(0, END)
            self.entryPwd.delete(0, END)

        #self.showTable()


    def updateUsuario(self):
        user = Usuarios()

        if(self.verificaIdade() == False):
            self.lblMsg["text"] = "Idade inválida."

        elif(self.verificaUsuario(user)):
            self.lblMsg["text"] = "Nome de Usuario invalido"

        elif(self.verificaNome() == False):
            self.lblMsg["text"] = "Nome invalido"

        else:
            user.id = self.entryId.get()
            user.nome = self.entryName.get()
            user.idade = self.entryAge.get()
            user.usuario = self.entryUsu.get()
            user.senha = self.entryPwd.get()

            self.lblMsg["text"] = user.updateUser()

            self.entryId.delete(0, END)
            self.entryName.delete(0, END)
            self.entryAge.delete(0, END)
            self.entryUsu.delete(0, END)
            self.entryPwd.delete(0, END)

    def excluirUsuario(self):
        user = Usuarios()

        user.id = self.entryId.get()

        self.lblMsg["text"] = user.deleteUser()

        self.entryId.delete(0, END)
        self.entryName.delete(0, END)
        self.entryAge.delete(0, END)
        self.entryUsu.delete(0, END)
        self.entryPwd.delete(0, END)

    def buscarUsuario(self):
        user = Usuarios()

        id = self.entryId.get()

        self.lblMsg["text"] = user.selectUser(id)

        self.entryId.delete(0, END)
        self.entryId.insert(INSERT, user.id)

        self.entryName.delete(0, END)
        self.entryName.insert(INSERT, user.nome)

        self.entryAge.delete(0, END)
        self.entryAge.insert(INSERT, user.idade)

        self.entryUsu.delete(0, END)
        self.entryUsu.insert(INSERT, user.usuario)

        self.entryPwd.delete(0, END)
        self.entryPwd.insert(INSERT, user.senha)

    def verificaIdade(self):
        if(self.entryAge.get().isnumeric()):
            if(int(self.entryAge.get()) > 0 and int(self.entryAge.get()) < 105):
                return True 
            else:
                return False 
        else: 
            return False
        
    def verificaUsuario(self, user):
        usuarios = user.verificaUsuario(self.entryUsu.get())
        #print(usuarios[0][0], usuarios[0][1])

        if(len(usuarios) == 0): 
            return False #Permitido
        elif(len(usuarios) != 0  and (usuarios[0][0] == self.entryUsu.get()) and (usuarios[0][1] == self.entryId.get())):
            return False #alteracao permitida
        else:
            return True #alteracao nao permitida

        """if (len(usuarios) != 0):
            return True 
        else:
            return False """ 

    def verificaNome(self):
        for x in self.entryName.get():
            if(x == " "):
                continue 
            elif(x.isalpha()):
                chave = True 
            else:
                chave = False
                break

        return (chave)
            
    
window = Tk()
window.geometry('400x280')
window.title("Cadastro de Usuários")
Application(window)
window.mainloop()