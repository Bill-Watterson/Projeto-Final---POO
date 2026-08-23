class Pagamento:
    """Representa um valor pago para abater do saldo da comanda."""

    def __init__(self, valor: float) -> None:
        self.__valor: float = valor

    @property
    def valor(self) -> float:
        return self.__valor
