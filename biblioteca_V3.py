#Sistema de uma Biblioteca, onde o usuário pode cadastrar livros, visualizar a disponibilidade, buscar por livros específicos, além de registrar empréstimos e devoluções.


#Classe que representa os livros da biblioteca.
class Livro:
    def __init__(self, titulo, autor, ano):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._disponivel = True

#Retorna uma representação textual formatada do livro:
    def __str__(self):
        status = "Disponível" if self._disponivel else "Emprestado"
        return f"'{self._titulo}' por {self._autor} ({self._ano}) - Status: {status}"

#Métodos:
    def emprestar(self):
        if self._disponivel:
            self._disponivel = False
            return True
        return False

    def devolver(self):
        if not self._disponivel:
            self._disponivel = True
            return True
        return False

#Classe que representa um usuário cadastrado na biblioteca.
class Usuario:
    def __init__(self, nome, telefone, email, endereco, idade):
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._endereco = endereco
        self._idade = idade
        self._livros_emprestados = []

#Retorna uma descrição do usuário:
    def __str__(self):
        return f"Nome: {self._nome} | E-mail: {self._email} | Telefone: {self._telefone}"
    
    #Métodos:
    def adicionar_emprestimo(self, livro):
        self._livros_emprestados.append(livro)

    def remover_emprestimo(self, livro):
        if livro in self._livros_emprestados:
            self._livros_emprestados.remove(livro)

#Classe que gerencia todo o funcionamento do sistema.
class Biblioteca:
    def __init__(self, nome):
        self._nome = nome
        self._livros = []
        self._usuarios = []

    #Métodos:

    def encontrar_usuario(self, email):
        for usuario in self._usuarios:
            if usuario._email.lower() == email.strip().lower():
                return usuario
        return None

    def encontrar_livro(self, titulo):
        for livro in self._livros:
            if livro._titulo.lower() == titulo.strip().lower():
                return livro
        return None

    def cadastrar_livro(self):
        print("\n*** Cadastro de Novo Livro ***\n")
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano: ")
        novo_livro = Livro(titulo, autor, ano)
        self._livros.append(novo_livro)
        print(f"\nLivro '{titulo}' cadastrado com sucesso!\n")

    def criar_usuario(self):
        print("\n*** Cadastro de Novo Usuário ***\n")
        nome = input("Nome do usuário: ")
        idade = input("Idade: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        endereco = input("Endereço: ")
        novo_usuario = Usuario(nome, telefone, email, endereco, idade)
        self._usuarios.append(novo_usuario)
        print(f"\nUsuário {nome} cadastrado com sucesso!\n")

    def encontrar_livro(self, titulo):
        for livro in self._livros:
            if livro._titulo.lower() == titulo.strip().lower():
                return livro
        return None
    
    def encontrar_usuario(self, email):
        for usuario in self._usuarios:
            if usuario._email.lower() == email.strip().lower():
                return usuario
        return None

    def buscar_livro(self):
        if not self._livros:
            print("\n*** Nenhum livro cadastrado até o momento. ***\n")
            return
        
        titulo_livro = input("\n*** Digite o titulo (ou parte dele) do livro que esta procurando: ***\n").strip().lower()
        pesquisado = [livro for livro in self._livros if titulo_livro in livro._titulo.lower()]

        if pesquisado:
            print("\n*** Livro pesquisado ***")
            for i, livro in enumerate(pesquisado, start=1):
                print(f"{i}. {livro}")
            print()
        else:
            print(f"\n*** Nenhum livro encontrado com o termo '{pesquisado}'. ***\n")

    def listar_todos_livros(self):
        if not self._livros:
            print("\n*** Nenhum livro cadastrado ainda. ***\n")
            return
        print("\n*** Lista de Livros Cadastrados ***\n")
        for i, livro in enumerate(self._livros, start=1):
            print(f"{i}. {livro}")
        print()

    def listar_usuarios(self):
        if not self._usuarios:
            print("\n*** Nenhum usuário cadastrado ainda. ***\n")
            return
        print("\n*** Lista de Usuarios: ***\n")
        for i, usuario in enumerate(self._usuarios, start=1):
            print(f"{i}. {usuario}")
        print()

    def emprestar_livro(self):
        email_usuario = input("\n*** E-mail do usuário: ***\n")
        usuario = self.encontrar_usuario(email_usuario)
        if not usuario:
            print("\n*** Usuário não encontrado. ***\n")
            return

        titulo_livro = input("\n*** Título do livro a emprestar: ***\n")
        livro = self.encontrar_livro(titulo_livro)
        if not livro:
            print("\n*** Livro não encontrado. ***\n")
            return

        # Lógica de negócio centralizada na Biblioteca
        if livro.emprestar():
            usuario.adicionar_emprestimo(livro)
            print(f"\n*** Empréstimo de '{livro._titulo}' para {usuario._nome} realizado com sucesso. ***\n")
        else:
            print(f"\n*** O livro '{livro._titulo}' não está disponível para empréstimo. ***\n")

    def devolver_livro(self):
        titulo_livro = input("\n*** Título do livro a devolver: ***\n")
        livro = self.encontrar_livro(titulo_livro)
        if not livro:
            print("\n*** Livro não encontrado. ***\n")
            return

            # Encontrar o usuário que está com o livro (em um sistema real, isso seria mais direto)
        usuario_com_livro = None
        for u in self._usuarios:
            if livro in u._livros_emprestados:
                usuario_com_livro = u
                break
            
        if not usuario_com_livro:
            print(f"\n*** Erro: Este livro não consta como emprestado por nenhum usuário. ***\n")
            # Mesmo assim, tentaremos devolver para corrigir o estado
            if not livro.disponivel:
                livro.devolver()
                print("\n*** Status do livro corrigido para 'Disponível'. ***\n")
            return

        if livro.devolver():
            usuario_com_livro.remover_emprestimo(livro)
            print(f"\n*** Devolução de '{livro._titulo}' por {usuario_com_livro._nome} realizada com sucesso. ***\n")
        else:
            print(f"\n*** Este livro já constava como disponível. ***\n")

#Exibe o menu de opções para o usuário.
def menu():
    tela = """
    =================== MENU BIBLIOTECA ===================
    [1] Cadastrar Livro
    [2] Emprestar Livro
    [3] Buscar Livro
    [4] Devolver Livro
    [5] Criar Usuário
    [6] Listar Usuários
    [7] Listar Todos os Livros
    [0] Sair
    =======================================================
    => """
    return input(tela)

def main():
    minha_biblioteca = Biblioteca(f"Biblioteca Pública de Cubatão")
    print(f"Bem-vindo ao sistema da {minha_biblioteca._nome}!")

    while True:
        opcao = menu()

        if opcao == "1":
            minha_biblioteca.cadastrar_livro()

        elif opcao == "2":
            minha_biblioteca.emprestar_livro()

        elif opcao == "3":
            minha_biblioteca.buscar_livro()

        elif opcao == "4":
            minha_biblioteca.devolver_livro()

        elif opcao == "5":
            minha_biblioteca.criar_usuario()

        elif opcao == "6":
            minha_biblioteca.listar_usuarios()

        elif opcao == "7":
            minha_biblioteca.listar_todos_livros()

        elif opcao == "0":
            print("\n*** Saindo do sistema... Até logo! ***\n")
            break
        else:
            print("\n*** Opção inválida, por favor, tente novamente. ***\n")

if __name__ == "__main__":
    main()