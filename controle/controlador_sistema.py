from tela.tela_sistema import TelaSistema
from controle.controlador_alunos import ControladorAlunos
from controle.controlador_professores import ControladorProfessores
# from controle.controlador_disciplinas import ControladorDisciplinas
# from controle.controlador_atividades import ControladorAtividades

class ControladorSistema:

    def __init__(self):
        self.__controlador_alunos = ControladorAlunos(self)
        self.__controlador_professores = ControladorProfessores(self)
        # self.__controlador_disciplinas = ControladorDisciplinas(self)
        # self.__controlador_atividades = ControladorAtividades(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_alunos(self):
        return self.__controlador_alunos

    @property
    def controlador_professores(self):
        return self.__controlador_professores

    # @property
    # def controlador_disciplinas(self):
    #     return self.__controlador_disciplinas
    #
    # @property
    # def controlador_atividades(self):
    #     return self.__controlador_atividades

    def inicia_sistema(self):
        self.abre_tela()

    def menu_alunos(self):
        self.__controlador_alunos.abre_tela()

    def menu_professores(self):
        self.__controlador_professores.abre_tela()

    # def menu_disciplinas(self):
    #     self.__controlador_disciplinas.abre_tela()
    #
    # def menu_atividades(self):
    #     self.__controlador_atividades.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.menu_alunos,
                        2: self.menu_professores,
                        # 3: self.menu_disciplinas,
                        # 4: self.menu_atividades,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            try:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            except KeyError:
                print("Entrada inválida! Informe uma opção da lista de opções.")
