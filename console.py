import cmd
import getpass
from bd import DataBase
from utilities import crypto
from prettytable import PrettyTable


class PasswordManager(cmd.Cmd):
    prompt = "(---) "
    bd = DataBase()

    def do_create(self, line):
        """create passwords"""
        item = input("Item: ")
        usr = input("Username or E-mail: ")
        password = getpass.getpass("Enter your password: ")
        lenght = len(password)
        encryp_pwsd = crypto.encrypted(password)
        self.bd.create_password(item, usr, encryp_pwsd[0], encryp_pwsd[1], lenght)

    def do_all(self, line):
        data = self.bd.show_all()
        table = PrettyTable(["id", "Item", "Email/Username", "Password"])
        for item in data:
            item = self.secret_password(item)
            table.add_row(item)
        print(table)

    def do_read(self, line):
        id_item = input("Ingrese el id del item que desea descubrir: ")
        data = self.bd.read_password(id_item)
        table = PrettyTable(["Item", "Email/Username", "Password"])
        dencrypted_password = crypto.denrcypted(data[2], data[3])
        new_item = list(data[:3])
        new_item[2] = dencrypted_password
        table.add_row(new_item)
        print(table)

    def do_quit(self, line):
        """Quit command to exit the program and close connection with database."""
        self.bd.cerrar_sesion()
        return True

    def emptyline(self):
        """Ignore empty lines."""
        self.lastcmd = ''
        return cmd.Cmd.emptyline(self)

    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)

    def tokenizer(self, line):
        tokens = line.split()
        return tokens

    def secret_password(self, items):
        lenght = items[4]
        new_element = ''.join(['*' for _ in range(lenght)])
        new_items = list(items[:4])
        new_items[3] = new_element
        return new_items



if __name__ == '__main__':
    PasswordManager().cmdloop()
