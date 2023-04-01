import tkinter as tk

class Sala(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Sala")
        self.geometry("960x600")
        self.resizable(0, 0)
        self.columnconfigure(1, weight=2)
        
        self.show()

    def show(self):

        self.frame = tk.Frame(self, width=300, height=350)
        self.frame.grid(row=0, column=0)

        filas = 5
        columnas = 9
        cont = 1
        letras = 'ABCDEFGHIJKLMN'

        for i in range(filas):
            letra = tk.Label(self.frame, text=letras[i], font='Arial')
            letra.grid(row=i, column=0)
            
            for j in range(1, columnas+1):
                butaca = tk.Checkbutton(self.frame,
                                    text=f"{cont}",
                                    bd=3,
                                    font='Arial',
                                    width=3,
                                    selectcolor='yellow',
                                    indicatoron=False)
                butaca.grid(row=i, column=j, padx=5, pady=5)
                cont += 1
            letra = tk.Label(self.frame, text=letras[i], font='Arial')
            letra.grid(row=i, column=j+1)


app = Sala()
app.mainloop()