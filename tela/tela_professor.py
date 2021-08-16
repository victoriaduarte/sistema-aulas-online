
class TelaProfessor():

    def tela_opcoes(self):
        print("\n-------- PROFESSORES ----------")
        print("Lista de opções")
        print("1 - Cadastrar Professor")
        print("2 - Editar Professor")
        print("3 - Listar Professores")
        print("4 - Excluir Professor")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input(">>> Escolha a opção: "))
                return opcao
            except ValueError:
                print("Entrada inválida! A opção deve ser um número inteiro.")

    def pega_dados_professor(self):
        print("\n------ DADOS PROFESSOR --------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        email = input("Email: ")
        id = input("ID: ")

        return {"nome": nome, "cpf": cpf,  "email": email, "id": id}

    def mostra_professor(self, dados_professor):
        print("\nNOME:", dados_professor["nome"])
        print("CPF:", dados_professor["cpf"])
        print("EMAIL:", dados_professor["email"])
        print("ID:", dados_professor["id"])

    def seleciona_professor(self):
        id = input("\n>>> ID do professor que deseja selecionar: ")
        return id

    def mostra_mensagem(self, msg):
        print(msg)