from tkinter import Tk, Frame, Entry, Button, StringVar, messagebox

# --- Constantes ---
calc_size=[228, 304]
color=["#222", "#444", "#5af", "#555", "#acf", "#137"]
my_font=("Times New Roman", 14, 'normal')

def but_style_config2(but, parent, com, txt, rowNum, colNum, h=None, rspan=None):
    if h==None:
        h=2
    if rspan==None:
        rspan=1
    but = Button(parent, command=com, bg=color[1], fg=color[2], activebackground=color[3], activeforeground=color[4], width=3, height=h, text=txt)
    but.grid(row=rowNum, column=colNum, padx=2, pady=2, rowspan=rspan)


class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent=parent
        self.calc_text=StringVar()
        self.ans=""
        self.GUI()

    # --- Interfaz ---
    def GUI(self):
        f=Frame(self.parent, bg=color[0])
        f.place(x=2, y=2)

        # ---------------- First row ----------------
        e=Entry(f, state='readonly', bg=color[5] , fg=color[2], width=23, textvariable=self.calc_text, justify='right', font=my_font)
        e.grid(row=0, column=0, columnspan=4, padx=2, pady=4, ipady=2)

        # ---------------- Second row ----------------
        but_style_config2("b_add", f, lambda:self.write_on_calc("+"), "+", 1, 0) #Addition
        but_style_config2("b_sub", f, lambda:self.write_on_calc("-"), "-", 1, 1) #Substraction
        but_style_config2("b_mul", f, lambda:self.write_on_calc("*"), "*", 1, 2) #Multiplication
        but_style_config2("b_div", f, lambda:self.write_on_calc("/"), "/", 1, 3) #Divition

        # ---------------- Third row ----------------
        but_style_config2("b_7", f, lambda:self.write_on_calc(7), "7", 2, 0) #Number button 7
        but_style_config2("b_8", f, lambda:self.write_on_calc(8), "8", 2, 1) #Number button 8
        but_style_config2("b_9", f, lambda:self.write_on_calc(9), "9", 2, 2) #Number button 9
        but_style_config2("b_back", f, lambda:self.delete_last_char(), "<--", 2, 3) #Erase last simbol

        # ---------------- Fourth row ----------------
        but_style_config2("b_4", f, lambda:self.write_on_calc(4), "4", 3, 0) #Number button 4
        but_style_config2("b_5", f, lambda:self.write_on_calc(5), "5", 3, 1) #Number button 5
        but_style_config2("b_6", f, lambda:self.write_on_calc(6), "6", 3, 2) #Number button 6
        but_style_config2("b_Ze", f, lambda:self.erase(), "Ze", 3, 3) #Reset calculator

        # ---------------- Fifth row ----------------
        but_style_config2("b_1", f, lambda:self.write_on_calc(1), "1", 4, 0) #Number button 1
        but_style_config2("b_2", f, lambda:self.write_on_calc(2), "2", 4, 1) #Number button 2
        but_style_config2("b_3", f, lambda:self.write_on_calc(3), "3", 4, 2) #Number button 3
        but_style_config2("b_eq", f, lambda:self.equal(), "=", 4, 3, 5, 2) #Equal button

        # ---------------- Sixth row ----------------
        but_style_config2("b_ans", f, lambda:self.answer(), "Ans", 5, 0) #Last answer
        but_style_config2("b_0", f, lambda:self.write_on_calc(0), "0", 5, 1) #Number button 0
        but_style_config2("b_dot", f, lambda:self.write_on_calc("."), ".", 5, 2) #Dot button

    # ------------ SCREEN CONFIGURATION --------------
    def write_on_calc(self, dig):
        count=self.calc_text.get()+str(dig)

        #Evalua si los digitos ingresados son operables
        try:
            eval(count)
            self.calc_text.set(count)
        except:
            ld=count[-2]
            # No deja escribir mas de un cero
            if dig=="0" and ld!="0":
                print(f"dig: {dig}\nld: {ld}")
                self.calc_text.set(count)

            #No deja duplicar operadores
            if dig=="+" or dig=="-" or dig=="*" or dig=="/":
                if ld!="+" and ld!="-" and ld!="*" and ld!="/" and ld!=".":
                    self.calc_text.set(count)
            
    def erase(self):
        self.calc_text.set("")

    def delete_last_char(self):
        t=self.calc_text.get()
        t=t[:-1]
        self.calc_text.set(t)

    def equal(self):
        t=self.calc_text.get()
        try:
            self.ans=eval(t)
            if self.ans%1==0.0:
                self.ans=int(self.ans)
            self.calc_text.set(self.ans)
        except:
            messagebox.showerror('Calculator','Impossible operation.')

    def answer(self):
        self.write_on_calc(self.ans)

if __name__=="__main__":
    root=Tk()
    root.geometry(f"{calc_size[0]}x{calc_size[1]}")
    root.resizable(False, False)
    root.title("Calculator")
    root.config(bg=color[5])
    app=Calculator(root)
    app.mainloop()