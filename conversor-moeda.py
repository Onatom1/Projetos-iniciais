from tkinter import Tk, ttk
from tkinter import *

import json
import requests
import string

from PIL import ImageTk, Image,ImageOps , ImageDraw

import http.client


# --------------- Cores ---------------------- #
cor0 = "#FFFFFF"  # Brancao
cor1 = "#333333"  # Preto
cor2 = "#00a5a5"  # Verde-Azulado

# --------------- Janela ---------------------- #
root = Tk()
root.geometry('300x320')
root.title('Conversor')
root.configure(bg=cor0)

style = ttk.Style(root)
style.theme_use('clam')


# --------------- Função ---------------------- #
def converter():
    moeda_1 = combo1.get()
    moeda_2 = combo2.get()

    # Utilize a nova URL da API e a chave correspondente
    url = f"https://v6.exchangerate-api.com/v6/eaa1c82eab7d78ac11839f71/latest/{moeda_1}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Obtenha a taxa de câmbio para a moeda de destino
        taxa_cambio = data['conversion_rates'][moeda_2]
        
        # Converta o valor para a moeda de destino diretamente
        final = float(valor.get()) * taxa_cambio

        # Obtenha o símbolo da moeda de destino
        simbolo = obter_simbolo_moeda(moeda_2)
        
        currency = f"{simbolo} {final:,.2f}"
        resultado.configure(text=currency)

    except requests.exceptions.RequestException as e:
        resultado.configure(text="Erro na solicitação")

# Função para obter o símbolo da moeda
def obter_simbolo_moeda(moeda):
    # Trate os símbolos manualmente para cada moeda
    if moeda == 'USD':
        return '$'
    elif moeda == 'EUR':
        return '€'
    elif moeda == 'BRL':
        return 'R$'
    # Adicione mais moedas conforme necessário

    return ''  # Se a moeda não estiver na lista acima, retorne uma string vazia

# --------------- Frames ---------------------- #
top = Frame(root, width=300, height=60, pady=0, padx=0, bg=cor1, relief='flat')
top.grid(row=0, column=0, columnspan=2)

# LOGO
icon = Image.open('image/log.png')
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top,image=icon, compound=LEFT, text="Conversor de moeda ", height=5, pady=30, padx=13,
               relief="raised", anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor0)
app_name.place(x=0, y=0)

main = Frame(root, width=300, height=260, bg=cor0, pady=5, padx=0, relief='flat')
main.grid(row=1, column=0, sticky=NSEW)

resultado = Label(main, text='', width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'), bg='#ffffff', fg=cor1)
resultado.place(x=50, y=10)

moeda = ['BRL','EUR','USD']

app_ = Label(main,text='De', width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10  bold'), bg=cor0, fg=cor1)
app_.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8,  justify=CENTER,font=('Ivy 12 bold'))
combo1['values'] = (moeda)
combo1.place(x=50, y=115)

app_ = Label(main,text='Para', width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
app_.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo2['values'] = (moeda)
combo2.place(x=160, y=115)

valor = Entry(main, width=22,justify=CENTER, font=('Ivy 12 bold'), relief=SOLID)
valor.place(x=50, y=155)

botao = Button(main, text="Converter ", command=converter, width=19,padx=5, height=1, bg=cor2, fg=cor0,  font=('Ivy 12 bold'), relief=RAISED, overrelief=RIDGE)
botao.place(x=50, y=210)


# Rodapé --------------------------------------------------------------
rodape_label = Label(root, text='By Yury Mota', font=('Verdana 5'), bg=cor0, fg=cor2)
rodape_label.place(relx=0, rely=1.0, anchor=SW, y=2)



root.mainloop()

