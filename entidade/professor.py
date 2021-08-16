from entidade.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome: str, cpf: str, email: str, id: str):
        super().__init__(nome, cpf, email)
        if isinstance(id, str):
            self.id = id

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, id: str):
        if isinstance(id, str):
            self.__id = id