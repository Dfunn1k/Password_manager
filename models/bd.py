#!/usr/bin/python3
import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'Chavez040718',
            db = 'menagerie'
        )

        self.cursor = self.connection.cursor()
        print("Conexión establecida exitosamente!")

    def traer_Datos(self):
        sql = 'SELECT * FROM t_familia'
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            for user in data:
                print(user)
        except Exception as e:
            print(e)

    def registrar_amigo(self, nombre, altura, peso, nacimiento, celular):
        sql = "INSERT INTO `t_familia` VALUES(id, %s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (nombre, altura, peso, nacimiento, celular))
            self.connection.commit()
        except Exception as e:
            print(e)

    def cerrar_sesion(self):
        self.connection.close()


bd = DataBase()
bd.traer_Datos()
bd.registrar_amigo('Paul', 168, 80, '1999-11-15', '939222888')
bd.traer_Datos()
bd.cerrar_sesion() 