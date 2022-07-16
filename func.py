import mysql.connector
from infos import *

class DBvendas:
    def __init__(self):
         self.conexao = mysql.connector.connect(host="localhost", user="root", passwd="q1w2e3", db="vendas")
         self.meu_cursor = self.conexao.cursor()

    def salvar_produtos(self,cod,descr,fabricante,quantidade):
        objproduto = Informações(cod, descr, fabricante, quantidade)
        comando_sql = f'insert into produtos ' \
                      f'(cod, descr, fabricante, quantidade) value'\
                      f'("{objproduto.cod}", "{objproduto.descr}","{objproduto.fabricante}","{objproduto.quantidade}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def listar_produtos(self):
        comando_sql = 'select * from produtos'
        self.meu_cursor.execute( comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)


    def procurar(self,cod):
        comando_sql= f'select * from produtos where cod={cod}'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print (i)
  

    def alterar_produto(self, atributo, valor, cod):
       comando_sql = f'update produtos set {atributo} = "{valor}" where id = {cod}'
       self.meu_cursor.execute(comando_sql)
       self.conexao.commit()
 