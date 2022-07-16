from func import *

class Menu:
    def __init__(self):
        opt = DBvendas()
        
        
        while True:
            entrada = input('1 - Cadastro\n2 - Listar Produtos\n3 - Buscar produto\n4 - Alterar Produto\n0 - Sair')


            if entrada == '1':
                cod = input("Insira o Código: ")
                descr = input("Insira a Descrição: ")
                fabricante = input("Insira o Fabricante: ")
                quantidade = input("Insira a Quantidade: ")
                opt.salvar_produtos(cod,descr,fabricante,quantidade)

            elif entrada == '2':
               opt.listar_produtos()

            elif entrada == '3':
               cod=input('Insira o código')
               opt.procurar(cod)
              

            elif entrada == '4':
                cod = input('Informe cod: ')
                nome = input('Novo nome do produto: ')
                atributo = 'nome' 
                opt.alterar_produto(nome,atributo,cod)
         
            elif entrada == '0':
              break

            else:
              print('erro')



