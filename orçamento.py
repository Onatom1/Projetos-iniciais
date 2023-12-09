from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Cores
cor0 = "#2e2d2b"  # Preto
cor1 = "#feffff"  # Branco
cor2 = "#4fa882"  # Verde
cor3 = "#464242"  # Valor
cor4 = "#403d3d"  # Letra
cor5 = "#e06636"  # - Profit
cor6 = "#038cfc"  # Azul
cor7 = "#3fbfb9"  # Verde
cor8 = "#263238"  # + Verde
cor9 = "#e9edf5"  # + Verde
cor10 = "#6e8faf"
cor11 = "#f2f4f2"

# Janela
janela = Tk()
janela.title('')
janela.geometry('390x300')
janela.configure(background=cor1)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use('clam')

# Função
def calcular():
    renda_mensal = float(e_valor_quantia.get())
    
    # Obtendo as percentagens
    obter_50_porcento = (50/100) * renda_mensal
    obter_30_porcento = (30/100) * renda_mensal
    obter_20_porcento = (20/100) * renda_mensal
    
    label_necessidades['text'] = f'R${obter_50_porcento:,.2f}'
    label_quer['text'] = f'R${obter_30_porcento:,.2f}' 
    label_poupanca['text'] = f'R${obter_20_porcento:,.2f}'

# Frames
# Frame Cima --------------------------------------------------
frameCima = Frame(janela, width=300, height=50, bg=cor1, relief='flat')
frameCima.grid(row=0, column=0, columnspan=3)

# LOGO
app_label = Label(frameCima, text='Orçamento', compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 20'), bg=cor1, fg=cor4)
app_label.grid(row=0, column=0)

app_img = Image.open('image/log.png')
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=cor1, fg=cor4)
app_logo.grid(row=0, column=1)

l_linha = Label(frameCima, width=295, height=1, anchor=NW, font=('Verdana 1'), bg=cor3, fg=cor1)
l_linha.grid(row=1, column=0, columnspan=3)

# Frame Meio --------------------------------------------------
frameMeio = Frame(janela, width=300, height=90, bg=cor1, relief="solid")
frameMeio.grid(row=1, column=0, columnspan=3)

l_valor_quantia = Label(frameMeio, text='Renda Mensal?', height=1, anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_valor_quantia.grid(row=0, column=0, padx=7, pady=15)

e_valor_quantia = Entry(frameMeio, width=10, font=('Ivy 14'), justify='center', relief="solid")
e_valor_quantia.grid(row=0, column=1, pady=10)

botao_calcular = Button(frameMeio, anchor=NW, text=' Calcular'.upper(), overrelief=RIDGE, font=('Ivy 9'), bg=cor1, fg=cor0, command=calcular)
botao_calcular.grid(row=0, column=2, padx=10)

# Frame Baixo -------------------------------------------------------
frameBaixo = Frame(janela, width=300, height=200, bg=cor9, relief="raised")
frameBaixo.grid(row=2, column=0, columnspan=3, pady=10)

l_nome = Label(frameBaixo, text='Regra Orçamentária 50/30/20:', padx=10, width=35, height=1, anchor=NW, font=('Verdana 11'), bg=cor3, fg=cor1)
l_nome.grid(row=0, column=0, columnspan=3)

# Total necessidades -------------------------------------------------------
l_total_necessidades = Label(frameBaixo, text='Necessidades:', height=1, anchor=E, font=('Verdana 10'), bg=cor9, fg=cor0)
l_total_necessidades.grid(row=1, column=0, padx=10, pady=5, sticky=E)

label_necessidades = Label(frameBaixo, width=22, height=1, anchor=NW, font=('Verdana 12 '), bg=cor1, fg=cor4)
label_necessidades.grid(row=1, column=1, pady=5, sticky=W)

# Total Quer -------------------------------------------------------
l_total_quer = Label(frameBaixo, text='Gastar como quiser: ', height=1, anchor=E, font=('Verdana 10'), bg=cor9, fg=cor0)
l_total_quer.grid(row=2, column=0, padx=10, pady=5, sticky=E)

label_quer = Label(frameBaixo, width=22, height=1, anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor4)
label_quer.grid(row=2, column=1, pady=5, sticky=W)

# Total Poupança -------------------------------------------------------
l_total_poupanca = Label(frameBaixo, text='Poupança e dívida:', height=1, anchor=E, font=('Verdana 10'), bg=cor9, fg=cor0)
l_total_poupanca.grid(row=3, column=0, padx=10, pady=5, sticky=E)

label_poupanca = Label(frameBaixo, width=22, height=1, anchor=NW, font=('Verdana 12'), bg=cor1, fg=cor4)
label_poupanca.grid(row=3, column=1, pady=5, sticky=W)


# Rodapé --------------------------------------------------------------
rodape_label = Label(janela, text='By Yury Mota', font=('Verdana 8'), bg=cor1, fg=cor4)
rodape_label.place(relx=0, rely=1.0, anchor=SW, y=-5)


janela.mainloop()