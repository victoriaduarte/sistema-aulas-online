
class TelaAluno():

    def tela_opcoes(self):
        print("\n-------- ALUNOS ----------")
        print("Lista de opções")
        print("1 - Cadastrar Aluno")
        print("2 - Editar Aluno")
        print("3 - Listar Alunos")
        print("4 - Excluir Aluno")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input(">>> Escolha a opção: "))
                return opcao
            except ValueError:
                print("Entrada inválida! A opção deve ser um número inteiro.")

    def pega_dados_aluno(self):
        print("\n-------- DADOS ALUNO ----------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        matricula = input("Matricula: ")

        return {"nome": nome, "cpf": cpf, "email": email, "matricula": matricula}

    def mostra_aluno(self, dados_aluno):
        print("\nNOME:", dados_aluno["nome"])
        print("CPF:", dados_aluno["cpf"])
        print("EMAIL:", dados_aluno["email"])
        print("MATRICULA:", dados_aluno["matricula"])

    def seleciona_aluno(self):
        matricula = input("\n>>> Matricula do aluno que deseja selecionar: ")
        return matricula

    def mostra_mensagem(self, msg):
        print(msg)