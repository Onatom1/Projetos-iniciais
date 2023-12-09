from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# --------------- Função ---------------------- #
def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get()) ** 2
    resultado = peso / altura

    if resultado < 18.6:
        l_resultado_texto['text'] = "Seu IMC é: Abaixo do peso"
    elif 18.5 <= resultado < 24.9:
        l_resultado_texto['text'] = "Seu IMC é: Normal"
    elif 25 <= resultado < 29.9:
        l_resultado_texto['text'] = "Seu IMC é: Sobrepeso"
    else:
        l_resultado_texto['text'] = "Seu IMC é: Obesidade"

    l_resultado['text'] = "{:.{}f}".format(resultado, 2)


# --------------- Cores ---------------------- #
co0 = "#444466"  # Preto
co1 = "#feffff"  # Branco
co2 = "#4065a1"  # Azul


# --------------- Janela ---------------------- #
janela = Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg=co1)

# --------------- Frames ---------------------- #
frame_cima = Frame(janela, width=295, height=50, bg=co1, pady=0, padx=0, relief="flat")
frame_cima.grid(row=0, column=0, sticky=NSEW)

# LOGO
app_img = Image.open('image/log.png')
app_img = app_img.resize((30, 30))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(janela, image=app_img, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=co1, fg=co2)
app_logo.place(x=10, y=0)


frame_baixo = Frame(janela, width=295, height=200, bg=co1, pady=0, padx=0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW)

style = ttk.Style(janela)
style.theme_use("clam")

# --------------- Config dos Frames de cima ---------------------- #
app_nome = Label(frame_cima, text="Calculadora de IMC", width=23, height=1, padx=0, relief="flat", anchor="center", font=('Ivy 16 bold'), bg=co1, fg=co0)
app_nome.place(x=0, y=2)

         #Linha: 
app_linha = Label(frame_cima, text="", width=400, height=1, padx=0, relief="flat", anchor="nw", font=('Arial', 1), bg=co2, fg=co1)
app_linha.place(x=0, y=35)

# --------------- Config dos Frames de baixo ---------------------- #
                        #Peso:
l_peso = Label(frame_baixo, text="Insira seu peso", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_peso.grid(row=0, column=0, columnspan=1, sticky=NW, pady=10, padx=3)

e_peso = Entry(frame_baixo, width=5, font=('Ivy 10 bold'), justify='center', relief=SOLID)
e_peso.grid(row=0, column=1, columnspan=1, sticky=NSEW, pady=10, padx=3)

                       #Altura:
l_altura = Label(frame_baixo, text="Insira sua altura", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_altura.grid(row=1, column=0, columnspan=1, sticky=NW, pady=10, padx=3)

e_altura = Entry(frame_baixo, width=5, font=('Ivy 10 bold'), justify='center', relief=SOLID)
e_altura.grid(row=1, column=1, columnspan=1, sticky=NSEW, pady=10, padx=3)

                    #Resultado:
l_resultado = Label(frame_baixo, width=5, text="---", height=1, padx=6, pady=12, relief="flat", anchor="center", font=('Ivy 24 bold'), bg=co2, fg=co1)
l_resultado.place(x=175, y=10)

l_resultado_texto = Label(frame_baixo, width=37, text="", height=1, padx=0, pady=12, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_resultado_texto.place(x=0, y=85)


# ------------ Botão Calcular ------------------ #
b_calcular = Button(frame_baixo, command=calcular, text="Calcular", width=34, height=1, overrelief=SOLID, bg=co2, fg="white", font=('Ivy 10 bold'), anchor="center", relief=RAISED)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)


# --------------- Loop para manter janela aberta ---------------------- #
janela.mainloop()
