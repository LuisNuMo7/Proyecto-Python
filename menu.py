#!/usr/bin/python3
import tkinter as tk

    
app = tk.Tk()

app.geometry('600x300')
app.configure(background='lightblue')
tk.Wm.wm_title(app,'Tic Tac Toe con Python y Tkinter')


tk.Button(
    app,
    text='Nuevo Juego 3 x 3',
    font=('Courier', 14),
    bg='#00a8e8',
    fg='white',
).pack(
    fill=tk.BOTH,
    expand=True
)
tk.Button(
    app,
    text='Nuevo Juego 5 x 5',
    font=('Courier', 14),
    bg='#00a8e8',
    fg='white',
).pack(
    fill=tk.BOTH,
    expand=True
)
tk.Button(
    app,
    text='Records',
    font=('Courier', 14),
    bg='#00a8e8',
    fg='white',
).pack(
    fill=tk.BOTH,
    expand=True
)

app.mainloop()