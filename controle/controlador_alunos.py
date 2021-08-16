from tela.tela_aluno import TelaAluno
from entidade.aluno import Aluno


class ControladorAlunos():

    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema

    def pega_aluno_por_matricula(self, matricula: str):
        for aluno in self.__alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def cadastrar_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        aluno = Aluno(dados_aluno["nome"], dados_aluno["cpf"],
                      dados_aluno["email"], dados_aluno["matricula"])
        self.__alunos.append(aluno)
        self.__tela_aluno.mostra_mensagem("\n>>> Aluno cadastrado com sucesso!")

    def editar_aluno(self):
        self.lista_alunos()
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula_aluno)

        if aluno is not None:
            novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
            aluno.nome = novos_dados_aluno["nome"]
            aluno.cpf = novos_dados_aluno["cpf"]
            aluno.email = novos_dados_aluno["email"]
            aluno.matricula = novos_dados_aluno["matricula"]
            self.lista_alunos()
        else:
            self.__tela_aluno.mostra_mensagem("\nATENÇÃO: Aluno não existente")

    def lista_alunos(self):
        if len(self.__alunos) == 0:
            self.__tela_aluno.mostra_mensagem("\nATENÇÃO: Não há alunos cadastrados")
        else:
            print("\n**** ALUNOS CADASTRADOS ****")
            for aluno in self.__alunos:
                self.__tela_aluno.mostra_aluno({"nome": aluno.nome, "cpf": aluno.cpf,
                                                "email": aluno.email, "matricula": aluno.matricula})

    def excluir_aluno(self):
        self.lista_alunos()
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_por_matricula(matricula_aluno)

        if aluno is not None:
            self.__alunos.remove(aluno)
            self.lista_alunos()
            self.__tela_aluno.mostra_mensagem("\n>>> Aluno excluído com sucesso!")
        else:
            self.__tela_aluno.mostra_mensagem("\nATENÇÃO: Aluno não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_aluno,
                        2: self.editar_aluno,
                        3: self.lista_alunos,
                        4: self.excluir_aluno,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
