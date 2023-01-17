import cmd
from bd import DataBase
import getpass
from cryptography.fernet import Fernet

class PasswordManager(cmd.Cmd):
    prompt = "(---) "
    bd = DataBase()

    def do_create(self, line):
        """create passwords"""
        item = input("Item: ")
        usr = input("Username or E-mail: ")
        password = getpass.getpass("Enter your password: ")
        lenght = len(password)
        encryp_pwsd = self.encrypted(password)
        self.bd.create_password(item, usr, encryp_pwsd[0], encryp_pwsd[1], lenght) # encrypt paswd and key

    def do_all(self, line):
        self.bd.show_data()

    def encrypted(self, pswd):
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        pswd_bytes = pswd.encode()
        ciphered_pswd = cipher_suite.encrypt(pswd_bytes)
        return [ciphered_pswd, key]

    def denrcypted(self, pswd, key):
        cipher_suite = Fernet(key)
        password = cipher_suite.decrypt(pswd)
        return password


    def do_read(self, line):
        tokens = self.tokenizer(line)
        self.bd.create

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



if __name__ == '__main__':
    PasswordManager().cmdloop()
