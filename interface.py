from tkinter import *
from func import *


root = Tk()
fr1 = Frame(root)
fr2 = Frame(root)
fr3 = Frame(root)
fr4 = Frame(root)
fr5 = Frame(root)
fr6 = Frame(root)
fr7 = Frame(root)

#   Geometry

root.geometry('300x250')

funct = DBvendas()


def salvarProduto() :
    cod = ent1_1.get()
    descr = ent2_1.get()
    quantidade = ent3_1.get()
    fabricante = ent4_1.get()
    funct.salvar_produtos(cod, descr, fabricante, quantidade)

def listar():
    atributo = 'produtos'
    list1= funct.listar_produtos(atributo)
    for i in list1:
        lb1_3['text'] += 'Cod: ' + str(i[0]) + ' ' + 'Prod: ' +str(i[1]) + '\n'
    return list1


def procurar():
    cod = lb2.get()
    list1= funct.procurar(cod)
    for i in list1:
        lb3['text'] += str(i[0]) +  str(i[1]) + '\n'

def alterar():
    cod = lb2.get()
    nome = lb4.get()
    atributo = lb6.get()
    funct.alterar_produto(atributo, nome, cod)





root.grid_rowconfigure(0,  weight=1)
root.grid_rowconfigure(1,  weight=1)
root.grid_rowconfigure(2,  weight=1)
root.grid_rowconfigure(3,  weight=1)
root.grid_rowconfigure(5,  weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
fr1.grid(row=1, column=0, sticky=NSEW)

#   Frame 1

lb1 = Label(fr1, text='Interface', font="Calibri 16", pady=20)
bt1 = Button(fr1, text='Cadastrar produto', command = lambda: [fr1.grid_remove(), fr2.grid(row=0, column=1), fr7.grid(row=6, column=1)])
bt2 = Button(fr1, text='Listar produto', command = lambda: [fr1.grid_remove(), fr5.grid(row=0, column=1), fr7.grid(row=6, column=2)])
bt3 = Button(fr1, text='Atualizar descrição', command = lambda: [fr1.grid_remove(), fr6.grid(row=0, column=1), fr7.grid(row=6, column=1)])
bt4 = Button(fr1, text='Procurar Produto', command = lambda: [fr1.grid_remove(), fr5.grid(row=0, column=1), fr7.grid(row=6, column=1)])
bt6 = Button(fr1, text='Sair', command = root.destroy)


#   Widgets 1

lb1.grid(row=0, column=2, sticky=EW)
bt1.grid(row=1, column=1, sticky=NSEW)
bt2.grid(row=2, column=1, sticky=NSEW)
bt3.grid(row=1, column=3, sticky=NSEW)
bt4.grid(row=2, column=3, sticky=NSEW)
bt6.grid(row=5, column=2, sticky=NSEW)

#   Frame 2

bt1 = Button(fr2, text='Cadastrar Produto', command = lambda: [fr2.grid_remove(), fr3.grid(row=0, column=1)])
bt1.grid(row=1, column=1, sticky=NSEW)


#   Frame 3

lb1 = Label(fr3, text='Produto')
lb2 = Label(fr3, text='Cod: ')
lb3 = Label(fr3, text='descr: ')
lb4 = Label(fr3, text='fabricante: ')
lb5 = Label(fr3, text='quantidade: ')
ent1_1 = Entry(fr3, text='') 
ent2_1 = Entry(fr3, text='')
ent3_1 = Entry(fr3, text='')
ent4_1 = Entry(fr3, text='')
bt1 = Button(fr3, text='Salvar', command= salvarProduto)



#   Widgets 3

lb1.grid(row=2, column=2, sticky=NSEW)
lb2.grid(row=3, column=1, sticky=NSEW)
ent1_1.grid(row=3, column=2, sticky=NSEW)
lb3.grid(row=4, column=1, sticky=NSEW)
ent2_1.grid(row=4, column=2, sticky=NSEW)
lb4.grid(row=5, column=1, sticky=NSEW)
ent3_1.grid(row=5, column=2, sticky=NSEW)
lb5.grid(row=6, column=1, sticky=NSEW)
ent4_1.grid(row=6, column=2, sticky=NSEW)
bt1.grid(row=7, column=1, sticky=NSEW)


#   Frame 4

lb1_3 = Label(fr4, text='')
bt1 = Button(fr4, text='Listar Produtos', command= listar)


#   Widgets 4

bt1.grid(row=1, column=1, sticky=NSEW)
lb1_3.grid(row=3, column=1, sticky=NSEW)


#   Frame 5

lb1 = Label(fr5, text='Informe o Cod ')
lb2 = Entry(fr5, text='')
lb3 = Label(fr5, text='')
bt1 = Button(fr5, text='Buscar', command= procurar)


#   Widgets 5

bt1.grid(row=3, column=1, sticky=NSEW)
lb1.grid(row=1, column=1, sticky=NSEW)
lb2.grid(row=1, column=2, sticky=NSEW)
lb3.grid(row=2, column=2, sticky=NSEW)

#   Frame 6

lb1 = Label(fr6, text='Informe o Código: ')
lb2 = Entry(fr6, text='')
lb3 = Label(fr6, text='Novas Informações: ')
lb4 = Entry(fr6, text='')
lb5 = Label(fr6, text='Local da mudança: ')
lb6 = Entry(fr6, text='')
bt1 = Button(fr6, text='Alterar', command= alterar)


#   Widgets 6

bt1.grid(row=5, column=1, sticky=NSEW)
lb1.grid(row=1, column=1, sticky=NSEW)
lb2.grid(row=1, column=2, sticky=NSEW)
lb3.grid(row=2, column=1, sticky=NSEW)
lb4.grid(row=2, column=2, sticky=NSEW)
lb5.grid(row=3, column=1, sticky=NSEW)
lb6.grid(row=3, column=2, sticky=NSEW)

#   Frame 7

bt1 = Button(fr7, text='Voltar', command= lambda: [fr2.grid_remove(), fr1.grid(row=0, column=1),fr3.grid_remove(), fr4.grid_remove(), fr5.grid_remove(),fr6.grid_remove(),fr7.grid_remove(),fr8.grid_remove(),fr9.grid_remove()])


#   Widgets 7

bt1.grid(row=1, column=0, sticky=NSEW)

#   Rodar

root.mainloop()