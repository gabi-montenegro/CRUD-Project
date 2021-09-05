import mysql.connector


class Banco():
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="gabi",
            database="crud")

        self.createTable()

    def createTable(self):
        mycursor = self.connection.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), idade VARCHAR(5), usuario VARCHAR(255), senha VARCHAR(255))")
        self.connection.commit()


Banco()