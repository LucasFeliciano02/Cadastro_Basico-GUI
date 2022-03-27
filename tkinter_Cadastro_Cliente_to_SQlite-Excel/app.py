"""
pip3 install --upgrade tensorflow-gpu --user  =  caso der erro de nao reconhecer o pandas ou ipython

https://www.w3schools.com/colors/colors_picker.asp  =  App de escolher cor
https://iconarchive.com/  =  baixar icones que vao do lado do nome do app
"""

import tkinter as tk
from tkinter import messagebox
import sqlite3
import pandas as pd


# * CRIANDO O BANCO DE DADOS SQLITE, COMENTAR TUDO, POIS AO RODAR ELE VAI CRIAR MAIS UM BANCO DE DADOS DO MESMO (CRIA E COMENTA)


# conexao = sqlite3.connect('cadastro_clientes.db')

# c = conexao.cursor()

# c.execute(''' CREATE TABLE clientes (
#     nome text,
#     sobrenome text,
#     email text,
#     telefone text
#     )
# ''')

# conexao.commit()

# conexao.close()


# * Função de Botoes: 'cadastrar_cliente'; enviando para o sqlite e 'exporta_clientes'; enviando com pandas para excel

def validar(entradas):
    for entrada in entradas.keys():
        if not(entradas[entrada]):
            messagebox.showerror(
                'Erro', f'Preencha corretamente o campo {entrada}!')
            return False
    return True


def cadastrar_cliente():
    conexao = sqlite3.connect('cadastro_clientes.db')

    c = conexao.cursor()
    form = {
        'nome': entry_nome.get(),
        'sobrenome': entry_sobrenome.get(),
        'email': entry_email.get(),
        'telefone': entry_telefone.get()
    }

    if validar(form):
        c.execute(
            "INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)", form)
        conexao.commit()

    conexao.close()

    # Reseta a visulização ao cadastrar o cliente
    entry_nome.delete(0, "end")
    entry_sobrenome.delete(0, "end")
    entry_email.delete(0, "end")
    entry_telefone.delete(0, "end")


def exporta_clientes():
    conexao = sqlite3.connect('cadastro_clientes.db')

    c = conexao.cursor()

    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=[
                                        'nome', 'sobrenome', 'email', 'telefone', 'id_banco'])
    clientes_cadastrados.to_excel('banco_clientes.xlsx')
    conexao.commit()

    conexao.close()


# * CRIANDO A INTERFACE GRÁFICA
janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela.iconbitmap('cadastro_db_icon.ico')  # imagem do app
janela['bg'] = '#d9d9d9'  # =  COR  |  #aaaaaa  =  cinza claro
janela.resizable(width=False, height=False)  # Bloquia a tela cheia e deixa como nao redirecionamento


# * Labels:  (nomes e onde ficam)

label_nome = tk.Label(janela, text='Nome:', font='times', bg='#d9d9d9')  # bg/fg='black'  |  font='verdana/arial/times 20 bold italic'
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome:', font='times', bg='#d9d9d9')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail:', font='times', bg='#d9d9d9')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone:', font='times', bg='#d9d9d9')
label_telefone.grid(row=3, column=0, padx=10, pady=10)


# * Entrys:   (campo de pesquisa)

entry_nome = tk.Entry(janela, text='Nome', width=29)
entry_nome.grid(row=0, column=1, padx=15, pady=10)

entry_sobrenome = tk.Entry(janela, text='Sobrenome', width=29)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, text='E-mail', width=29)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, text='Telefone', width=29)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)


# * Botões:

botao_cadastrar = tk.Button(
    janela, text='Cadastrar Cliente', command=cadastrar_cliente, font='times')
botao_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

botao_exportar = tk.Button(
    janela, text='Exportar para Excell', command=exporta_clientes, font='times')
botao_exportar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)


# * Centralizando o arquivo

# Dimensoes da janela
largura = 320
altura = 290

# Resolução do nosso sistema
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenwidth()
# print(largura_screen, altura_screen)  # para saber as dimensoes do monitor


# Posição da janela
posx = largura_screen/2 - largura/1.8
posy = altura_screen/5 - altura/5

# Definir a geometria
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


janela.mainloop()
