#!/usr/bin/python3
import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'Chavez040718',
            db = 'manager_password'
        )

        self.cursor = self.connection.cursor()
        print("Conexión establecida exitosamente!")

    def show_data(self):
        sql = 'SELECT * FROM t_passwords'
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            for user in data:
                print(user)
        except Exception as e:
            print(e)

    def create_password(self, name, correo, password, key, lenght):
        sql = "INSERT INTO `t_passwords` VALUES(id, %s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (name, correo, password, key, lenght))
            self.connection.commit()
            print("Se registro su contraseña")
        except Exception as e:
            print(e)

    def read_password(self, name):
        sql = "SELECT name FROM"

    def cerrar_sesion(self):
        print("Conexión cerrada!")
        self.connection.close()


