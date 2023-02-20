#!/usr/bin/python3
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=600, height=600)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.newgame3 = tk.Button(
                            self,
                            text='Nuevo Juego 3 x 3',
                            font=('Courier', 14),
                            bg='#00a8e8',
                            fg='white',
                        ).pack(
                            fill=tk.BOTH,
                            expand=True)
        self.newgame5 = tk.Button(
                            self,
                            text='Nuevo Juego 5 x 5',
                            font=('Courier', 14),
                            bg='#00a8e8',
                            fg='white',
                        ).pack(
                            fill=tk.BOTH,
                            expand=True)
        self.resultados = tk.Button(
                            self,
                            text='Resultados',
                            font=('Courier', 14),
                            bg='#00a8e8',
                            fg='white',
                            command=self.abrir_resultados
                        ).pack(
                            fill=tk.BOTH,
                            expand=True)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def abrir_resultados(self):
        self.win = tk.Toplevel()
        self.win.geometry('400x400')
        self.salir = tk.Button(self.win, text="QUIT", fg="red",
                               command=self.win.destroy)
        self.salir.pack(side="bottom")


root = tk.Tk()
root.wm_title('Tic Tac Toe con Python y Tkinter')
app = Application(master=root)
app.mainloop()
