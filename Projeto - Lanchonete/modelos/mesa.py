class Mesa:
    """Representa uma mesa da lanchonete."""

    def __init__(self, numero: int) -> None:
        self.__numero: int = numero
        self.__ocupada: bool = False

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def ocupada(self) -> bool:
        return self.__ocupada

    def ocupar(self) -> None:
        self.__ocupada = True

    def desocupar(self) -> None:
        self.__ocupada = False
