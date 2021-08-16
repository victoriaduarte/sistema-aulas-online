from tela.tela_professor import TelaProfessor
from entidade.professor import Professor


class ControladorProfessores():

    def __init__(self, controlador_sistema):
        self.__professores = []
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema

    def pega_professor_por_id(self, id: str):
        for professor in self.__professores:
            if professor.id == id:
                return professor
        return None

    def cadastrar_professor(self):
        dados_professor = self.__tela_professor.pega_dados_professor()
        professor = Professor(dados_professor["nome"], dados_professor["cpf"],
                              dados_professor["email"], dados_professor["id"])
        self.__professores.append(professor)
        self.__tela_professor.mostra_mensagem("\n>>> Professor cadastrado com sucesso!")

    def editar_professor(self):
        self.lista_professores()
        id_professor = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_id(id_professor)

        if professor is not None:
            novos_dados_professor = self.__tela_professor.pega_dados_professor()
            professor.nome = novos_dados_professor["nome"]
            professor.cpf = novos_dados_professor["cpf"]
            professor.email = novos_dados_professor["email"]
            professor.id = novos_dados_professor["id"]
            self.lista_professores()
        else:
            self.__tela_professor.mostra_mensagem("\nATENÇÃO: Professor não existente")

    def lista_professores(self):
        if len(self.__professores) == 0:
            self.__tela_professor.mostra_mensagem("\nATENÇÃO: Não há professores cadastrados")
        else:
            print("\n**** ALUNOS CADASTRADOS ****")
            for professor in self.__professores:
                self.__tela_professor.mostra_professor({"nome": professor.nome, "cpf": professor.cpf,
                                                        "email": professor.email, "id": professor.id})

    def excluir_professor(self):
        self.lista_professores()
        id_professor = self.__tela_professor.seleciona_professor()
        professor = self.pega_professor_por_id(id_professor)

        if professor is not None:
            self.__professores.remove(professor)
            self.lista_professores()
            self.__tela_professor.mostra_mensagem("\n>>> Professor excluído com sucesso!")
        else:
            self.__tela_professor.mostra_mensagem("\nATENÇÃO: Professor não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_professor,
                        2: self.editar_professor,
                        3: self.lista_professores,
                        4: self.excluir_professor,
                        0: self.retornar}

        while True:
            lista_opcoes[self.__tela_professor.tela_opcoes()]()
