from tkinter import*
from tkinter import Tk, ttk
from PIL import Image, ImageTk

# Cores
cor0 = "#2e2d2b"  # Preto
cor1 = "#feffff"  # Branco
cor2 = "#4fa882"  # Verde
cor3 = "#38576b"  # Valor
cor4 = "#403d3d"   # Çetra
cor5 = "#e06636"   # - Profit
cor6 = "#038cfc"   # Azul
cor7 = "#3fbfb9"   # Verde
cor8 = "#263238"   # + Verde
cor9 = "#e9edf5"   # + Verde
cor10 ="#6e8faf"  #
cor11 = "#f2f4f2"


# Janela
root = Tk()
root.title ("")
root.geometry('380x500')
root.configure(background=cor1)
root.resizable(width=FALSE, height=FALSE)

style = ttk.Style(root)
style.theme_use("clam")



# Função --------------------------------------------------
def calcular():
    # Obtendo os valores Ativos
    ativo_1 = e_valor_casa.get()
    ativo_2 = e_valor_imovel.get()
    ativo_3 = e_valor_veiculos.get()
    ativo_4 = e_valor_investimentos.get()
    ativo_5 = e_outros_ativos.get()
    
    # Obtendo os valores Passivos
    passivo_1 = e_valor_hipoteca.get()
    passivo_2 = e_valor_carro.get()
    passivo_3 = e_valor_estudante.get()
    passivo_4 = e_valor_dividas.get()

    # Verificando as entradas se pegaram os valores
    if ativo_1 == '' or ativo_2 == '' or ativo_3 == '' or ativo_4 == '' or ativo_5 == '' or passivo_1 == '' or passivo_2 == '' or passivo_3 == '' or passivo_4 == '':
        print('Entra algum valor')
        return
    else:
        # Calculando o valor total dos ativos
        total_ativos = float(ativo_1) + float(ativo_2) + float(ativo_3) + float(ativo_4) + float(ativo_5)
        # Calculando o valor total dos passivos
        total_passivos = float(passivo_1) + float(passivo_2) + float(passivo_3) + float(passivo_4)
        # Calculando Patrimônio línquido
        patrimonio_liquido = total_ativos - total_passivos
        
        l_resultado['text'] = f'R${patrimonio_liquido:,.2f}'

 
# Frames
# Frame Cima --------------------------------------------------
frameCima = Frame(root, width=380, height=50, bg=cor1, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2)

# Frame Baixo --------------------------------------------------
frameBaixo = Frame(root, width=380, height=400, bg=cor1, relief="flat")
frameBaixo.grid(row=2, column=0, pady=10)

frameResultado = Frame(root, width=364, height=50, bg=cor3, relief="flat")
frameResultado.grid(row=1, column=0, pady=10)

# Dividindo o Frame

frameAtivos = Frame(frameBaixo, width=180, height=370, bg=cor9, relief="flat")
frameAtivos.grid(row=0, column=0, pady=0, padx=5)

framePassivos = Frame(frameBaixo, width=180, height=370, bg=cor9, relief="flat")
framePassivos.grid(row=0, column=1, pady=0)


# LOGO
app_img = Image.open('image/log.png')
app_img = app_img.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=cor1, fg=cor4)
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text="Calculadora de patrimônio líquido", compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Ivy, 12'), bg=cor1, fg=cor4)
app_.place(x=50, y=20)

l_linha = Label(frameCima, width=380, height=1, anchor=NW, font=('Verdana 1'), bg=cor3, fg=cor1)
l_linha.place(x=0, y=47)


# Entrando Ativos -------------------------------------------------------

l_nome = Label(frameAtivos, text='Insira Ativos', padx=10, width=35, height=1, anchor=NW, font=('Verdana 11'), bg=cor2, fg=cor1)
l_nome.place(x=0, y=0)

# Valor da Casa
l_casa = Label(frameAtivos, text='Valor da Casa', height=1, anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_casa.place(x=10, y=40)

e_valor_casa = Entry(frameAtivos, width=10, font=('Ivy 12'), justify='center', relief="solid")
e_valor_casa.place(x=10, y=65)

#  Imóveis
l_imoveis = Label(frameAtivos, text='Imóveis', height=1, anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_imoveis.place(x=10, y=105)

e_valor_imovel = Entry(frameAtivos, width=10, font=('Ivy 12'), justify="center", relief="solid")
e_valor_imovel.place(x=10, y=125)

# Veículos
l_veiculos = Label(frameAtivos, text='Veículos', height=1, anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_veiculos.place(x=10, y=165)

e_valor_veiculos = Entry(frameAtivos, width=10, font=('Ivy 12'), justify="center", relief="solid")
e_valor_veiculos.place(x=10, y=195)

# Investimentos e Poupança
l_investimentos = Label(frameAtivos, text='Investimentos', height=1, anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_investimentos.place(x=10, y=230)

e_valor_investimentos = Entry(frameAtivos, width=10, font=('Ivy 12'), justify="center", relief="solid")
e_valor_investimentos.place(x=10, y=255)

# Outros Ativos
l_ativos = Label(frameAtivos, text='Outros Ativos', height=1, anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_ativos.place(x=10, y=295)

e_outros_ativos = Entry(frameAtivos, width=10, font=('Ivy 12'), justify="center", relief="solid")
e_outros_ativos.place(x=10, y=315)


# Entrando Passivos -------------------------------------------------------
l_nome = Label(framePassivos, text='Insira Passivos', padx=10, width=35, height=1, anchor=NW, font=('Verdana 11'), bg=cor5, fg=cor1)
l_nome.place(x=0, y=0)

# Hipoteca
l_hipoteca = Label(framePassivos, text='Hipoteca', height=1, anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_hipoteca.place(x=10, y=40)

e_valor_hipoteca = Entry(framePassivos, width=10, font=('Ivy 12'), justify="center", relief="solid")
e_valor_hipoteca.place(x=10, y=65)

# Empréstimos de Carro
l_carro = Label(framePassivos, text='Empréstimos de Carro', height=1, anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_carro.place(x=10, y=105)

e_valor_carro = Entry(framePassivos, width=10, font=('Ivy 12'), justify="center", relief="solid")
e_valor_carro.place(x=10, y=125)

# Empréstimos Estudantis
l_estudante = Label(framePassivos, text="Empréstimos Estudantis", height=1,anchor=E, font=('Verdana 9 '), bg=cor9, fg=cor0)
l_estudante.place(x=10, y=165)

e_valor_estudante = Entry(framePassivos, width=10, font=('Ivy 12'), justify="center", relief="solid")
e_valor_estudante.place(x=10, y=195)

# Outras dívidas
l_dividas = Label(framePassivos, text="Outras dívidas", height=1,anchor=E, font=('Verdana 9 '), bg=cor9, fg=cor0)
l_dividas.place(x=10, y=230)

e_valor_dividas = Entry(framePassivos, width=10, font=('Ivy 12'), justify="center", relief="solid")
e_valor_dividas.place(x=10, y=255)

# Resultado -------------------------------------------------------
l_resultado = Label(frameResultado, text='R${:,.2f}'.format(00),padx=10, width=15, height=1,anchor=NE, font=('Verdana 25 bold'), bg=cor3, fg=cor1)
l_resultado.place(x=0, y=7)


botao_calcular = Button(framePassivos,command=calcular, width=12, anchor=CENTER, text=" Calcular".upper(), overrelief=RIDGE,  font=('ivy 9 bold '),bg=cor1, fg=cor0 )
botao_calcular.place(x=10, y=310)

# Rodapé --------------------------------------------------------------
rodape_label = Label(root, text='By Yury Mota', font=('Verdana 8'), bg=cor1, fg=cor4)
rodape_label.place(relx=0, rely=1.0, anchor=SW, y=-5)


root.mainloop()