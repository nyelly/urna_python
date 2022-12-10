from tkinter import *
from tkinter import messagebox

from sorteador import sorteador_numeros

class Aplication():
    def __init__(self, janela):
        janela.title("Aplicação tkinter")
        janela.geometry("300x300")
        self.container1 = Frame(janela)
        self.container1.grid(row=0, column=0)
        self.container2 = Frame(janela)
        self.container2.grid(row=0, column=1)
        self.container3 = Frame(janela)
        self.container3.grid(row=1, column=0)
        self.container4 = Frame(janela)
        self.container4.grid(row=1, column=0)

        self.label1 = Label(self.container1, text="Você deseja sortear 10 números?", font = 20)        
        self.label1.pack()

        self.label2 = Label(self.container1, text="")
        self.label2.pack()
       
        self.btn1 = Button(self.container3, text= "Sortear" ,command=self.mudaNumero, font=15,foreground="white", background="black")
        self.btn1.pack()

        self.btn2 = Button(self.container3, text= "Não" ,command=janela.destroy, font=15,foreground="white", background="black")
        self.btn2.pack()

    def mudaNumero(self):
        
        numeros_retornados = sorteador_numeros()
        self.label2["text"]= numeros_retornados
    

 
app = Tk()
Aplication(app)
app.mainloop()
