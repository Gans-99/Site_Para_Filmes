# 🎬 DISKCINE — Sistema de Gerenciamento de Filmes em Python

Projeto desenvolvido para a disciplina **Fundamentos de Programação**, com o objetivo de implementar um sistema de gerenciamento de filmes com interface gráfica (**Tkinter**). O projeto simula uma videolocadora digital, permitindo cadastro, listagem e exclusão de filmes por gênero, além de login e controle de administradores.

---

## 📘 Sobre o Projeto

**DISKCINE** é um sistema de gerenciamento de filmes desenvolvido em **Python**, com interface gráfica utilizando **Tkinter**.
O projeto tem como objetivo aplicar os conceitos fundamentais de **programação estruturada**, **manipulação de arquivos**, **funções** e **modularização**.
O sistema simula uma **videolocadora digital**, permitindo o **cadastro, listagem e exclusão de filmes** divididos por gênero (Ação, Comédia, Ficção, Romance, Animação, Terror e Documentários).
Também inclui um **sistema de login e controle de administradores**, possibilitando o gerenciamento seguro dos dados.

---

## 🎯 Objetivo Acadêmico

Trabalho desenvolvido para a disciplina **Fundamentos de Programação**, com o propósito de implementar um sistema completo em **Python**, aplicando:

* Manipulação de **arquivos texto (.txt)**
* **Estruturas de decisão e repetição**
* **Funções e modularização**
* **Criação de interface gráfica (Tkinter)**
* **Controle de usuários e autenticação simples**
* **Organização de dados por categorias**

---

## ⚙️ Funcionalidades Principais

### ✅ Login e Acesso Administrativo

* Sistema de autenticação de usuários
* Controle de acesso para cadastro e exclusão de filmes

### ✅ Cadastro de Filmes por Gênero

* Gêneros: Ação, Animação, Comédia, Ficção, Romance, Terror e Documentários
* Armazena informações em arquivos `.txt` individuais para cada gênero

### ✅ Listagem de Filmes

* Exibe todos os filmes cadastrados em uma interface Tkinter
* Permite visualização separada por gênero

### ✅ Remoção de Filmes

* Exclui títulos diretamente pelo sistema
* Atualiza automaticamente o arquivo correspondente

### ✅ Interface Gráfica Amigável

* Desenvolvida com **Tkinter**, simulando uma locadora interativa

---

## 🗂️ Estrutura de Arquivos

```
📁 Site_Para_Filmes/
│
├── main.py                            # Arquivo principal (inicializa o sistema)
├── senhaadministrador.txt             # Usuário e senha do administradores
├── ListaDeFilmesDeAcao.txt            # Lista de filmes de ação
├── ListaDeFilmesDeAnimacao.txt        # Lista de filmes de animação
├── ListaDeFilmesDeComedia.txt         # Lista de filmes de comédia
├── ListaDeFilmesDeFiccao.txt          # Lista de filmes de ficção científica
├── ListaDeFilmesDeRomance.txt         # Lista de filmes de romance
├── ListaDeFilmesDeTerror.txt          # Lista de filmes de terror
├── ListaDeFilmesDoDocumentarios.txt   # Lista de filmes de documentários
└── README.md                          # (este arquivo)
```

---

## 💻 Como Executar o Projeto

1️⃣ **Instale o Python 3**
Certifique-se de ter o Python instalado no computador.

2️⃣ **Execute o programa**
Abra o terminal ou prompt de comando na pasta do projeto e digite:

```bash
python main.py
```

3️⃣ **Use a interface gráfica**
A janela principal será aberta, exibindo as opções de login e gerenciamento de filmes.

---

## 🔐 Fluxo de Uso

1. Inicie o programa (`main.py`)
2. Faça login como administrador
3. Escolha o gênero de filme desejado
4. Cadastre, visualize ou remova títulos
5. Os dados são automaticamente salvos em arquivos `.txt`

---

## 👥 Equipe do Trabalho

| Membros              |
| -------------------- |
| Mahatma Gandhi       |
| Ciro Coimbra         |               
| Alexsandro Martins   |
| Lígia Sufia          |
| Luana Cristina       |

---

## 🧩 Possíveis Melhorias Futuras

* Implementar **pesquisa de filmes** por nome ou gênero
* Adicionar **avaliações e classificações**
* Criar **relatórios automáticos** (número de filmes por categoria)
* Migrar os dados para um **banco de dados SQLite**
* Modernizar a interface com **Tkinter avançado** ou **PyQt**

---

## 📜 Licença

Este projeto foi desenvolvido para fins acadêmicos na disciplina de **Fundamentos de Programação**.
Você pode reutilizá-lo livremente para fins de estudo e aprendizado.

🎥 *“DISKCINE — a nostalgia das locadoras, agora em versão digital.”*
