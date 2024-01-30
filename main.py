from tkinter import *
from tkinter import ttk


bg_primary = '#003566'
bg_secondary = '#ffc300'
bg_display = '#001d3d'
text_primary = '#fff'


janela = Tk()
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg=bg_primary)

# Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=bg_display)
frame_tela.grid(row=0, column=0)

frame_body = Frame(janela, width=235, height=268)
frame_body.grid(row=1, column=0)

# Variavel que armzena todos valores
todos_valores = ''

valor_display = StringVar()

# Função inserção no display


def entrada_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    # Inserindo valor na tela
    valor_display.set(todos_valores)


def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_display.set(str(resultado))


def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_display.set('')


# Criando label
app_label = Label(frame_tela, textvariable=valor_display, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=(
    'Helvetica 18'), bg=bg_display, fg=text_primary)
app_label.place(x=0, y=0)

# Criando os botões

# Primeira linha
b_C = Button(frame_body, command=limpar_tela, text='C', width=11, height=2, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_C.place(x=0, y=0)

b_2 = Button(frame_body, command=lambda: entrada_valores('%'), text='%', width=5, height=2, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_body, command=lambda: entrada_valores('/'), text='/', width=5, height=2, bg=bg_secondary, fg=text_primary, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

# Segunda Linha
b_4 = Button(frame_body, command=lambda: entrada_valores('7'), text='7', width=5, height=2, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_body, command=lambda: entrada_valores('8'), text='8', width=5, height=2, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(frame_body, command=lambda: entrada_valores('9'), text='9', width=5, height=2, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_body, command=lambda: entrada_valores('*'), text='*', width=5, height=2, bg=bg_secondary, fg=text_primary, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

# Terceira Linha
b_8 = Button(frame_body, command=lambda: entrada_valores('4'), text='4', width=5, height=2, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frame_body, command=lambda: entrada_valores('5'), text='5', width=5, height=2, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)

b_10 = Button(frame_body, command=lambda: entrada_valores('6'), text='6', width=5, height=2, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)

b_11 = Button(frame_body, command=lambda: entrada_valores('-'), text='-', width=5, height=2, bg=bg_secondary, fg=text_primary, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

# Quarta Linha
b_12 = Button(frame_body, command=lambda: entrada_valores('1'), text='1', width=5, height=2, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_body, command=lambda: entrada_valores('2'), text='2', width=5, height=2, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14 = Button(frame_body, command=lambda: entrada_valores('3'), text='3', width=5, height=2, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15 = Button(frame_body, command=lambda: entrada_valores('+'), text='+', width=5, height=2, bg=bg_secondary, fg=text_primary, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

# Ultima linha
b_C = Button(frame_body, command=lambda: entrada_valores('0'), text='0', width=11, height=2, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_C.place(x=0, y=208)
b_2 = Button(frame_body, command=lambda: entrada_valores('.'), text='.', width=5, height=2, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=208)

b_3 = Button(frame_body, command=calcular, text='=', width=5, height=2, bg=bg_secondary, fg=text_primary, font=(
    'Helvetica 12 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=208)

janela.mainloop()
