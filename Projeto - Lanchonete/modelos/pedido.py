from modelos.produto import Produto


class Pedido:
    """Representa um produto solicitado com sua respectiva quantidade."""

    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.__produto: Produto = produto
        self.__quantidade: int = quantidade

    @property
    def produto(self) -> Produto:
        return self.__produto

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @property
    def valor_total(self) -> float:
        return self.__produto.preco * self.__quantidade
