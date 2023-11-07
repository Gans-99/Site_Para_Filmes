'''
                        TRABALHO EM EQUIPE DE FUNDAMENTOS DE PROGRAMAÇÃO

                                        EQUIPE:
                                        Alexsandro Martins
                                        Ciro Coimbra
                                        Lígia Sufia 
                                        Luana Cristina
                                        Mahatma Gandhi

'''

from tkinter import *

# JANELA PRINCIPAL
menu_inicial = Tk()
menu_inicial.title('DISK CINE')
menu_inicial.geometry('1020x600+130+130')
menu_inicial.resizable(False, False)
menu_inicial['bg'] = 'black'

# TITULO
l_tit = Label(menu_inicial, text=(f"{39 * ' '} DISKCINE {40 * ' '}\n\n\n\n"), anchor=NE, font=('impact 40 bold italic'),
              bg="lightblue")
l_tit.place(x=5, y=5)

nameUser = StringVar()
senhaMestre = StringVar() #Luana e Sufia
name = StringVar()  # Sufia e Luana
senhaAdm = StringVar()  # Sufia e Luana
nome_do_filme = StringVar()  # Sufia e Luana
data_do_filme = StringVar()  # Sufia e Luana
sinopse_do_filme = StringVar()  # Sufia e Luana
codigo_filme_a_ser_deletado = IntVar()  # Sufia e Luana
disponibilidade_do_filme = StringVar()  # Sufia e Luana
codigo_filme = IntVar()  # Mahatma e Ciro


def inicio():
    tela_inicial = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_inicial.place(x=70, y=90, width=880, height=490)
    bemvindo = Label(tela_inicial, text='\nBEM-VINDO!\n SELECIONE O TIPO DE USUARIO: ', anchor=NE,
                     font=('solid 18 bold'))
    bemvindo.pack()
    usuario = Button(tela_inicial, text='COMUM', bord=5, font=('solid', 12, 'bold'), command=frame_usuario)
    usuario.place(x=380, y=180)
    administrador = Button(tela_inicial, text='ADMINISTRADOR', bord=5, font=('solid', 12, 'bold'),
                           command=frame_senha_adm)
    administrador.place(x=342, y=230)


def inserir_filmes():
    frame_inserir = Frame(menu_inicial, borderwidth=5, relief='solid')
    frame_inserir.place(x=72, y=90, width=875, height=490)
    inserir = Label(frame_inserir, text='\nSELECIONE O GÊNERO \nQUE DESEJA INSERIR O FILME', anchor=NE,
                    font=('solid 18 bold'))
    inserir.pack()
    acao = Button(frame_inserir, text='  AÇÃO  ', borderwidth=5, font=('solid 12 bold'), command=inserirFilmeAcao)
    acao.place(x=230, y=140)
    ficcao = Button(frame_inserir, text='FICÇÃO', borderwidth=5, font=('solid 12 bold'), command=inserirFilmeFiccao)
    ficcao.place(x=550, y=140)
    comedia = Button(frame_inserir, text='COMÉDIA', borderwidth=5, font=('solid 12 bold'), command=inserirFilmeComedia)
    comedia.place(x=80, y=220)
    romance = Button(frame_inserir, text='ROMANCE', borderwidth=5, font=('solid 12 bold'), command=inserirFilmeRomance)
    romance.place(x=380, y=220)
    animacao = Button(frame_inserir, text='ANIMAÇÃO', borderwidth=5, font=('solid 12 bold'),
                      command=inserirFilmeAnimacao)
    animacao.place(x=690, y=220)
    terror = Button(frame_inserir, text='TERROR', borderwidth=5, font=('solid 12 bold'), command=inserirFilmeTerror)
    terror.place(x=230, y=310)
    documentarios = Button(frame_inserir, text='DOCUMENTÁRIOS', borderwidth=5, font=('solid 12 bold'),
                           command=inserirFilmeDocumentario)
    documentarios.place(x=510, y=310)
    voltar = Button(frame_inserir, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)

def loginAdm():
    frame_senha = Frame(menu_inicial, borderwidth=5, relief='solid')
    frame_senha.place(x=72, y=90, width=875, height=490)

    login_sistema = Label(frame_senha,text='FAÇA O LOGIN PARA ACESSAR O SISTEMA',anchor=NE,font=('solid 18 bold'))
    login_sistema.pack()

    login = Label(frame_senha,text='LOGIN',anchor=NE,font=('solid 18 bold'))
    login.place(x=380, y=140)

    usuario_label = Label(frame_senha, text='USUÁRIO:', anchor=NE, font=('solid 12 bold'))
    usuario_label.place(x=230, y=210)
    usuario_input = Entry(frame_senha,textvariable=nameUser,font=('solid', 18, 'normal'))
    usuario_input.place(x=320, y=210)
    senha_label = Label(frame_senha, text='SENHA:', anchor=NE, font=('solid 12 bold'))
    senha_label.place(x=230, y=280)
    senha_input = Entry(frame_senha,textvariable=senhaAdm,font=('solid', 18, 'normal'),show='*')
    senha_input.place(x=320, y=280)

    acessar = Button(frame_senha,text='ENTRAR',borderwidth=5,font=('solid', 12, 'bold'),command=acessado_adm)
    acessar.place(x=380, y=350)
    voltar = Button(frame_senha,text='VOLTAR', borderwidth=5,font=('normal, 12'),command=frame_senha_adm)
    voltar.place(x=750, y=430)

def checaSenhaADM(nameUser, senhaAdm):
    abrir = open("Arquivos/senhaadministrador.txt", "r")
    listarArquivo = abrir.readlines()
    for linha in range(len(listarArquivo)):
        linhaUser = listarArquivo[linha].split(";")
        for index in linhaUser:
            nomeUser = index.split("|")[0]
            senha = index.split("|")[1]

            if nomeUser == nameUser and senha == senhaAdm:
                return True

        return Label(menu_inicial, text="Senha ou usuário incorretos", font=('normal', 12, 'bold')).place(x=380,y=350)


def acessado_adm():
    if checaSenhaADM(nameUser.get(), senhaAdm.get()):
        frame_adm = Frame(menu_inicial, borderwidth=5, relief='solid')
        frame_adm.place(x=72, y=90, width=875, height=490)
        acessado = Label(frame_adm, text='\nSESSÃO DO ADMINISTRADOR', anchor=NE, font=('solid 18 bold'))
        acessado.pack()
        inserir = Button(frame_adm, text='INSERIR FILMES', bord=5, font=('solid', 12, 'bold'), command=inserir_filmes)
        inserir.place(x=348, y=180)
        listar = Button(frame_adm, text='LISTAR FILMES', bord=5, font=('solid', 12, 'bold'), command=frame_usuario)
        listar.place(x=352, y=240)
        apagar = Button(frame_adm, text='APAGAR FILMES', bord=5, font=('solid', 12, 'bold'), command=frame_deleta_filme)
        apagar.place(x=352, y=300)
        menu = Button(frame_adm, text='VOLTAR', bord=5, font=('normal', 12), command=frame_senha_adm)
        menu.place(x=750, y=430)


def loginCadastrar():
    frame_senha = Frame(menu_inicial, borderwidth=5, relief='solid')
    frame_senha.place(x=72, y=90, width=875, height=490)

    login_sistema = Label(frame_senha,text='FAÇA O SEU CADASTRADO',anchor=NE,font=('solid 18 bold'))
    login_sistema.pack()

    login = Label(frame_senha,text='NOVO CADASTRO',anchor=NE,font=('solid 18 bold'))
    login.place(x=350, y=100)

    senha_label = Label(frame_senha, text='SENHA PADRÃO:', anchor=NE, font=('solid 12 bold'))
    senha_label.place(x=200, y=140)
    senha_input = Entry(frame_senha,textvariable=senhaMestre,font=('solid', 18, 'normal'),show='*')
    senha_input.place(x=340, y=140)

    usuario_label = Label(frame_senha, text='NOVO USUÁRIO:', anchor=NE, font=('solid 12 bold'))
    usuario_label.place(x=200, y=210)
    usuario_input = Entry(frame_senha,textvariable=nameUser,font=('solid', 18, 'normal'))
    usuario_input.place(x=340, y=210)
    senha_label = Label(frame_senha, text='NOVA SENHA:', anchor=NE, font=('solid 12 bold'))
    senha_label.place(x=200, y=280)
    senha_input = Entry(frame_senha,textvariable=senhaAdm,font=('solid', 18, 'normal'),show='*')
    senha_input.place(x=340, y=280)

    acessar = Button(frame_senha,text='CADASTRAR',borderwidth=5,font=('solid', 12, 'bold'),command=checar_senha_padrao)
    acessar.place(x=380, y=350)
    voltar = Button(frame_senha,text='VOLTAR',borderwidth=5,font=('normal, 12'),command=frame_senha_adm)
    voltar.place(x=750, y=430)


def checar_senha_padrao():
    senhaPadrao = '3035'
    if senhaPadrao == senhaMestre.get():
        f = open("Arquivos/senhaadministrador.txt", "a")
        f.write(
            f";{nameUser.get()}|{senhaAdm.get()}"
        )
        f.close()
        return frame_senha_adm()

    else:
        return False


def frame_senha_adm():
    frame_senha = Frame(menu_inicial, borderwidth=5, relief='solid')
    frame_senha.place(x=72, y=90, width=875, height=490)
    bemvindo = Label(frame_senha,text='\nBEM-VINDO!\nSESSÃO DO ADMINISTRADOR',anchor=NE,font=('solid 18 bold'))
    bemvindo.pack()
    padrao = Label(frame_senha,text='Escolha uma das opções abaixo:',anchor=NE,font=('solid 14 bold'))
    padrao.place(x=270, y=170)
    acessar = Button(frame_senha,text='LOGIN',borderwidth=5,font=('solid', 12, 'bold'),command=loginAdm)
    acessar.place(x=380, y=220)
    cadastrar = Button(frame_senha,text='CADASTRAR NOVO USUÁRIO',borderwidth=5,font=('solid', 12, 'bold'),command=loginCadastrar)
    cadastrar.place(x=300, y=270)
    voltar = Button(frame_senha,text='VOLTAR',borderwidth=5,font=('normal, 12'),command=inicio)
    voltar.place(x=750, y=430)


def frame_deleta_filme():
    frame_deleta = Frame(menu_inicial, borderwidth=5, relief='solid')
    frame_deleta.place(x=72, y=90, width=875, height=490)
    deletar = Label(frame_deleta, text='\nSELECIONE O GÊNERO \nQUE DESEJA DELETAR O FILME', anchor=NE,
                    font=('solid 18 bold'))
    deletar.pack()
    deletar_acao = Button(frame_deleta, text='  AÇÃO  ', borderwidth=5, font=('solid 12 bold'),
                          command=deletarFilmeAcao)
    deletar_acao.place(x=230, y=140)
    deletar_ficcao = Button(frame_deleta, text='FICÇÃO', borderwidth=5, font=('solid 12 bold'),
                            command=deletarFilmeFiccao)
    deletar_ficcao.place(x=550, y=140)
    deletar_comedia = Button(frame_deleta, text='COMÉDIA', borderwidth=5, font=('solid 12 bold'),
                             command=deletarFilmeComedia)
    deletar_comedia.place(x=80, y=220)
    deletar_romance = Button(frame_deleta, text='ROMANCE', borderwidth=5, font=('solid 12 bold'),
                             command=deletarFilmeRomance)
    deletar_romance.place(x=380, y=220)
    deletar_animacao = Button(frame_deleta, text='ANIMAÇÃO', borderwidth=5, font=('solid 12 bold'),
                              command=deletarFilmeAnimacao)
    deletar_animacao.place(x=690, y=220)
    deletar_terror = Button(frame_deleta, text='TERROR', borderwidth=5, font=('solid 12 bold'),
                            command=deletarFilmeTerror)
    deletar_terror.place(x=230, y=310)
    deletar_documentarios = Button(frame_deleta, text='DOCUMENTÁRIOS', borderwidth=5, font=('solid 12 bold'),
                                   command=deletarFilmeDocumentarios)
    deletar_documentarios.place(x=510, y=310)
    voltar = Button(frame_deleta, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def deletarFilmeAcao():
    tela_deleta_acao = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_deleta_acao.place(x=72, y=90, width=875, height=490)
    acao_titulo = Label(tela_deleta_acao, text='\n   FILMES DE AÇÃO  ', anchor=NE, font=('solid 20 bold'))
    acao_titulo.pack()
    deletar_filme(tela_deleta_acao, "acao")
    voltar = Button(tela_deleta_acao, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def deletarFilmeFiccao():
    tela_deleta_ficcao = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_deleta_ficcao.place(x=72, y=90, width=875, height=490)
    ficcao_titulo = Label(tela_deleta_ficcao, text='\n   FILMES DE FICÇÃO  ', anchor=NE, font=('solid 20 bold'))
    ficcao_titulo.pack()
    deletar_filme(tela_deleta_ficcao, "ficcao")
    voltar = Button(tela_deleta_ficcao, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def deletarFilmeComedia():
    tela_deleta_comedia = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_deleta_comedia.place(x=72, y=90, width=875, height=490)
    comedia_titulo = Label(tela_deleta_comedia, text='\n   FILMES DE COMÉDIA  ', anchor=NE, font=('solid 20 bold'))
    comedia_titulo.pack()
    deletar_filme(tela_deleta_comedia, "comedia")
    voltar = Button(tela_deleta_comedia, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def deletarFilmeRomance():
    tela_deleta_romance = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_deleta_romance.place(x=72, y=90, width=875, height=490)
    romance_titulo = Label(tela_deleta_romance, text='\n   FILMES DE ROMANCE  ', anchor=NE, font=('solid 20 bold'))
    romance_titulo.pack()
    deletar_filme(tela_deleta_romance, "romance")
    voltar = Button(tela_deleta_romance, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def deletarFilmeAnimacao():
    tela_deleta_animacao = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_deleta_animacao.place(x=72, y=90, width=875, height=490)
    animacao_titulo = Label(tela_deleta_animacao, text='\n   FILMES DE ANIMAÇÃO  ', anchor=NE, font=('solid 20 bold'))
    animacao_titulo.pack()
    deletar_filme(tela_deleta_animacao, "animacao")
    voltar = Button(tela_deleta_animacao, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def deletarFilmeTerror():
    tela_deleta_terror = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_deleta_terror.place(x=72, y=90, width=875, height=490)
    terror_titulo = Label(tela_deleta_terror, text='\n   FILMES DE TERROR  ', anchor=NE, font=('solid 20 bold'))
    terror_titulo.pack()
    deletar_filme(tela_deleta_terror, "terror")
    voltar = Button(tela_deleta_terror, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def deletarFilmeDocumentarios():
    tela_deleta_documentarios = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_deleta_documentarios.place(x=72, y=90, width=875, height=490)
    documentarios_titulo = Label(tela_deleta_documentarios, text='\n   FILMES DE DOCUMENTÁRIOS  ', anchor=NE,
                                 font=('solid 20 bold'))
    documentarios_titulo.pack()
    deletar_filme(tela_deleta_documentarios, "documentarios")
    voltar = Button(tela_deleta_documentarios, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def deletar_filme(tela, genero):
    def deletarFilme(i, genero, ):
        if genero == "acao":
            linha = open("Arquivos/ListaDeFilmesDeAcao.txt", "r", -1, "utf-8")
            linhaDeletar = linha.readlines()
            cont = 1
            with open("Arquivos/ListaDeFilmesDeAcao.txt", "w", -1, "utf-8") as fw:
                for line in linhaDeletar:
                    if cont != i:
                        fw.write(line)
                    cont += 1
        elif genero == "ficcao":
            linha = open("Arquivos/ListaDeFilmesDeFiccao.txt", "r", -1, "utf-8")
            linhaDeletar = linha.readlines()
            cont = 1
            with open("Arquivos/ListaDeFilmesDeFiccao.txt", "w", -1, "utf-8") as fw:
                for line in linhaDeletar:
                    if cont != i:
                        fw.write(line)
                    cont += 1
        elif genero == "comedia":
            linha = open("Arquivos/ListaDeFilmesDeComedia.txt", "r", -1, "utf-8")
            linhaDeletar = linha.readlines()
            cont = 1
            with open("Arquivos/ListaDeFilmesDeComedia.txt", "w", -1, "utf-8") as fw:
                for line in linhaDeletar:
                    if cont != i:
                        fw.write(line)
                    cont += 1
        elif genero == "romance":
            linha = open("Arquivos/ListaDeFilmesDeRomance.txt", "r", -1, "utf-8")
            linhaDeletar = linha.readlines()
            cont = 1
            with open("Arquivos/ListaDeFilmesDeRomance.txt", "w", -1, "utf-8") as fw:
                for line in linhaDeletar:
                    if cont != i:
                        fw.write(line)
                    cont += 1
        elif genero == "animacao":
            linha = open("Arquivos/ListaDeFilmesDeAnimacao.txt", "r", -1, "utf-8")
            linhaDeletar = linha.readlines()
            cont = 1
            with open("Arquivos/ListaDeFilmesDeAnimacao.txt", "w", -1, "utf-8") as fw:
                for line in linhaDeletar:
                    if cont != i:
                        fw.write(line)
                    cont += 1
        elif genero == "terror":
            linha = open("Arquivos/ListaDeFilmesDeTerror.txt", "r", -1, "utf-8")
            linhaDeletar = linha.readlines()
            cont = 1
            with open("Arquivos/ListaDeFilmesDeTerror.txt", "w", -1, "utf-8") as fw:
                for line in linhaDeletar:
                    if cont != i:
                        fw.write(line)
                    cont += 1
        elif genero == "documentarios":
            linha = open("Arquivos/ListaDeFilmesDocumentarios.txt", "r", -1, "utf-8")
            linhaDeletar = linha.readlines()
            cont = 1
            with open("Arquivos/ListaDeFilmesDocumentarios.txt", "w", -1, "utf-8") as fw:
                for line in linhaDeletar:
                    if cont != i:
                        fw.write(line)
                    cont += 1

    def verificar_codigo_deletar():
        try:
            k = codigo_filme_a_ser_deletado.get()
            for i in range(1, len(listaLinhas) + 1):
                if k == i:
                    deletarFilme(i, genero)
            if genero == "acao":
                deletarFilmeAcao()
            elif genero == "ficcao":
                deletarFilmeFiccao()
            elif genero == "comedia":
                deletarFilmeComedia()
            elif genero == "romance":
                deletarFilmeRomance()
            elif genero == "animacao":
                deletarFilmeAnimacao()
            elif genero == "terror":
                deletarFilmeTerror()
            elif genero == "documentarios":
                deletarFilmeDocumentarios()
        except:
            pass

    codigo_do_filme = Label(tela, text='Digite o código do filme:', anchor=NE, font=('solid 12 bold'))
    codigo_do_filme.place(x=550, y=170)
    codigo_entrar = Entry(tela, textvariable=codigo_filme_a_ser_deletado, font=('solid', 15, 'normal'))
    codigo_entrar.place(x=550, y=200)
    deletar = Button(tela, text='DELETAR', borderwidth=5, font=('normal', 12, 'bold'), command=verificar_codigo_deletar)
    deletar.place(x=550, y=240)

    generos = {
        "acao": ("Arquivos/ListaDeFilmesDeAcao.txt", "r", -1, "utf-8"),
        "ficcao": ("Arquivos/ListaDeFilmesDeFiccao.txt", "r", -1, "utf-8"),
        "comedia": ("Arquivos/ListaDeFilmesDeComedia.txt", "r", -1, "utf-8"),
        "romance": ("Arquivos/ListaDeFilmesDeRomance.txt", "r", -1, "utf-8"),
        "animacao": ("Arquivos/ListaDeFilmesDeAnimacao.txt", "r", -1, "utf-8"),
        "terror": ("Arquivos/ListaDeFilmesDeTerror.txt", "r", -1, "utf-8"),
        "documentarios": ("Arquivos/ListaDeFilmesDocumentarios.txt", "r", -1, "utf-8")
    }

    arq, tipo, b, e = generos[genero]
    linha = open(arq, tipo, b, e)
    listaLinhas = linha.readlines()
    analise = 0
    for i in range(1, len(listaLinhas) + 1):
        nome = listaLinhas[i - 1].split("|")
        if len(nome[0]) > 50:
            analise = 1
    if len(listaLinhas) >= 8 or analise:
        sb = Scrollbar(tela)
        sb.pack(side=LEFT, fill=Y)
        filmesRolagem = Listbox(tela, font=('solid 12 bold'), yscrollcommand=sb.set)
        for i in range(1, len(listaLinhas) + 1):
            nome = listaLinhas[i - 1].split("|")
            filmesRolagem.insert(END, f"{i}- {nome[0]}")
        filmesRolagem.pack(side=LEFT, fill=Y)
    else:
        for i in range(1, len(listaLinhas) + 1):
            nome = listaLinhas[i - 1].split("|")
            Label(tela, text=f"{i}- {nome[0]}", font=('solid 12 bold')).place(x=100, y=90 + (i - 1) * 50)

def frame_usuario():
    tela_usuario = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_usuario.place(x=72, y=90, width=875, height=490)
    genero = Label(tela_usuario, text='\nGÊNEROS', anchor=NE, font=('solid 20 bold'))
    genero.pack()
    acao = Button(tela_usuario, text='  AÇÃO  ', borderwidth=5, font=('solid 12 bold'), command=frame_acao)
    acao.place(x=230, y=140)
    ficcao = Button(tela_usuario, text='FICÇÃO', borderwidth=5, font=('solid 12 bold'), command=frame_ficcao)
    ficcao.place(x=550, y=140)
    comedia = Button(tela_usuario, text='COMÉDIA', borderwidth=5, font=('solid 12 bold'), command=frame_comedia)
    comedia.place(x=80, y=220)
    romance = Button(tela_usuario, text='ROMANCE', borderwidth=5, font=('solid 12 bold'), command=frame_romance)
    romance.place(x=380, y=220)
    animacao = Button(tela_usuario, text='ANIMAÇÃO', borderwidth=5, font=('solid 12 bold'), command=frame_animacao)
    animacao.place(x=690, y=220)
    terror = Button(tela_usuario, text='TERROR', borderwidth=5, font=('solid 12 bold'), command=frame_terror)
    terror.place(x=230, y=310)
    documentarios = Button(tela_usuario, text='DOCUMENTÁRIOS', borderwidth=5, font=('solid 12 bold'),
                           command=frame_documnetarios)
    documentarios.place(x=510, y=310)
    voltar = Button(tela_usuario, text='I N Í C I O', borderwidth=5, font=('normal 12'), command=inicio)
    voltar.place(x=750, y=430)


def frame_acao():
    tela_acao = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_acao.place(x=72, y=90, width=875, height=490)
    acao_titulo = Label(tela_acao, text='\n   FILMES DE AÇÃO  ', anchor=NE, font=('solid 20 bold'))
    acao_titulo.pack()
    mostra_filme(tela_acao, "acao")
    voltar = Button(tela_acao, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=frame_usuario)
    voltar.place(x=750, y=430)


def frame_ficcao():
    tela_ficcao = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_ficcao.place(x=72, y=90, width=875, height=490)
    ficcao_titulo = Label(tela_ficcao, text='\n   FILMES DE FICÇÃO  ', anchor=NE, font=('solid 20 bold'))
    ficcao_titulo.pack()
    mostra_filme(tela_ficcao, "ficcao")
    voltar = Button(tela_ficcao, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=frame_usuario)
    voltar.place(x=750, y=430)


def frame_comedia():
    tela_comedia = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_comedia.place(x=72, y=90, width=875, height=490)
    comedia_titulo = Label(tela_comedia, text='\n   FILMES DE COMÉDIA  ', anchor=NE, font=('solid 20 bold'))
    comedia_titulo.pack()
    mostra_filme(tela_comedia, "comedia")
    voltar = Button(tela_comedia, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=frame_usuario)
    voltar.place(x=750, y=430)


def frame_romance():
    tela_romance = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_romance.place(x=72, y=90, width=875, height=490)
    romance_titulo = Label(tela_romance, text='\n   FILMES DE ROMANCE  ', anchor=NE, font=('solid 20 bold'))
    romance_titulo.pack()
    mostra_filme(tela_romance, "romance")
    voltar = Button(tela_romance, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=frame_usuario)
    voltar.place(x=750, y=430)


def frame_animacao():
    tela_animacao = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_animacao.place(x=72, y=90, width=875, height=490)
    animacao_titulo = Label(tela_animacao, text='\n   FILMES DE ANIMAÇÃO  ', anchor=NE, font=('solid 20 bold'))
    animacao_titulo.pack()
    mostra_filme(tela_animacao, "animacao")
    voltar = Button(tela_animacao, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=frame_usuario)
    voltar.place(x=750, y=430)


def frame_terror():
    tela_terror = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_terror.place(x=72, y=90, width=875, height=490)
    terror_titulo = Label(tela_terror, text='\n   FILMES DE TERROR  ', anchor=NE, font=('solid 20 bold'))
    terror_titulo.pack()
    mostra_filme(tela_terror, "terror")
    voltar = Button(tela_terror, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=frame_usuario)
    voltar.place(x=750, y=430)


def frame_documnetarios():
    tela_documentarios = Frame(menu_inicial, borderwidth=5, relief='solid')
    tela_documentarios.place(x=72, y=90, width=875, height=490)
    documentarios_titulo = Label(tela_documentarios, text='\n   DOCUMENTÁRIOS  ', anchor=NE, font=('solid 20 bold'))
    documentarios_titulo.pack()
    mostra_filme(tela_documentarios, "documentarios")
    voltar = Button(tela_documentarios, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=frame_usuario)
    voltar.place(x=750, y=430)


def mostra_filme(t, genero):
    def abrir_descricao_filme(i, genero):
        telaVoltar = {
            "acao": frame_acao,
            "ficcao": frame_ficcao,
            "comedia": frame_comedia,
            "romance": frame_romance,
            "animacao": frame_animacao,
            "terror": frame_terror,
            "documentarios": frame_documnetarios
        }

        filme = listaLinhas[i].split("|")
        tela_descricao = Frame(menu_inicial, borderwidth=5, relief='solid')
        tela_descricao.place(x=72, y=90, width=875, height=490)
        titulo_filme = Label(tela_descricao, text=f'\n{filme[0]}', anchor=NE, font=('solid 20 bold'))
        titulo_filme.pack()
        nome_sinopse = Label(tela_descricao, text=f'SINOPSE:', anchor=NE, font=('solid 11 bold'))
        nome_sinopse.pack()
        nome_sinopse.place(x=30, y=80)
        if len(filme[1]) > 72:
            descricaoFormatada = ""
            for i in range(len(filme[1])):
                descricaoFormatada += filme[1][i]
                if len(descricaoFormatada) % 72 == 0:
                    if descricaoFormatada[-1] == " ":
                        descricaoFormatada += "\n"
                    else:
                        descricaoFormatada += "-\n"
            filme[1] = descricaoFormatada
        else:
            pass
        sobre_filme = Label(tela_descricao, text=f'{filme[1]}', anchor=NE, font=('solid 15 bold'))
        sobre_filme.pack()
        sobre_filme.place(x=30, y=100)
        ano_filme = Label(tela_descricao, text=f'LANÇAMENTO: {filme[2]}', anchor=NE, font=('solid 11 bold'))
        ano_filme.pack()
        ano_filme.place(x=30, y=400)
        streaming = Label(tela_descricao, text=f'STREAMING: {filme[3]}', anchor=NE, font=('solid 11 bold'))
        streaming.pack()
        streaming.place(x=30, y=430)
        voltar = Button(tela_descricao, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=telaVoltar[genero])
        voltar.place(x=750, y=430)

    def verificar_codigo():
        try:
            k = codigo_filme.get()
            for i in range(1, len(listaLinhas) + 1):
                if k == i:
                    abrir_descricao_filme(i - 1, genero)
        except:
            pass

    codigo = Label(t, text='Digite o código do filme:', anchor=NE, font=('solid 12 bold'))
    codigo.place(x=550, y=170)
    codigo_entrar = Entry(t, textvariable=codigo_filme, font=('solid', 15, 'normal'))
    codigo_entrar.place(x=550, y=200)
    acessar = Button(t, text='PESQUISAR', borderwidth=5, font=('normal', 12, 'bold'), command=verificar_codigo)
    acessar.place(x=550, y=240)

    generos = {
        "acao": ("Arquivos/ListaDeFilmesDeAcao.txt", "r", -1, "utf-8"),
        "ficcao": ("Arquivos/ListaDeFilmesDeFiccao.txt", "r", -1, "utf-8"),
        "comedia": ("Arquivos/ListaDeFilmesDeComedia.txt", "r", -1, "utf-8"),
        "romance": ("Arquivos/ListaDeFilmesDeRomance.txt", "r", -1, "utf-8"),
        "animacao": ("Arquivos/ListaDeFilmesDeAnimacao.txt", "r", -1, "utf-8"),
        "terror": ("Arquivos/ListaDeFilmesDeTerror.txt", "r", -1, "utf-8"),
        "documentarios": ("Arquivos/ListaDeFilmesDocumentarios.txt", "r", -1, "utf-8")
    }

    arq, tipo, b, e = generos[genero]
    linha = open(arq, tipo, b, e)
    listaLinhas = linha.readlines()
    analise = 0
    for i in range(1, len(listaLinhas) + 1):
        nome = listaLinhas[i - 1].split("|")
        if len(nome[0]) > 50:
            analise = 1
    if len(listaLinhas) > 8 or analise:
        sb = Scrollbar(t)
        sb.pack(side=LEFT, fill=Y)
        filmesRolagem = Listbox(t, font=('solid 12 bold'), yscrollcommand=sb.set)
        for i in range(1, len(listaLinhas) + 1):
            nome = listaLinhas[i - 1].split("|")
            filmesRolagem.insert(END, f"{i}- {nome[0]}")
        filmesRolagem.pack(side=LEFT, fill=Y)
    else:
        for i in range(1, len(listaLinhas) + 1):
            nome = listaLinhas[i - 1].split("|")
            Label(t, text=f"{i}- {nome[0]}", font=('solid 12 bold')).place(x=100, y=90 + (i - 1) * 50)


def inserirFilmeAcao():
    frame_filme_acao = Frame(menu_inicial, borderwidth=5, relief='solid')
    frame_filme_acao.place(x=72, y=90, width=875, height=490)
    insere_dados = Label(frame_filme_acao, text='\nPREENCHA OS DADOS DO FILME DE AÇÃO', anchor=NE,
                         font=('solid 18 bold'))
    insere_dados.pack()
    nome_do_filme_label = Label(frame_filme_acao, text='TÍTULO:', anchor=NE, font=('solid 15 bold'))
    nome_do_filme_label.place(x=230, y=170)
    escrever_nome = Entry(frame_filme_acao, textvariable=nome_do_filme, font=('solid', 15, 'normal'))
    escrever_nome.place(x=450, y=170)
    sinopse_do_filme_label = Label(frame_filme_acao, text='SINOPSE:', anchor=NE, font=('solid 15 bold'))
    sinopse_do_filme_label.place(x=230, y=220)
    escrever_sinopse = Entry(frame_filme_acao, textvariable=sinopse_do_filme, font=('solid', 15, 'normal'))
    escrever_sinopse.place(x=450, y=220)
    data_do_filme_label = Label(frame_filme_acao, text='LANÇAMENTO:', anchor=NE, font=('solid 15 bold'))
    data_do_filme_label.place(x=230, y=270)
    escrever_data = Entry(frame_filme_acao, textvariable=data_do_filme, font=('solid', 15, 'normal'))
    escrever_data.place(x=450, y=270)
    disponibilidade_do_filme_label = Label(frame_filme_acao, text='STREAMING:', anchor=NE, font=('solid 15 bold'))
    disponibilidade_do_filme_label.place(x=230, y=320)
    escrever_disponibilidade = Entry(frame_filme_acao, textvariable=disponibilidade_do_filme,
                                     font=('solid', 15, 'normal'))
    escrever_disponibilidade.place(x=450, y=320)
    botao_de_salvar = Button(frame_filme_acao, text='SALVAR', borderwidth=5, font=('normal, 12'),
                             command=insere_no_arquivo_acao)
    botao_de_salvar.place(x=750, y=380)
    voltar = Button(frame_filme_acao, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def insere_no_arquivo_acao():
    f = open("Arquivos/ListaDeFilmesDeAcao.txt", "a")
    f.write(
        f"{nome_do_filme.get()}|{sinopse_do_filme.get()}|{data_do_filme.get()}|{disponibilidade_do_filme.get()}\n"
    )
    f.close()
    acessado_adm()


def inserirFilmeFiccao():
    frame_filme_ficcao = Frame(menu_inicial, borderwidth=5, relief='solid')
    frame_filme_ficcao.place(x=72, y=90, width=875, height=490)
    insere_dados = Label(frame_filme_ficcao, text='\nPREENCHA OS DADOS DO FILME DE FICÇÃO', anchor=NE,
                         font=('solid 18 bold'))
    insere_dados.pack()
    nome_do_filme_label = Label(frame_filme_ficcao, text='TÍTULO:', anchor=NE, font=('solid 15 bold'))
    nome_do_filme_label.place(x=230, y=170)
    escrever_nome = Entry(frame_filme_ficcao, textvariable=nome_do_filme, font=('solid', 15, 'normal'))
    escrever_nome.place(x=450, y=170)
    sinopse_do_filme_label = Label(frame_filme_ficcao, text='SINOPSE:', anchor=NE, font=('solid 15 bold'))
    sinopse_do_filme_label.place(x=230, y=220)
    escrever_sinopse = Entry(frame_filme_ficcao, textvariable=sinopse_do_filme, font=('solid', 15, 'normal'))
    escrever_sinopse.place(x=450, y=220)
    data_do_filme_label = Label(frame_filme_ficcao, text='LANÇAMENTO:', anchor=NE, font=('solid 15 bold'))
    data_do_filme_label.place(x=230, y=270)
    escrever_data = Entry(frame_filme_ficcao, textvariable=data_do_filme, font=('solid', 15, 'normal'))
    escrever_data.place(x=450, y=270)
    disponibilidade_do_filme_label = Label(frame_filme_ficcao, text='STREAMING:', anchor=NE, font=('solid 15 bold'))
    disponibilidade_do_filme_label.place(x=230, y=320)
    escrever_disponibilidade = Entry(frame_filme_ficcao, textvariable=disponibilidade_do_filme,
                                     font=('solid', 15, 'normal'))
    escrever_disponibilidade.place(x=450, y=320)
    botao_de_salvar = Button(frame_filme_ficcao, text='SALVAR', borderwidth=5, font=('normal, 12'),
                             command=insere_no_arquivo_ficcao)
    botao_de_salvar.place(x=750, y=380)
    voltar = Button(frame_filme_ficcao, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def insere_no_arquivo_ficcao():
    f = open("Arquivos/ListaDeFilmesDeFiccao", "a")
    f.write(f"{nome_do_filme.get()}|{sinopse_do_filme.get()}|{data_do_filme.get()}|{disponibilidade_do_filme.get()}\n")
    f.close()
    acessado_adm()


def inserirFilmeComedia():
    frame_filme_comedia = Frame(menu_inicial, borderwidth=5, relief='solid')
    frame_filme_comedia.place(x=72, y=90, width=875, height=490)
    insere_dados = Label(frame_filme_comedia, text='\nPREENCHA OS DADOS DO FILME DE COMÉDIA', anchor=NE,
                         font=('solid 18 bold'))
    insere_dados.pack()
    nome_do_filme_label = Label(frame_filme_comedia, text='TÍTULO:', anchor=NE, font=('solid 15 bold'))
    nome_do_filme_label.place(x=230, y=170)
    escrever_nome = Entry(frame_filme_comedia, textvariable=nome_do_filme, font=('solid', 15, 'normal'))
    escrever_nome.place(x=450, y=170)
    sinopse_do_filme_label = Label(frame_filme_comedia, text='SINOPSE:', anchor=NE, font=('solid 15 bold'))
    sinopse_do_filme_label.place(x=230, y=220)
    escrever_sinopse = Entry(frame_filme_comedia, textvariable=sinopse_do_filme, font=('solid', 15, 'normal'))
    escrever_sinopse.place(x=450, y=220)
    data_do_filme_label = Label(frame_filme_comedia, text='LANÇAMENTO:', anchor=NE, font=('solid 15 bold'))
    data_do_filme_label.place(x=230, y=270)
    escrever_data = Entry(frame_filme_comedia, textvariable=data_do_filme, font=('solid', 15, 'normal'))
    escrever_data.place(x=450, y=270)
    disponibilidade_do_filme_label = Label(frame_filme_comedia, text='STREAMING:', anchor=NE, font=('solid 15 bold'))
    disponibilidade_do_filme_label.place(x=230, y=320)
    escrever_disponibilidade = Entry(frame_filme_comedia, textvariable=disponibilidade_do_filme,
                                     font=('solid', 15, 'normal'))
    escrever_disponibilidade.place(x=450, y=320)
    botao_de_salvar = Button(frame_filme_comedia, text='SALVAR', borderwidth=5, font=('normal, 12'),
                             command=insere_no_arquivo_comedia)
    botao_de_salvar.place(x=750, y=380)
    voltar = Button(frame_filme_comedia, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def insere_no_arquivo_comedia():
    f = open("Arquivos/ListaDeFilmesDeComedia.txt", "a")
    f.write(f"{nome_do_filme.get()}|{sinopse_do_filme.get()}|{data_do_filme.get()}|{disponibilidade_do_filme.get()}\n")
    f.close()
    acessado_adm()


def inserirFilmeRomance():
    frame_filme_romance = Frame(menu_inicial, borderwidth=5, relief='solid')
    frame_filme_romance.place(x=72, y=90, width=875, height=490)
    insere_dados = Label(frame_filme_romance, text='\nPREENCHA OS DADOS DO FILME DE ROMANCE', anchor=NE,
                         font=('solid 18 bold'))
    insere_dados.pack()
    nome_do_filme_label = Label(frame_filme_romance, text='TÍTULO:', anchor=NE, font=('solid 15 bold'))
    nome_do_filme_label.place(x=230, y=170)
    escrever_nome = Entry(frame_filme_romance, textvariable=nome_do_filme, font=('solid', 15, 'normal'))
    escrever_nome.place(x=450, y=170)
    sinopse_do_filme_label = Label(frame_filme_romance, text='SINOPSE:', anchor=NE, font=('solid 15 bold'))
    sinopse_do_filme_label.place(x=230, y=220)
    escrever_sinopse = Entry(frame_filme_romance, textvariable=sinopse_do_filme, font=('solid', 15, 'normal'))
    escrever_sinopse.place(x=450, y=220)
    data_do_filme_label = Label(frame_filme_romance, text='LANÇAMENTO:', anchor=NE, font=('solid 15 bold'))
    data_do_filme_label.place(x=230, y=270)
    escrever_data = Entry(frame_filme_romance, textvariable=data_do_filme, font=('solid', 15, 'normal'))
    escrever_data.place(x=450, y=270)
    disponibilidade_do_filme_label = Label(frame_filme_romance, text='STREAMING:', anchor=NE, font=('solid 15 bold'))
    disponibilidade_do_filme_label.place(x=230, y=320)
    escrever_disponibilidade = Entry(frame_filme_romance, textvariable=disponibilidade_do_filme,
                                     font=('solid', 15, 'normal'))
    escrever_disponibilidade.place(x=450, y=320)
    botao_de_salvar = Button(frame_filme_romance, text='SALVAR', borderwidth=5, font=('normal, 12'),
                             command=insere_no_arquivo_romance)
    botao_de_salvar.place(x=750, y=380)
    voltar = Button(frame_filme_romance, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def insere_no_arquivo_romance():
    f = open("Arquivos/ListaDeFilmesDeRomance.txt", "a")
    f.write(f"{nome_do_filme.get()}|{sinopse_do_filme.get()}|{data_do_filme.get()}|{disponibilidade_do_filme.get()}\n")
    f.close()
    acessado_adm()


def inserirFilmeAnimacao():
    frame_filme_animacao = Frame(menu_inicial, borderwidth=5, relief='solid')
    frame_filme_animacao.place(x=72, y=90, width=875, height=490)
    insere_dados = Label(frame_filme_animacao, text='\nPREENCHA OS DADOS DO FILME DE ANIMAÇÃO', anchor=NE,
                         font=('solid 18 bold'))
    insere_dados.pack()
    nome_do_filme_label = Label(frame_filme_animacao, text='TÍTULO:', anchor=NE, font=('solid 15 bold'))
    nome_do_filme_label.place(x=230, y=170)
    escrever_nome = Entry(frame_filme_animacao, textvariable=nome_do_filme, font=('solid', 15, 'normal'))
    escrever_nome.place(x=450, y=170)
    sinopse_do_filme_label = Label(frame_filme_animacao, text='SINOPSE:', anchor=NE, font=('solid 15 bold'))
    sinopse_do_filme_label.place(x=230, y=220)
    escrever_sinopse = Entry(frame_filme_animacao, textvariable=sinopse_do_filme, font=('solid', 15, 'normal'))
    escrever_sinopse.place(x=450, y=220)
    data_do_filme_label = Label(frame_filme_animacao, text='LANÇAMENTO:', anchor=NE, font=('solid 15 bold'))
    data_do_filme_label.place(x=230, y=270)
    escrever_data = Entry(frame_filme_animacao, textvariable=data_do_filme, font=('solid', 15, 'normal'))
    escrever_data.place(x=450, y=270)
    disponibilidade_do_filme_label = Label(frame_filme_animacao, text='STREAMING:', anchor=NE, font=('solid 15 bold'))
    disponibilidade_do_filme_label.place(x=230, y=320)
    escrever_disponibilidade = Entry(frame_filme_animacao, textvariable=disponibilidade_do_filme,
                                     font=('solid', 15, 'normal'))
    escrever_disponibilidade.place(x=450, y=320)
    botao_de_salvar = Button(frame_filme_animacao, text='SALVAR', borderwidth=5, font=('normal, 12'),
                             command=insere_no_arquivo_animacao)
    botao_de_salvar.place(x=750, y=380)
    voltar = Button(frame_filme_animacao, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def insere_no_arquivo_animacao():
    f = open("Arquivos/ListaDeFilmesDeAnimacao.txt", "a")
    f.write(f"{nome_do_filme.get()}|{sinopse_do_filme.get()}|{data_do_filme.get()}|{disponibilidade_do_filme.get()}\n")
    f.close()
    acessado_adm()


def inserirFilmeTerror():
    frame_filme_terror = Frame(menu_inicial, borderwidth=5, relief='solid')
    frame_filme_terror.place(x=72, y=90, width=875, height=490)
    insere_dados = Label(frame_filme_terror, text='\nPREENCHA OS DADOS DO FILME DE TERROR', anchor=NE,
                         font=('solid 18 bold'))
    insere_dados.pack()
    nome_do_filme_label = Label(frame_filme_terror, text='TÍTULO:', anchor=NE, font=('solid 15 bold'))
    nome_do_filme_label.place(x=230, y=170)
    escrever_nome = Entry(frame_filme_terror, textvariable=nome_do_filme, font=('solid', 15, 'normal'))
    escrever_nome.place(x=450, y=170)
    sinopse_do_filme_label = Label(frame_filme_terror, text='SINOPSE:', anchor=NE, font=('solid 15 bold'))
    sinopse_do_filme_label.place(x=230, y=220)
    escrever_sinopse = Entry(frame_filme_terror, textvariable=sinopse_do_filme, font=('solid', 15, 'normal'))
    escrever_sinopse.place(x=450, y=220)
    data_do_filme_label = Label(frame_filme_terror, text='LANÇAMENTO:', anchor=NE, font=('solid 15 bold'))
    data_do_filme_label.place(x=230, y=270)
    escrever_data = Entry(frame_filme_terror, textvariable=data_do_filme, font=('solid', 15, 'normal'))
    escrever_data.place(x=450, y=270)
    disponibilidade_do_filme_label = Label(frame_filme_terror, text='STREAMING:', anchor=NE, font=('solid 15 bold'))
    disponibilidade_do_filme_label.place(x=230, y=320)
    escrever_disponibilidade = Entry(frame_filme_terror, textvariable=disponibilidade_do_filme,
                                     font=('solid', 15, 'normal'))
    escrever_disponibilidade.place(x=450, y=320)
    botao_de_salvar = Button(frame_filme_terror, text='SALVAR', borderwidth=5, font=('normal, 12'),
                             command=insere_no_arquivo_terror)
    botao_de_salvar.place(x=750, y=380)
    voltar = Button(frame_filme_terror, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def insere_no_arquivo_terror():
    f = open("Arquivos/ListaDeFilmesDeTerror.txt", "a")
    f.write(f"{nome_do_filme.get()}|{sinopse_do_filme.get()}|{data_do_filme.get()}|{disponibilidade_do_filme.get()}\n")
    f.close()
    acessado_adm()


def inserirFilmeDocumentario():
    frame_filme_documentario = Frame(menu_inicial, borderwidth=5, relief='solid')
    frame_filme_documentario.place(x=72, y=90, width=875, height=490)
    insere_dados = Label(frame_filme_documentario, text='\nPREENCHA OS DADOS DO FILME DE DOCUMENTÁRIO', anchor=NE,
                         font=('solid 18 bold'))
    insere_dados.pack()
    nome_do_filme_label = Label(frame_filme_documentario, text='TÍTULO:', anchor=NE, font=('solid 15 bold'))
    nome_do_filme_label.place(x=230, y=170)
    escrever_nome = Entry(frame_filme_documentario, textvariable=nome_do_filme, font=('solid', 15, 'normal'))
    escrever_nome.place(x=450, y=170)
    sinopse_do_filme_label = Label(frame_filme_documentario, text='SINOPSE:', anchor=NE, font=('solid 15 bold'))
    sinopse_do_filme_label.place(x=230, y=220)
    escrever_sinopse = Entry(frame_filme_documentario, textvariable=sinopse_do_filme, font=('solid', 15, 'normal'))
    escrever_sinopse.place(x=450, y=220)
    data_do_filme_label = Label(frame_filme_documentario, text='LANÇAMENTO:', anchor=NE, font=('solid 15 bold'))
    data_do_filme_label.place(x=230, y=270)
    escrever_data = Entry(frame_filme_documentario, textvariable=data_do_filme, font=('solid', 15, 'normal'))
    escrever_data.place(x=450, y=270)
    disponibilidade_do_filme_label = Label(frame_filme_documentario, text='STREAMING:', anchor=NE,
                                           font=('solid 15 bold'))
    disponibilidade_do_filme_label.place(x=230, y=320)
    escrever_disponibilidade = Entry(frame_filme_documentario, textvariable=disponibilidade_do_filme,
                                     font=('solid', 15, 'normal'))
    escrever_disponibilidade.place(x=450, y=320)
    botao_de_salvar = Button(frame_filme_documentario, text='SALVAR', borderwidth=5, font=('normal, 12'),
                             command=insere_no_arquivo_documentario)
    botao_de_salvar.place(x=750, y=380)
    voltar = Button(frame_filme_documentario, text='VOLTAR', borderwidth=5, font=('normal, 12'), command=acessado_adm)
    voltar.place(x=750, y=430)


def insere_no_arquivo_documentario():
    f = open("Arquivos/ListaDeFilmesDocumentarios.txt", "a")
    f.write(f"{nome_do_filme.get()}|{sinopse_do_filme.get()}|{data_do_filme.get()}|{disponibilidade_do_filme.get()}\n")
    f.close()
    acessado_adm()

inicio()

menu_inicial.mainloop()