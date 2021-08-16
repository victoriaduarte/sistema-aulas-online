class TelaSistema:

    def tela_opcoes(self):
        print("\n-------- Sistema de Aulas Online ---------")
        print("Lista de opções")
        print("1 - Alunos")
        print("2 - Professores")
        # print("3 - Disciplinas")
        # print("4 - Atividades")
        print("0 - Finalizar sistema")

        while True:
            try:
                opcao = int(input(">>> Escolha a opção: "))
                return opcao
            except ValueError:
                print("Entrada inválida! A opção deve ser um número inteiro.")
