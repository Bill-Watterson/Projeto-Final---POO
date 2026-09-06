from modelos.mesa import Mesa
from modelos.produto import Produto
from modelos.atendimento import Atendimento


class Lanchonete:
    """
    Classe de Aplicação.
    Responsabilidade: Manter os dados em memória e fornecer acesso encapsulado.
    Não possui mais regras de negócio.
    """

    def __init__(self) -> None:
        self.__mesas: list[Mesa] = []
        self.__produtos: list[Produto] = []
        self.__atendimentos: list[Atendimento] = []
        self.__historico: list[Atendimento] = []

    @property
    def mesas(self) -> list[Mesa]:
        return self.__mesas

    @property
    def produtos(self) -> list[Produto]:
        return self.__produtos

    @property
    def atendimentos(self) -> list[Atendimento]:
        return self.__atendimentos

    @property
    def historico(self) -> list[Atendimento]:
        return self.__historico