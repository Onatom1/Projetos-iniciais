from tkinter import *
import tkinter
from datetime import datetime
import pyglet
from PIL import Image, ImageTk

#Adiciona a fonte digital-7
pyglet.font.add_file('fonts/digital-7.ttf')



cor1 = "#DE7B7B"  #Preto
cor2 = "#fafcff"  #Branco
cor3 = "#21c25c"  #Verde
cor4 = "#eb463b"  #Vermelho
cor5 = "#dedcdc"  #Cinza
cor6 = "#3080f0"  #Azul

fundo = cor1 #Background
cor = cor2 #Fonte

janela = Tk()
janela.title("")
janela.geometry('320x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=fundo)

# --------------- Dicionários para Tradução ---------------------- #
meses_pt = {
    'Jan': 'Jan',
    'Feb': 'Fev',
    'Mar': 'Mar',
    'Apr': 'Abr',
    'May': 'Mai',
    'Jun': 'Jun',
    'Jul': 'Jul',
    'Aug': 'Ago',
    'Sep': 'Set',
    'Oct': 'Out',
    'Nov': 'Nov',
    'Dec': 'Dez'
}

dias_semana_pt = {
    'Monday': 'Segunda',
    'Tuesday': 'Terça',
    'Wednesday': 'Quarta',
    'Thursday': 'Quinta',
    'Friday': 'Sexta',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}


# --------------- Função ---------------------- #
def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = dias_semana_pt[tempo.strftime("%A")]
    dia = tempo.day
    mes = meses_pt[tempo.strftime("%b")]
    ano = tempo.strftime("%Y")
    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + "   " + str(dia) + "/" + mes + "/" + ano)


# --------------- Label ---------------------- #
l1 = Label(janela, text="10:05:05", font=('digital-7',  80), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela,  font=('Arial',  20), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

# LOGO
app_img = Image.open('image/log.png')
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(janela, image=app_img, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=cor1, fg=cor4)
app_logo.place(x=270, y=115)

# Rodapé --------------------------------------------------------------
rodape_label = Label(janela, text='By Yury Mota', font=('Verdana 8'), bg=cor1, fg=cor2)
rodape_label.place(relx=0, rely=1.0, anchor=SW, y=-5)

#Executar
relogio()
janela.mainloop()
