from tkinter import *
from tkinter import ttk

class APP():

    def __init__(self, window):
        self.window = window
        self.window.title('Password Manager')

        #creating frame container
        frame = LabelFrame(self.window, text = 'Register a new password')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # name input
        Label(frame, text = 'Name: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # password input
        Label(frame, text='Password: ').grid(row=2, column=0)
        self.password = Entry(frame, show='*')
        self.password.grid(row = 2, column=1)

        # button 'add password'
        ttk.Button(frame, text='Save Password').grid(row=3, columnspan=2, sticky= W + E)

        # table
        self.list = ttk.Treeview(height=10, columns=2)
        self.list.grid(row=4, column=0,columnspan=2)

    def show_passwords(self):
        self.window.destroy()
        self.shows = tk.Tk






if __name__ == '__main__':
    window = Tk()
    aplication = APP(window)
    window.mainloop()

