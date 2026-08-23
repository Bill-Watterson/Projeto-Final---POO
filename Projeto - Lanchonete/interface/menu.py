from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lanchonete import Lanchonete


class Menu(ABC):
    def __init__(self, lanchonete: "Lanchonete") -> None:
        self._lanchonete: "Lanchonete" = lanchonete

    @abstractmethod
    def executar(self) -> None:
        pass
