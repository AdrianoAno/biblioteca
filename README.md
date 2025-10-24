🧑‍💻 Adriano Santos

    Desenvolvido como projeto de prática em Python e POO.
📅 Outubro de 2025  

    Contato:    adrianossantos97@gmail.com  
    
    Linkedin:   www.linkedin.com/in/adriano-santos-83b2b9263  
    
    Github:     https://github.com/AdrianoAno

<br>
<h1> 📚 Sistema de Biblioteca em Python </h1>

<h2>Um sistema simples e funcional para gerenciamento de uma biblioteca, desenvolvido em Python, utilizando os princípios da Programação Orientada a Objetos (POO).</h2>

<br>
<h1> Sobre o Projeto</h1>

<h2>O sistema permite que um administrador (ou atendente da biblioteca) possa:

📘 Cadastrar novos livros

👤 Cadastrar novos usuários

🔍 Buscar livros por nome (ou parte do nome)

📖 Emprestar e devolver livros

📄 Visualizar todos os livros cadastrados

🧾 Listar usuários registrados

O programa é totalmente executado no terminal, com menus interativos e feedbacks claros sobre cada ação.</h2>

<br>
<h1>⚙️ Funcionalidades Principais</h1>

<br>
<h2>📘 Classe Livro

Representa os livros da biblioteca.

Atributos:

* _titulo: título do livro

* _autor: nome do autor

* _ano: ano de publicação

* _disponivel: status do livro (disponível ou emprestado)

Métodos:

emprestar(): altera o status do livro para emprestado

devolver(): devolve o livro, tornando-o disponível novamente

__str__(): retorna uma representação textual formatada do livro</h2>

<br>
<h2>👤 Classe Usuario

Representa um usuário cadastrado na biblioteca.

Atributos:

* _nome, _telefone, _email, _endereco, _idade

* _livros_emprestados: lista com os livros que o usuário pegou emprestados

Métodos:

* adicionar_emprestimo(livro)

* remover_emprestimo(livro)

* __str__(): retorna uma descrição do usuário</h2>

<br>
<h2>🏛️ Classe Biblioteca

Gerencia todo o funcionamento do sistema.

Atributos:

* _nome: nome da biblioteca

* _livros: lista de livros cadastrados

* _usuarios: lista de usuários registrados

Principais métodos:

* cadastrar_livro()

* criar_usuario()

* buscar_livro()

* emprestar_livro()

* devolver_livro()

* listar_todos_livros()

* listar_usuarios()

* encontrar_livro(titulo)

* encontrar_usuario(email)</h2>

<br>
<h1>Menu Principal:</h1>

<h2>
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
</h2>

<br>
<h1> Exemplo de uso: </h1>

<h2>

Bem-vindo ao sistema da Biblioteca Pública de Cubatão!  

  
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
=> 1  
*** Cadastro de Novo Livro ***  
  
Título: Dom Casmurro  
Autor: Machado de Assis  
Ano: 1899  
  
Livro 'Dom Casmurro' cadastrado com sucesso!  

</h2>

<br>
<h1>🧠 Conceitos Aplicados </h1>

<h2>
  
* Encapsulamento: uso de atributos privados (_atributo)

* Abstração: classes bem definidas para entidades reais

* Reutilização de código: separação lógica entre classes e responsabilidades

* Orientação a Objetos: instâncias de Livro, Usuario e Biblioteca interagem entre si
</h2>


<h1> Diagrama UML de Classes — Sistema de Biblioteca </h1>

![Diagrama UML]("https://github.com/AdrianoAno/biblioteca/blob/main/Diagrama%20UML.png")
