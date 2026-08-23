from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lanchonete import Lanchonete


class Tela(ABC):
    def __init__(self, lanchonete: "Lanchonete") -> None:
        self._lanchonete: "Lanchonete" = lanchonete
