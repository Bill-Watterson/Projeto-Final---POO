from abc import ABC, abstractmethod


class Produto(ABC):
    """Classe abstrata base para os produtos comercializados."""

    def __init__(self, codigo: int, nome: str, preco: float) -> None:
        self.__codigo: int = codigo
        self.__nome: str = nome
        self.__preco: float = preco
        self.__disponivel: bool = True

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def preco(self) -> float:
        return self.__preco

    @property
    def disponivel(self) -> bool:
        return self.__disponivel

    @abstractmethod
    def descricao_detalhada(self) -> str:
        """Exibe os dados detalhados utilizando polimorfismo."""
        pass


class Suco(Produto):
    def __init__(self, codigo: int, nome: str, preco: float, tamanho: str) -> None:
        super().__init__(codigo, nome, preco)
        self.__tamanho: str = tamanho

    @property
    def tamanho(self) -> str:
        return self.__tamanho

    def descricao_detalhada(self) -> str:
        return f"Suco: {self.nome} ({self.__tamanho})"


class Sanduiche(Produto):
    def __init__(self, codigo: int, nome: str, preco: float, pao: str) -> None:
        super().__init__(codigo, nome, preco)
        self.__pao: str = pao

    @property
    def pao(self) -> str:
        return self.__pao

    def descricao_detalhada(self) -> str:
        return f"Sanduíche: {self.nome} (Pão: {self.__pao})"


class SaladaDeFrutas(Produto):
    def __init__(self, codigo: int, nome: str, preco: float, adicional: str) -> None:
        super().__init__(codigo, nome, preco)
        self.__adicional: str = adicional

    @property
    def adicional(self) -> str:
        return self.__adicional

    def descricao_detalhada(self) -> str:
        return f"Salada de Frutas: {self.nome} (+{self.__adicional})"
