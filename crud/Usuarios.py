from Banco import Banco 

class Usuarios(object):
    def __init__(self, id = 0, nome = "", idade="", usuario ="", senha = ""):
        self.info = {}
        self.id = id 
        self.nome = nome 
        self.idade = idade 
        self.usuario = usuario 
        self.senha = senha

    def insertUser(self):
        db = Banco()

        try:
            mycursor = db.connection.cursor()

            mycursor.execute("INSERT INTO usuarios (nome, idade, usuario, senha) SELECT * FROM (SELECT '"+ self.nome +"' as nome, '"+ self.idade + "' as idade, '"+ self.usuario +"' as usuario, '"+ self.senha +"' as senha) as temp WHERE NOT EXISTS (SELECT usuario FROM usuarios WHERE usuario = '"+ self.usuario + "') LIMIT 1") 

            #insert into usuarios (nome, idade, usuario, senha) 
            #select * from (select 'Joao' as nome, '23' as idade, 'gab_m' as usuario, '123456' as senha) as temp
            #where not exists (select usuario from usuarios where usuario = 'gab_m') limit 1;
            
            #WHERE NOT EXISTS (SELECT usuario from usuarios  WHERE usuario = '"+ self.usuario +"'")

            db.connection.commit()
            mycursor.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    
    def updateUser(self):
        db = Banco()

        try:
            mycursor = db.connection.cursor()

            mycursor.execute("UPDATE usuarios SET nome = '" + self.nome + "', idade = '" + self.idade + "', usuario = '"+ self.usuario + "', senha = '"+ self.senha + "' WHERE id = '" + self.id + "'")

            db.connection.commit()

            mycursor.close()

            return "Usuário atualizado com sucesso."
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):
        db = Banco()

        try:
            mycursor = db.connection.cursor()

            mycursor.execute("DELETE FROM usuarios WHERE id = '" + self.id + "'")

            db.connection.commit()
            mycursor.close()

            return "Usuário excluído com sucesso."
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, id):
        db = Banco()

        try:
            mycursor = db.connection.cursor()

            mycursor.execute("SELECT * FROM usuarios WHERE id = '"+ id +"'")

            for linha in mycursor:
                self.id = linha[0]
                self.nome = linha[1]
                self.idade = linha[2]
                self.usuario = linha[3]
                self.senha = linha[4]

            mycursor.close()

            return "Busca feita com sucesso."
        except:
            return "Ocorreu um erro na busca do usuário."

    def verificaUsuario(self, usu):
        db = Banco()

        try:
            mycursor = db.connection.cursor()
            mycursor.execute("SELECT usuario, id FROM usuarios WHERE usuario = '"+ usu +"'")

            return mycursor.fetchall()

        except:
            return "Ocorreu um erro na verificação do nome de usuário"

    
    """ def verificaIdUsuario(self, usu):
        db = Banco()

        try:
            mycursor = db.connection.cursor()
            mycursor.execute("SELECT id FROM usuarios WHERE usuario = '" + usu + "'")

            return mycursor.fetchall()
        except:
            return "Ocorreu um erro na verificação do nome de usuário" """


    '''def createTable(self):
        db = Banco()
        
        mycursor = db.connection.cursor()
        mycursor.execute("SELECT COUNT(*) FROM usuarios")

        return mycursor.fetchone()

    def getRow(self, id):
        db = Banco()

        mycursor = db.connection.cursor()

        
        idStr = str(id)
        mycursor.execute("SELECT nome, idade, usuario, senha FROM usuarios WHERE id = '"+ idStr +"'")

        return mycursor.fetchall()

    def getId(self):
        db = Banco()

        mycursor = db.connection.cursor()
        mycursor.execute("SELECT id FROM usuarios")

        return mycursor.fetchall()'''