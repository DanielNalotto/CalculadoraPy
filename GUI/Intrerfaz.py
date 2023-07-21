from tkinter import Tk, Entry, Button, StringVar

WIN_WIDTH = 235
WIN_HEIGHT = 300

celeste = "#CAD9FF"
azul = "#304A9B"
gris = "#515458"

btn_font = ("Times New Roman", 16, "normal")
txt_font = ("Times New Roman", 24, "normal")

class Calculadora(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
        self.resizable(False, False)
        self.title("Calculadora")
        self.iconbitmap(".\logo.gif")
        self.config(bg=azul)
        self.txt_var = StringVar()
        self.widgets()
    
    def widgets(self):
        txt_cuentas = Entry(self, readonlybackground=celeste, fg=azul, textvariable=self.txt_var, state="readonly", font=txt_font, justify='right')
        txt_cuentas.place(x=10, y=10, width=215, height=50)
        
        fila_1, fila_2, fila_3, fila_4, fila_5 = 70, 115, 160, 205, 250
        column_1, column_2, column_3, column_4 = 10, 65, 120, 175
        btn_width, btn_height = 50, 40

        # Primer fila
        self.btn1 = Button(self, font=btn_font, bg=gris, fg=celeste, text="+")
        self.btn1.place(x=column_1, y=fila_1, width = btn_width, height = btn_height)

        self.btn2 = Button(self, font=btn_font, bg=gris, fg=celeste, text="-")
        self.btn2.place(x=column_2, y=fila_1, width = btn_width, height = btn_height)

        self.btn3= Button(self, font=btn_font, bg=gris, fg=celeste, text="*")
        self.btn3.place(x=column_3, y=fila_1, width = btn_width, height = btn_height)

        self.btn3= Button(self, font=btn_font, bg=gris, fg=celeste, text="/")
        self.btn3.place(x=column_4, y=fila_1, width = btn_width, height = btn_height)


        # Segunda fila
        self.btn1 = Button(self, font=btn_font, bg=gris, fg=celeste, text="7")
        self.btn1.place(x=column_1, y=fila_2, width = btn_width, height = btn_height)

        self.btn2 = Button(self, font=btn_font, bg=gris, fg=celeste, text="8")
        self.btn2.place(x=column_2, y=fila_2, width = btn_width, height = btn_height)

        self.btn3 = Button(self, font=btn_font, bg=gris, fg=celeste, text="9")
        self.btn3.place(x=column_3, y=fila_2, width = btn_width, height = btn_height)

        self.btn4 = Button(self, font=btn_font, bg=gris, fg=celeste, text="<--")
        self.btn4.place(x=column_4, y=fila_2, width = btn_width, height = btn_height)


        # Tercer fila
        self.btn1 = Button(self, font=btn_font, bg=gris, fg=celeste, text="4")
        self.btn1.place(x=column_1, y=fila_3, width = btn_width, height = btn_height)

        self.btn2 = Button(self, font=btn_font, bg=gris, fg=celeste, text="5")
        self.btn2.place(x=column_2, y=fila_3, width = btn_width, height = btn_height)

        self.btn3 = Button(self, font=btn_font, bg=gris, fg=celeste, text="6")
        self.btn3.place(x=column_3, y=fila_3, width = btn_width, height = btn_height)

        self.btn3 = Button(self, font=btn_font, bg=gris, fg=celeste, text="Ze")
        self.btn3.place(x=column_4, y=fila_3, width = btn_width, height = btn_height)
        

        # Cuarta fila
        self.btn1 = Button(self, font=btn_font, bg=gris, fg=celeste, text="1")
        self.btn1.place(x=column_1, y=fila_4, width = btn_width, height = btn_height)

        self.btn2 = Button(self, font=btn_font, bg=gris, fg=celeste, text="2")
        self.btn2.place(x=column_2, y=fila_4, width = btn_width, height = btn_height)

        self.btn3 = Button(self, font=btn_font, bg=gris, fg=celeste, text="3")
        self.btn3.place(x=column_3, y=fila_4, width = btn_width, height = btn_height)

        self.btn3 = Button(self, font=btn_font, bg=gris, fg=celeste, text="=")
        self.btn3.place(x=column_4, y=fila_4, width = btn_width, height = btn_height*2+5)


        # Quinta fila
        self.btn1 = Button(self, font=btn_font, bg=gris, fg=celeste, text="Ans")
        self.btn1.place(x=column_1, y=fila_5, width = btn_width, height = btn_height)

        self.btn2 = Button(self, font=btn_font, bg=gris, fg=celeste, text="0")
        self.btn2.place(x=column_2, y=fila_5, width = btn_width, height = btn_height)

        self.btn3= Button(self, font=btn_font, bg=gris, fg=celeste, text=".")
        self.btn3.place(x=column_3, y=fila_5, width = btn_width, height = btn_height)


if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
